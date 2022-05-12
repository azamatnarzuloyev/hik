from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularRedocView, 
    SpectacularSwaggerView
)
from django.conf import settings
urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/', include("product.urls")),
   path('api/v1/account/', include('account.urls', namespace='account')),
   path('blog/', include('blog.urls', namespace='blog')),
   path('comment/', include('comment.urls', namespace='comment')),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   path("api/v1/search/", include("search.urls")),

   path('api/v1/tolov/', include('tolov.urls', namespace='tolov')),
   path('api/v1/filter/', include('filter.urls', namespace='filters')),
   path('api/v1/banner/',include('Banner.urls',namespace='banner')),
   path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
   path('api/v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
   path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] 

    # add root static files
urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
#     # add media static files
urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
