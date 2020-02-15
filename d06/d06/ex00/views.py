from django.shortcuts import render, redirect
import random
from django.conf import settings
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import RegisterForm

def index(request):
    if 'user_name' not in request.session:
        un = settings.LIST_USER_NAMES[random.randint(0, 9) % 10]
        request.session['user_name'] = un
        request.session.set_expiry(42)
        print(f'Expire date for {un}: {request.session.get_expiry_date()}')

    # Get a session value -- this could be called in a different view,
    # or many requests later (or both):

    user_name = request.session['user_name']

    # Clear an item from the session:
    # del request.session['user_name']
    
    return render(request, 'index.html', {'user_name': user_name})


# def login(request):
#     form = 
#     return render(request, 'ex00/registration/login.html', {'form': form})


def register(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()
	    return redirect("../")
    else:
	    form = RegisterForm()
    return render(response, 'ex00/register.html', {'form': form})
