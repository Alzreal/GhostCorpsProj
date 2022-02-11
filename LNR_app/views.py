from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
import bcrypt

def landing(request):
    return render(request, 'LNR_app/landing.html')

def index(request):
    return render(request, 'LNR_app/index.html')

def register(request):
    errors=User.objects.register_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

    user=User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=pw_hash,
        )

    request.session['user_id']=user.id
    return redirect ('gb/')

def success(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You must be logged in to see this site!')
        return redirect('/')
    user=User.objects.get(id=request.session['user_id'])
    context={
        'user':user
    }
    return render (request, 'gb/', context)

def login(request):
    errors=User.objects.login_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    request.session['user_id'] = User.objects.get(email=request.POST['logusername']).id
    return redirect ('gb/')

def logout(request):
    request.session.flush()
    return redirect('/')