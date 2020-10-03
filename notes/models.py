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
    fac_id = models.IntegerField(max_length=10, null=True, unique=True)
    status = models.IntegerField(max_length=1, null=True)

    def _str__(self):
        return self.fac_id

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploading_date = models.CharField(max_length=30)
    category =models.CharField(max_length=20)
    subject =models.CharField(max_length=10)
    Note_file =models.FileField(null=True)
    file_type = models.CharField(max_length=30)
    description = models.CharField(max_length=200,null=True)

    def __str__(self):
        return Signup_fac.user.username