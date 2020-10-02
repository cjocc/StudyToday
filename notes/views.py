from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def login_stu(request):
    return render(request, 'login.html')


def admin_log(request):
    error = "";
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['passwd']
        user = authenticate(request, username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'admin_login.html', d)


def signup_stu(request):
    return render(request, 'signup_stu.html')


def signup_fac(request):
    return render(request, 'signup_fac.html')


def Logout(request):
    logout(request)
    return redirect('index')
