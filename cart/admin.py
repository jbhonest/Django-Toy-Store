from django.contrib import admin
from django.db.models import Count
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product',  'quantity')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item_row', 'created_at')
    list_filter = ('user', )
    inlines = (CartItemInline,)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(item_row=Count('cartitems'))

    @admin.display(ordering='item_row')
    def item_row(self, cart):
        return cart.cartitems.count()
