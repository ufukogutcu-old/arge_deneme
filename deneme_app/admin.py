from django.contrib import admin
from .models import Item
# Register your models here.


class ItemAdmin(admin.ModelAdmin):

    class Meta:
        model = Item


admin.site.register(Item, ItemAdmin)
