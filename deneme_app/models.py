from django.db import models


# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    size = models.IntegerField()
    color = models.CharField(max_length=10)
