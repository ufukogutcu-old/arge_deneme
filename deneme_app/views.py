from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Item
from django.contrib.auth.models import User
from .serializers import ItemSerializer, UserSerializer

# Create your views here.


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


def home_view(request):
    return render(request, 'home.html')

