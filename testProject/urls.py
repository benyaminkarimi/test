
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from drf_yasg import openapi
from django.conf import settings
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static

schema_view = get_schema_view(
    info=openapi.Info(
        title="API",
        default_version="v1",
        description="rightel REST API Tutorial",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email='benyamin.karimii@gmail.com'),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('account/', include('account.urls')),
    path('', schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path('redoc/', schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)