from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .decorators import login_excluded, send_forget_password_mail
from django.contrib.auth.models import User
import uuid


# Create your views here.
@login_excluded()
def login_view(request):
    if request.method == 'POST' :
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login, password=password_login)
        if user is not None:
            login(request, user)
            return redirect('default')
        else :
            messages.info(request, "Username or password is incorrect!")
    return render(request, "login.html")

@login_excluded()
def forgot_password(request):
    try :
        if request.method == 'POST':
            email_user = request.POST.get('email')

            if not User.objects.filter(email = email_user):
                messages.info(request, "User with email is not exists")
                return redirect('forgot_password')
            else:
                token = str(uuid.uuid4())
                user_obj = User.objects.get(email = email_user)
                send_forget_password_mail(user_obj, token)
                messages.info(request, "Check your email for password recovery link")
                return redirect('login')
    except Exception as e :
        print(e)
    return render(request, "forget-password.html")

@login_excluded()
def change_password(request, id):
    user_obj = User.objects.get(id = id)
    if request.method == 'POST':
        new_password = request.POST.get('pass1')
        confirm_password = request.POST.get('pass2')

        if len(new_password) <8 :
            messages.info(request, 'Your password must consist of at least 8 characters!')
            return redirect(f'change-password/{id}')

        elif new_password != confirm_password:
            messages.info(request, 'Password don\'t match')
            return redirect(f'change-password/{id}')

        user_obj.set_password(new_password)
        user_obj.save()
        messages.info(request, 'Password has been renewd sucessfully')
        return redirect('login')
    return render(request, 'change-password.html')
