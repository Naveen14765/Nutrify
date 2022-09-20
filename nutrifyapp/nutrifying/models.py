from django.db import models
from django.contrib.auth.models import User
import datetime


class Health(models.Model):
    food = models.CharField(max_length=50)
    weight = models.IntegerField(blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)
    userName = models.CharField(max_length=50, null=True)
    currentdate = models.DateField(default=datetime.date.today())
    timestamp = models.DateTimeField(auto_now_add=True)


class Excercise(models.Model):
    excercise = models.CharField(max_length=50)
    calories = models.IntegerField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    userName = models.CharField(max_length=50, null=True)
    currentdate = models.DateField(default=datetime.date.today())


class DateField(models.Model):
    userinput = models.DateField()


class CommunityPeople(models.Model):
    posts = models.ImageField(upload_to='images', null=True)
    comment = models.TextField(null=True)
    userName = models.CharField(max_length=50, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


