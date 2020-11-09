from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models import BaseModelWithName
from core.choices import GAME_EDITION_CHOICES
import weapons.choices as choices


class WeaponRealLife(BaseModelWithName):
    """ Real life equivalent weapon """
    pass


class WeaponManufacturer(BaseModelWithName):
    """ Weapon manufacturer """
    pass


class Weapon(BaseModelWithName):
    """ In Game weapon e.g Carbine Rifle """

    ammo_capacity = models.PositiveSmallIntegerField()
    extended_ammo = models.PositiveSmallIntegerField()
    weapon_type = models.CharField(choices=choices.WEAPON_TYPE_CHOICES, max_length=70)
    available_from = models.CharField(choices=choices.WEAPON_AVAILABLE_FROM_CHOICES,
                                      blank=True, null=True, max_length=50)
    release_date = models.DateField(null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(1)])
    modifications = models.CharField(choices=choices.WEAPON_MODIFICATIONS_CHOICES, blank=True, null=True, max_length=50)
    weapon_real_life = models.ForeignKey(WeaponRealLife, null=True, blank=True,
                                         on_delete=models.SET_NULL, related_name="weapons")
    game_edition_mode = models.CharField(choices=GAME_EDITION_CHOICES, max_length=50, null=True, blank=True)
    manufacturer = models.ForeignKey(WeaponManufacturer, on_delete=models.CASCADE, related_name="weapons")
    damage_rating = models.DecimalField(max_digits=2, decimal_places=1,
                                        validators=[MinValueValidator(1), MaxValueValidator(5)])
    firing_rating = models.DecimalField(max_digits=2, decimal_places=1,
                                        validators=[MinValueValidator(1), MaxValueValidator(5)])
    accuracy_rating = models.DecimalField(max_digits=2, decimal_places=1,
                                          validators=[MinValueValidator(1), MaxValueValidator(5)])
    range_rating = models.DecimalField(max_digits=2, decimal_places=1,
                                       validators=[MinValueValidator(1), MaxValueValidator(5)])
    clip_size_rating = models.DecimalField(max_digits=2, decimal_places=1,
                                           validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Weapon'
        verbose_name_plural = 'Weapons'

    def __str__(self):
        return self.name
