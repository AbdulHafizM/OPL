from audioop import maxpp
from distutils.command.upload import upload
from email.policy import default
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here. 


class Calendar(models.Model):
    name = models.CharField(max_length=25)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)


    def __str__(self):
        return str(self.name)


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True)
    image = models.ImageField(default='')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return str(self.title)


class_choices = (('jss1', 'JSS1'),
    ('jss2', 'JSS2'),
    ('jss3', 'JSS3'),
    ('ss1', 'SS1'),
    ('ss2', 'SS2'),
    ('ss3', 'SS3'))


class Admission(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.CharField(max_length=2)
    student_class = models.CharField(max_length=4, choices=class_choices, default='jss1')
    parent_name = models.CharField(max_length=25)
    number = models.CharField(max_length=11)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
