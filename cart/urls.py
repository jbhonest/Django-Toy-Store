from django.urls import path
from rest_framework_nested import routers
from .views import CartViewSet, CartItemViewSet

router = routers.DefaultRouter()
router.register('carts', CartViewSet)

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', CartItemViewSet, basename='cart-items')


# URLConf
urlpatterns = router.urls + carts_router.urls

urlpatterns += [
    # Add the checkout URL
    path('carts/<int:pk>/checkout/',
         CartViewSet.as_view({'post': 'checkout'}), name='cart-checkout'),
]
