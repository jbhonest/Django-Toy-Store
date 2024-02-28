from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions
from .models import Cart, CartItem, Wallet
from finance.models import Order, OrderItem
from finance.serializers import OrderSerializer
from .serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer, WalletSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.order_by('-pk')
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAdminUser]


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.order_by('-pk')
    serializer_class = CartSerializer

    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        cart = self.get_object()

        if cart.items.count() == 0:
            return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                # Create a new order based on current cart
                wallet = Wallet.objects.get(user=self.request.user)
                if wallet.balance >= cart.total_price():
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

                    wallet.balance -= cart.total_price()
                    wallet.save()

                    # Delete current cart
                    Cart.objects.filter(pk=cart.id).delete()

                    order_serializer = OrderSerializer(order)
                    return Response(order_serializer.data)
                else:
                    return Response({"error": "You don't have enough money in your wallet"}, status=status.HTTP_402_PAYMENT_REQUIRED)
        except (ValueError, TypeError):
            return Response({"error": "You must login to checkout"}, status=status.HTTP_401_UNAUTHORIZED)
        except ObjectDoesNotExist:
            return Response({"error": "You don't have a wallet yet"}, status=status.HTTP_402_PAYMENT_REQUIRED)


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
