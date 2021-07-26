from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Item
from django.contrib.auth.models import User


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'size', 'color']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
