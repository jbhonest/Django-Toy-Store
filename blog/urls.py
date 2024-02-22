from rest_framework import routers
from .views import CategoryViewSet, PostViewSet, CommentViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('images', ImageViewSet)

# URLConf
urlpatterns = router.urls
