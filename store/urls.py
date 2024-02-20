from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, CommentViewSet, ImageViewSet

category_router = routers.DefaultRouter()
category_router.register('', CategoryViewSet)

product_router = routers.DefaultRouter()
product_router.register('', ProductViewSet)

comment_router = routers.DefaultRouter()
comment_router.register('', CommentViewSet)

image_router = routers.DefaultRouter()
image_router.register('', ImageViewSet)

urlpatterns = [
    path('categories/', include(category_router.urls)),
    path('products/', include(product_router.urls)),
    path('comments/', include(comment_router.urls)),
    path('images/', include(image_router.urls)),
]
