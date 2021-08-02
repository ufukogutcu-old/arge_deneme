from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class MyUser(AbstractUser):
    class Meta:
        verbose_name = 'User'

    def __str__(self):
        return self.username


class Item(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    size = models.IntegerField()
    color = models.CharField(max_length=10)
    creator = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        string = str(self.name) + ':' + str(self.size) + ':' + str(self.color) + ':' + str(self.creator)
        return string
