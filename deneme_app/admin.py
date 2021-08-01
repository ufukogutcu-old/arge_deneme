from django.contrib import admin
from deneme_app.models import Item, MyUser
# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    class Meta:
        model = Item


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = MyUser


admin.site.register(Item, ItemAdmin)
admin.site.register(MyUser, UserAdmin)
