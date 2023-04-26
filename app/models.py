from turtle import update
from unicodedata import name
from venv import create
from django.db import models
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import User





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




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    reset_password_token = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse_lazy('edit', args=[str(self.id)])