# models.py

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True, null=True)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(max_length=100,blank=True, null=True)
    gender = models.CharField(max_length=10,blank=True, null=True)
    nationality = models.CharField(max_length=100,blank=True, null=True)
    phone = models.CharField(max_length=20,blank=True, null=True)
    university = models.CharField(max_length=100,blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(max_length = 1000, blank=True, null=True)
    street = models.CharField(max_length=100,blank=True, null=True)
    city = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.user.username
