from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Signup_stu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10, null=True)
    role = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.user.username

class Signup_fac(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10, null=True)
    faculty_id = models.CharField(max_length=10,null=True)
    role = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.user.username

