from rest_framework import viewsets
from .models import Product, Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.order_by('-pk')
    serializer_class = CartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.order_by('-pk')
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
