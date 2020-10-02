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
    error = "";
    if request.method == 'POST':
        u = request.POST['email_id']
        p = request.POST['passwd']
        user = authenticate(request, username=u, password=p)
        try:
                login(request, user)
                error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)


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


def signup_student(request):
    error = ""
    if request.method =='POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        mob = request.POST['m_number']
        email = request.POST['email_id']
        pwd = request.POST['password']
        r = 'S'

        try:
            user = User.objects.create_user(username=email, password=pwd, first_name=f_name, last_name=l_name)
            Signup_stu.objects.create(user=user,contact=mob, role=r)
            error = "no"
            print("error here")
        except Exception as e:
            error = 'yes'
            print(e)

    d = {'error': error}
    return render(request,'signup_stu.html', d)


def signup_fac(request):
    return render(request, 'signup_fac.html')


def Logout(request):
    logout(request)
    return redirect('index')


def profile(request):
    return render(request, 'profile.html')
