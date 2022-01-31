from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from LNR_app.models import User
from .models import *

def logged_in_user(request):
    return User.objects.get(id=request.session['user_id'])

def index(request):
    context={
        'user':logged_in_user(request)
    }
    return render(request, 'ghost/index.html', context)

def messages(request):
    context={
        'user':logged_in_user(request),
        'jobs':Job.objects.all(),
    }
    return render(request, 'ghost/messages.html', context)

def add_job(request):
    errors=Job.objects.job_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.errors(request, value)
        return redirect('/gb/messages')
    Job.objects.create(user_name=request.POST['user_name'], location=request.POST['location'], contact=request.POST['contact'], job=request.POST['job'], uploaded_by=logged_in_user(request))
    return redirect ('/gb/messages')

def delete_job(request, job_id):
    quote = Job.objects.get(id=job_id)
    quote.delete()
    return redirect ('/gb/messages')

def equipment(request):
    context={
        'user':logged_in_user(request)
    }
    return render(request, 'ghost/equipment.html', context)

def tobins(request):
    context={
        'user':logged_in_user(request)
    }
    return render(request, 'ghost/tobins.html', context)

def founding(request):
    context={
        'user':logged_in_user(request)
    }
    return render(request, 'ghost/founding.html', context)

def EditPage(request):
    context={
        'user':logged_in_user(request)
    }
    return render (request, 'ghost/EditAccount.html', context)

def EditAccount(request):
    context={
        'user':logged_in_user(request)
    }
    User.objects.filter(id=logged_in_user(request).id).update(first_name=request.POST['first_name'], 
    last_name=request.POST['last_name'], 
    email=request.POST['email'])
    return redirect ('/gb/EditAccount', context)

def medicorps(request):
    context={
        'user':logged_in_user(request)
    }
    return render(request, 'ghost/medicorps.html', context)