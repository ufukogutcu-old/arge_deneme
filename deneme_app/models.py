from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Item(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    size = models.IntegerField()
    color = models.CharField(max_length=10)
