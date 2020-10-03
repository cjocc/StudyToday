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
            error='no'
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
                login(request, user)
                error='no'
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
    error = ""
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        mob = request.POST['m_number']
        email = request.POST['email_id']
        pwd = request.POST['password']
        id = request.POST['fac_id']
        r = 'T'
        f_ids = fac_id.objects.all()
        for fid in f_ids:
            if fid.fac_id == id and fid.status == 1:
                error = 'yes'
                break
        if not fac_id.objects.filter(fac_id=id):
            error = "yes"

        if error == "":
            try:
                user = User.objects.create_user(username=email, password=pwd, first_name=f_name, last_name=l_name)
                Signup_fac.objects.create(user=user, contact=mob, faculty_id=id, role=r)
                f_stat = fac_id.objects.get(fac_id=id)
                f_stat.status = 1
                f_stat.save()
                error = "no"
            except:
                error = 'yes'
    d = {'error': error}
    return render(request, 'signup_fac.html', d)


def Logout(request):
    logout(request)
    return redirect('index')


def profile(request):
    return render(request, 'profile.html')


def edit_notes(request):
    role = ""
    if not request.user.is_authenticated:
        redirect('login')
    user= User.objects.get(id=request.user.id)
    data_Stu= Signup_stu.objects.filter(user=user)
    data_fac= Signup_fac.objects.filter(user=user)
    if data_Stu.exists():
        role='S';
    if data_fac.exists():
        role='T'
    d={'role':role}
    return render(request, 'edit_notes.html', d)


def explore_notes(request):
    return render(request,'explorenotes.html')
