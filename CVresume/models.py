from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Resume(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(choices=(
        ('M','M'),
        ('W','W'),
    ),max_length=50)
    bio = models.CharField(max_length=200)
    photo = models.ImageField(blank=True,null=True)


class Experience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    position = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    country = models.CharField(max_length=20)
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE,related_name='expi')


class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    school_name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    spec = models.CharField(max_length=20)
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE,related_name='edu')


class Languages(models.Model):
    name = models.CharField(max_length=20)
    level = models.CharField(choices=(
        ('A1','A1'),
        ('A2','A2'),
        ('B1','B2'),
        ('B2','B2'),
        ('C1','C1'),
        ('C2','C2'),
    ),max_length=20)
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE,related_name='language')


class Skills(models.Model):
    name = models.CharField(max_length=50)
    skill_level = models.IntegerField(default=0)
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE,related_name='skill')


class Certifications(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    image = models.ImageField()
    link = models.CharField(max_length=50)
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE,related_name='certification')




