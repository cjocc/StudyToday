from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Signup_stu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.IntegerField(max_length=10, null=True)
    role = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.user.username
    def get_role(self):
        return self.user.role

class Signup_fac(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10, null=True)
    faculty_id = models.IntegerField(max_length=10,null=True,unique=True)
    role = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.user.username

    def get_role(self):
        return self.user.role


class fac_id(models.Model):
    fac_id = models.IntegerField(max_length=10, null=True,unique=True)
    status = models.IntegerField(max_length=1, null=True)

    def _str__(self):
        return self.fac_id