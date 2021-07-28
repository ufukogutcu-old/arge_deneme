from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.backends import BaseBackend


# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    size = models.IntegerField()
    color = models.CharField(max_length=10)
