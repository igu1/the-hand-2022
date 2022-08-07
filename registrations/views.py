from django.contrib import auth
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.messages.views import messages


def login_view(request):
    if request.method == 'POST' and 'login' in request.POST:
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username + password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, message='Invalid username or password!')
    return render(request, 'login.html')


def forgot_password(request):
    return HttpResponse("<h1 style='color: red;'>Forgot Password Function Will be Added Soon</h1>\n<p>: For now "
                        "Contact With Admin</p>")


def register_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'registration.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, message='You Have Been Logged Out!')
    return redirect('login')
