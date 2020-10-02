from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('about', views.about, name='about'),
    path('contact', views.contact, name="contact"),
    path('login/', views.login_stu, name="login"),
    path('admin_login', views.admin_log, name='admin_login'),
    path('signup_stu', views.signup_student, name='signup_stu'),
    path('signup_fac', views.signup_fac, name="signup_fac"),
    path('logout', views.Logout, name='logout'),
    path('profile', views.profile, name='profile'),
]

