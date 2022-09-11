from django.db import models
from django.contrib.auth.models import User


class Health(models.Model):
    food = models.CharField(max_length=50)
    weight = models.IntegerField(blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)
    userName = models.CharField(max_length=50, null=True)


class Excercise(models.Model):
    excercise = models.CharField(max_length=50)
    calories = models.IntegerField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    userName = models.CharField(max_length=50, null=True)

