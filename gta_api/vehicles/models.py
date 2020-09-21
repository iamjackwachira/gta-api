from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models import BaseModelWithName
import vehicles.choices as choices


class VehicleRealLife(BaseModelWithName):
    """ Real life vehicle that is based on e.g Lamborghini """
    pass


class VehicleManufacturerRealLife(BaseModelWithName):
    """ Real life manufacturer for the vehicle e.g Jaguar """
    pass


class VehicleManufacturer(BaseModelWithName):
    """ Manufacturer for the vehicle e.g Ocelot """

    manufacturer_real_life = models.ForeignKey(
        VehicleManufacturerRealLife, related_name="vehicle_manufacturer", null=True, blank=True,
        on_delete=models.SET_NULL)


class VehicleStorageLocation(BaseModelWithName):
    """ Storage Locations for the vehicles e.g Appartment, Bunker """
    pass


class VehicleWorkshop(BaseModelWithName):
    """ Workshop for modifying vehicles. Can be normal garages or weaponized """
    pass


class Vehicle(BaseModelWithName):
    """ GTA ingame vehicle e.g Pegassi """

    vehicle_class = models.CharField(choices=choices.VEHICLE_CLASS_CHOICES, max_length=70)
    release_date = models.DateField(null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(1)])
    sellability = models.CharField(choices=choices.SELL_ABILITY_CHOICES, blank=True, null=True, max_length=50)
    resell_value_stolen = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True,
                                              validators=[MinValueValidator(1)])
    resell_value_purchased = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True,
                                                 validators=[MinValueValidator(1)])
    top_speed_mph = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1)])
    weight_in_kg = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1)])
    drive_train = models.CharField(choices=choices.DRIVE_TRAIN_CHOICES, max_length=3)
    num_gears = models.PositiveSmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
    speed_rating = models.DecimalField(max_digits=2, decimal_places=1,
                                       validators=[MinValueValidator(1), MaxValueValidator(5)])
    acceleration_rating = models.DecimalField(max_digits=2, decimal_places=1,
                                              validators=[MinValueValidator(1), MaxValueValidator(5)])
    handling_rating = models.DecimalField(max_digits=2, decimal_places=1,
                                          validators=[MinValueValidator(1), MaxValueValidator(5)])
    braking_rating = models.DecimalField(max_digits=2, decimal_places=1,
                                         validators=[MinValueValidator(1), MaxValueValidator(5)])
    game_edition_mode = models.CharField(choices=choices.GAME_EDITION_CHOICES, max_length=50, null=True, blank=True)
    special_features = models.CharField(choices=choices.VEHICLE_SPECIAL_FEATURES_CHOICES, max_length=20,
                                        null=True, blank=True)
    manufacturer = models.ForeignKey(VehicleManufacturer, on_delete=models.CASCADE, related_name="vehicles")
    vehicles_real_life = models.ManyToManyField(VehicleRealLife, related_name="vehicles")
    storage_locations = models.ManyToManyField(VehicleStorageLocation, related_name="vehicles")
    workshops = models.ManyToManyField(VehicleWorkshop, related_name="vehicles")

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        return self.name
