from rest_framework.viewsets import ModelViewSet
from .models import Cart, CartItem

from .serializers import CartSerializer, CartItemSerializer


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.order_by('-pk')
    serializer_class = CartItemSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.order_by('-pk')
    serializer_class = CartSerializer
