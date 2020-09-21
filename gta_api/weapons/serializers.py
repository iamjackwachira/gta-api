from rest_framework import serializers

from .models import Weapon, WeaponRealLife, WeaponManufacturer


class WeaponSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weapon
        fields = ('__all__')


class WeaponRealLifeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeaponRealLife
        fields = ('__all__')


class WeaponManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeaponManufacturer
        fields = ('__all__')
