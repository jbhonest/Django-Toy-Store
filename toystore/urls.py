from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from home.views import index

urlpatterns = [
    path('', index, name='index'),
    path(getattr(settings, 'ADMIN_URL'), admin.site.urls),
    path('api/blog/', include('blog.urls')),
    path('api/store/', include('store.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/finance/', include('finance.urls')),

    # SimpleJWT URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
