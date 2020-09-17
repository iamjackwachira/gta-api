from django.db import models

from core.models import BaseModel, BaseModelWithName
import vehicles.choices as choices


class RealLifeVehicle(BaseModelWithName):
    pass


class VehicleManufacturer(BaseModelWithName):
    pass


class VehicleStorageLocation(BaseModelWithName):
    pass


class VehicleWorkshop(BaseModelWithName):
    pass


class Vehicle(BaseModel):
    name = models.CharField(max_length=70, unique=True)
    vehicle_class = models.CharField(
        choices.VEHICLE_CLASS_CHOICES, max_length=70)
    manufacturer = models.ForeignKey(
        VehicleManufacturer, on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=20, decimal_places=2)
    storage_location = models.ManyToManyField(VehicleStorageLocation)
    workshop = models.ManyToManyField(
        VehicleWorkshop, help_text="Workshop for modifying vehicle")
    sell_ability = models.CharField(choices=choices.SELL_ABILITY_CHOICES,
                                    blank=True, null=True, max_length=50,
                                    help_text="If the vehicle can be sold")
    stolen_sell_value = models.DecimalField(
        max_digits=20, decimal_places=2,
        help_text="Max sell value if stolen")
    resale_value = models.DecimalField(max_digits=20, decimal_places=2,
                                       help_text="Max sell value if purchased")
    top_speed = models.DecimalField(max_digits=5, decimal_places=2)
    based_on = models.ForeignKey(RealLifeVehicle, on_delete=models.SET_NULL,
                                 blank=True, null=True,
                                 help_text="Reallife vehicle it's based on")
    weight_in_kg = models.DecimalField(max_digits=5, decimal_places=2)
    drive_train = models.CharField(
        choices=choices.DRIVE_TRAIN_CHOICES, max_length=3)
    num_gears = models.PositiveSmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
    speed_rating = models.PositiveSmallIntegerField()
    acceleration_rating = models.PositiveSmallIntegerField()
    handling_rating = models.PositiveSmallIntegerField()
    braking_rating = models.PositiveSmallIntegerField()
    game_edition_mode = models.CharField(choices.GAME_EDITION_CHOICES,
                                         max_length=20, null=True, blank=True,
                                         help_text="Game Edition/Mode")
    special_features = models.CharField(
        choices=choices.VEHICLE_SPECIAL_FEATURES_CHOICES,
        max_length=20, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        return self.name
