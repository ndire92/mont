from turtle import update
from unicodedata import name
from venv import create
from django.db import models
from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):

    description = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True, default="")
    addresse = models.CharField(max_length=50, null=True, blank=False)
    profile_pic = models.ImageField(upload_to='media/profile_pic')

    def __str__(self):
        return self.description


class CustomUser(models.Model):

    profile_pic = models.ImageField(upload_to='media/profile_pic')


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = RichTextField(blank=True)
    image = models.ImageField(upload_to='media/images/')

    def __str__(self):
        return self.user


class Slider(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/images/')

    sub_title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Ressource(models.Model):
    title = models.CharField(max_length=300)
    mot_cle = RichTextField(blank=True)
    date_en = models.DateField(default=timezone.now)
    action = models.FileField(upload_to='uploads/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
