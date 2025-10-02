from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, AddressViewSet, BankViewSet

router = DefaultRouter()
router.register("users", UserViewSet)
router.register("addresses", AddressViewSet)
router.register("banks", BankViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
