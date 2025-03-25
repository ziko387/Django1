from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import title
from django.contrib.auth import get_user_model
#create a custom user model
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True,blank=True,null=True)
    profile_picture = models.ImageField(upload_to="profile_pictures",blank=True,null=True)

    def __str__(self):
        return self.username
# Create your models here.
class Taskers(models.Model):
    """custom class for our taskers"""
    username =models.CharField(max_length=100,unique=True)
    email=models.EmailField(unique=True)
    create=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username

class Task(models.Model):
 ##attributes
    title=models.CharField(max_length=1000 ,unique=True)
    completed=models.BooleanField(default=False)
    create=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    #here establishing a one to many relationship#
    tasker=models.ForeignKey(Taskers,on_delete=models.SET_NULL,null=True,blank=True)
    user=models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
         return self.title

"""
    1. python manage.py cooler zero=resets for the app
    """""