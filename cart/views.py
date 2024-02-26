from django.db import transaction
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Cart, CartItem
from finance.models import Order, OrderItem
from finance.serializers import OrderSerializer
from .serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.order_by('-pk')
    serializer_class = CartSerializer

    @action(detail=True, methods=['get', 'post'])
    def checkout(self, request, pk=None):
        cart = self.get_object()

        if cart.items.count() == 0:
            return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                # Create a new order based on current cart
                order = Order.objects.create(user=self.request.user)
                order_items = [
                    OrderItem(
                        order=order,
                        product=item.product,
                        price=item.product.price,
                        quantity=item.quantity
                    ) for item in cart.items.all()
                ]
                OrderItem.objects.bulk_create(order_items)

                # Delete current cart
                Cart.objects.filter(pk=cart.id).delete()

                order_serializer = OrderSerializer(order)
                return Response(order_serializer.data)
        except ValueError:
            return Response({"error": "You must login to checkout"}, status=status.HTTP_401_UNAUTHORIZED)


class CartItemViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}

    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])
