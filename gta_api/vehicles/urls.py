from django.conf.urls import include, url
from rest_framework import routers
from . import views


router = routers.SimpleRouter()
router.register(r'vehicles', views.VehicleViewSet)
router.register(r'vehicles_real_life', views.VehicleRealLifeViewSet)
router.register(r'vehicle_workshops', views.VehicleWorkshopViewSet)
router.register(r'vehicle_storage_locations', views.VehicleStorageLocationViewSet)
router.register(r'vehicle_manufacturers', views.VehicleManufacturerViewSet)
router.register(r'vehicle_manufacturers_real_life', views.VehicleManufacturerRealLifeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
