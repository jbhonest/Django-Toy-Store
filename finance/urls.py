from rest_framework_nested import routers
from .views import OrderViewSet, OrderItemViewSet

router = routers.DefaultRouter()
router.register('orders', OrderViewSet)

orders_router = routers.NestedDefaultRouter(router, 'orders', lookup='order')
orders_router.register('items', OrderItemViewSet, basename='order-items')


# URLConf
urlpatterns = router.urls + orders_router.urls
