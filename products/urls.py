from django.urls import path
from rest_framework import routers
from products import views
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'', views.productViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        "noSaleProduct/<int:pk>/",
        views.noSaleProduct.as_view(),
        name="noSaleProduct",
    ),

]