from django.contrib import admin
from django.db.models import Count
from .models import Cart, CartItem


admin.site.register(Cart)
admin.site.register(CartItem)
