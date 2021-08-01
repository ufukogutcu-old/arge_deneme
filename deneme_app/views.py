from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Item, MyUser
from .serializers import ItemSerializer, UserSerializer
from django.db.models import Q


# Create your views here.


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


def home_view(request):
    user = request.user
    items = Item.objects.filter(
        Q(creator=user) & Q(size__gte=0)
    )
    context = {
        'items': items,
    }
    return render(request, 'home.html', context)
