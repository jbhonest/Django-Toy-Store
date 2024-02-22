from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, CommentViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('comments', CommentViewSet)
router.register('images', ImageViewSet)

# URLConf
urlpatterns = router.urls
