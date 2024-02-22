from django.urls import path, include
from rest_framework import routers
from .views import CartViewSet

cart_router = routers.DefaultRouter()
cart_router.register('', CartViewSet)


urlpatterns = [
    path('carts/', include(cart_router.urls)),

]
