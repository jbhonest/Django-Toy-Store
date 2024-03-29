from django.contrib import admin
from django.db.models import Count
from .models import Cart, CartItem, Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'balance')


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'cart')
    list_filter = ('product', 'cart')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_row', 'created_at')
    inlines = (CartItemInline,)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(item_row=Count('items'))

    @admin.display(ordering='item_row')
    def item_row(self, cart):
        return cart.items.count()
