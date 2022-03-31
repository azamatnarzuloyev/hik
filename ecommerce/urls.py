from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from decouple import config
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

# admin.autodiscover()
# admin.site.enable_nav_sidebar = False

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Azamat narzulloyev",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="azamatsabina1796@mail.ru"),
#       license=openapi.License(name="elektron dokon lisensiya"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )
from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularRedocView, 
    SpectacularSwaggerView
)



urlpatterns = [
  
   path('admin/', admin.site.urls),
   path('api/v1/', include("product.urls")),
   path('api/v1/account/', include('account.urls', namespace='account')),
   path('blog/', include('blog.urls', namespace='blog')),
   path('comment/', include('comment.urls', namespace='comment')),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   path("api/v1/search/", include("search.urls")),
#    path('api/v1/orders/', include('order.urls')),
   path('api/v1/tolov/', include('tolov.urls', namespace='tolov')),
#    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),  name='schema-redoc'),
   path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
   path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
   path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls.static import static
from django.conf import settings

    # add root static files
urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    # add media static files
urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
