from django.db import models
from django.core.validators import MinValueValidator

from core.models import BaseModelWithName
from core.choices import GAME_EDITION_CHOICES
import properties.choices as choices


class Property(BaseModelWithName):
    """ In Game weapon e.g Carbine Rifle """

    property_type = models.CharField(choices=choices.PROPERTY_TYPE_CHOICES, max_length=70)
    state = models.CharField(choices=choices.PROPERTY_LOCATION_CHOICES, max_length=70)
    available_from = models.CharField(choices=choices.PROPERTY_AVAILABLE_FROM_CHOICES,
                                      blank=True, null=True, max_length=50)
    purchase_price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(1)])
    vehicle_capacity = models.PositiveSmallIntegerField()
    release_date = models.DateField(null=True, blank=True)
    game_edition_mode = models.CharField(choices=GAME_EDITION_CHOICES, max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.name
