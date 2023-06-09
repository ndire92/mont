# Generated by Django 4.1.6 on 2023-03-13 16:21

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', ckeditor.fields.RichTextField(blank=True)),
                ('image', models.ImageField(upload_to='media/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/images/')),
                ('title', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
