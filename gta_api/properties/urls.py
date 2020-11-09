from django.conf.urls import include, url
from rest_framework import routers
from . import views


router = routers.SimpleRouter()
router.register(r'properties', views.PropertyViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
