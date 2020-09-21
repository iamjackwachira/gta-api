from rest_framework import serializers

from .models import (Vehicle, VehicleManufacturer, VehicleStorageLocation,
                     VehicleWorkshop, VehicleRealLife, VehicleManufacturerRealLife)


class VehicleWorkshopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleWorkshop
        fields = ('__all__')


class VehicleStorageLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleStorageLocation
        fields = ('__all__')


class VehicleManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleManufacturer
        fields = ('__all__')


class VehicleManufacturerRealLifeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleManufacturerRealLife
        fields = ('__all__')


class VehicleRealLifeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleRealLife
        fields = ('__all__')


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('__all__')
