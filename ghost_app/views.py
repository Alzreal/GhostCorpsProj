from multiprocessing import context
from django.shortcuts import render, redirect
from LNR_app.models import User

def logged_in_user(request):
    return User.objects.get(id=request.session['user_id'])

def index(request):
    context={
        'user':logged_in_user(request)
    }
    return render(request, 'ghost/index.html', context)

def messages(request):
    context={
        'user':logged_in_user(request)
    }
    return render(request, 'ghost/messages.html', context)

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