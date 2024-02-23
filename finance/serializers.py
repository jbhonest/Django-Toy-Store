from rest_framework import serializers
from store.models import Product
from .models import Order, OrderItem


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']


class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, order_item: OrderItem):
        return order_item.quantity * order_item.price

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'price', 'quantity', 'total_price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, order):
        return sum([item.quantity * item.price for item in order.items.all()])

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total_price']
