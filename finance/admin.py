from django.contrib import admin
from django.db.models import Count
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'order')
    list_filter = ('product', 'order')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_row', 'created_at', 'user')
    list_filter = ('user',)
    inlines = (OrderItemInline,)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(item_row=Count('items'))

    @admin.display(ordering='item_row')
    def item_row(self, cart):
        return cart.items.count()
