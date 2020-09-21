from django.conf.urls import include, url
from rest_framework import routers
from . import views


router = routers.SimpleRouter()
router.register(r'weapons', views.WeaponViewSet)
router.register(r'weapons_real_life', views.WeaponRealLifeViewSet)
router.register(r'weapon_manufacturers', views.WeaponManufacturerViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
