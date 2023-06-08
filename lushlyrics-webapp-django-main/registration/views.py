from django.shortcuts import render, redirect
from django.contrib import messages
from login.decorators import login_excluded
from .forms import CreateUserForm
# Create your views here.

@login_excluded()
def registrationPage(request):
    if request.method == 'POST' :
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else :
        form = CreateUserForm()
    context = {
        'form':form
    }
    return render(request, "signup.html", context)

