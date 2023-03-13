from turtle import update
from unicodedata import name
from venv import create
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER = (
        (1, 'agriculture'),
        (2, 'foncier'),
        (3, 'peche'),
        (4, 'education'),
        (5, 'sante'),

    )

    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')
    
class Post(models.Model):
    #admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = RichTextField(blank=True)
    image = models.ImageField(upload_to='media/images/')
    user =  models.ForeignKey(CustomUser, on_delete=models.CASCADE)



