from rest_framework import viewsets

from .models import (Vehicle, VehicleStorageLocation, VehicleManufacturer,
                     VehicleWorkshop, VehicleRealLife, VehicleManufacturerRealLife)
from .serializers import (VehicleSerializer, VehicleManufacturerSerializer, VehicleRealLifeSerializer,
                          VehicleStorageLocationSerializer, VehicleWorkshopSerializer,
                          VehicleManufacturerRealLifeSerializer)


class VehicleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleWorkshopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VehicleWorkshop.objects.all()
    serializer_class = VehicleWorkshopSerializer


class VehicleStorageLocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VehicleStorageLocation.objects.all()
    serializer_class = VehicleStorageLocationSerializer


class VehicleManufacturerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VehicleManufacturer.objects.all()
    serializer_class = VehicleManufacturerSerializer


class VehicleManufacturerRealLifeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VehicleManufacturerRealLife.objects.all()
    serializer_class = VehicleManufacturerRealLifeSerializer


class VehicleRealLifeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VehicleRealLife.objects.all()
    serializer_class = VehicleRealLifeSerializer
