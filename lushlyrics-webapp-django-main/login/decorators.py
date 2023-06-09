from django.shortcuts import redirect
from django.conf import settings
from django.core.mail import send_mail
def login_excluded():
    def decorator(view_method):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated :
                return redirect('default')
            return view_method(request, *args, **kwargs)
        return wrapper_func
    return decorator

def send_forget_password_mail(email, token):
    id = email.id
    subject = 'Forgot Password Youtify'
    message = f'Click this link to reset your password! \n http:http://127.0.0.1:8000/change-password/{id}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email.email]
    send_mail(subject,message,email_from,recipient_list)
    return True

