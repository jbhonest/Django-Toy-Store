from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, PostViewSet, CommentViewSet, ImageViewSet

category_router = routers.DefaultRouter()
category_router.register('', CategoryViewSet)

post_router = routers.DefaultRouter()
post_router.register('', PostViewSet)

comment_router = routers.DefaultRouter()
comment_router.register('', CommentViewSet)

image_router = routers.DefaultRouter()
image_router.register('', ImageViewSet)

urlpatterns = [
    path('categories/', include(category_router.urls)),
    path('posts/', include(post_router.urls)),
    path('comments/', include(comment_router.urls)),
    path('images/', include(image_router.urls)),
]
