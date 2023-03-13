from django.db import models

# Create your models here.
from django.db import models
#from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from asyncio import AbstractServer
from django.db import models

from app.models import CustomUser


# from django.contrib.auth.models import User


class Post(models.Model):
    #admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = RichTextField(blank=True)
    image = models.ImageField(upload_to='media/images/')
    


def __str__(self):
    return self.title


class Slider(models.Model):
    
    image = models.ImageField(upload_to='media/images/')
    title = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)
    # sub_title =models.CharField(max_length=25)
