from rest_framework import viewsets
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.order_by('-pk')
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderItemSerializer

    def get_serializer_context(self):
        return {'order_id': self.kwargs['order_pk']}

    def get_queryset(self):
        return OrderItem.objects.filter(order_id=self.kwargs['order_pk'])
