from django.contrib.auth.models import AnonymousUser
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
    if str(user) == 'AnonymousUser':
        items = Item.objects.all()
        is_logged_in = False
    else:
        items = Item.objects.filter(
            Q(creator=user) & Q(size__gte=0)
        )
        is_logged_in = True
    context = {
        'items': items,
        'isLoggedIn': is_logged_in,
    }
    return render(request, 'home.html', context)
