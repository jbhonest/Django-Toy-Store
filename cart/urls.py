from django.urls import path, include
from rest_framework import routers
from .views import CartViewSet, CartItemViewSet

cart_router = routers.DefaultRouter()
cart_router.register('', CartViewSet)


cartitem_router = routers.DefaultRouter()
cartitem_router.register('', CartItemViewSet)

urlpatterns = [
    path('carts/', include(cart_router.urls)),
    path('cart-items/', include(cartitem_router.urls)),
]
