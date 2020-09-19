import graphene
from graphene_django.types import DjangoObjectType

from .models import VehicleManufacturer, Vehicle


class VehicleType(DjangoObjectType):
    class Meta:
        model = Vehicle


class VehicleManufacturerType(DjangoObjectType):
    class Meta:
        model = VehicleManufacturer


class Query(graphene.ObjectType):
    vehicle = graphene.Field(VehicleType, id=graphene.Int())
    vehicles = graphene.List(VehicleType)
    manufacturer = graphene.Field(VehicleManufacturerType, id=graphene.Int())
    manufacturers = graphene.List(VehicleManufacturerType)

    def resolve_vehicle(self, info, **kwargs):
        id = kwargs.get('id')

        if not id:
            return Vehicle.objects.get(pk=id)

        return None

    def resolve_vehicles(self, info, **kwargs):
        return Vehicle.objects.all()

    def resolve_manufacturer(self, info, **kwargs):
        id = kwargs.get('id')

        if not id:
            return VehicleManufacturer.objects.get(pk=id)

        return None

    def resolve_manufacturers(self, info, **kwargs):
        return VehicleManufacturer.objects.all()


schema = graphene.Schema(query=Query)
