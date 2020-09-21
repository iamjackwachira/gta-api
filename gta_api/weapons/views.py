from rest_framework import viewsets

from .models import Weapon, WeaponManufacturer, WeaponRealLife
from .serializers import WeaponSerializer, WeaponManufacturerSerializer, WeaponRealLifeSerializer


class WeaponViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer


class WeaponManufacturerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WeaponManufacturer.objects.all()
    serializer_class = WeaponManufacturerSerializer


class WeaponRealLifeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WeaponRealLife.objects.all()
    serializer_class = WeaponRealLifeSerializer
