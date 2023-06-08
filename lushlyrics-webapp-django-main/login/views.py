from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .decorators import login_exlcluded


# Create your views here.
@login_exlcluded()
def login_view(request):
    if request.method == 'POST' :
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login, password_login=password_login)
        if user is not None:
            login(request, user)
            return redirect('default')
        else :
            messages.info(request, "Username or password is incorrect!")