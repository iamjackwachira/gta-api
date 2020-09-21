from model_utils import Choices
from django.utils.translation import ugettext_lazy as _


WEAPON_TYPE_CHOICES = Choices(
    ('handguns', _('Handguns')),
    ('shotguns', _('Shotguns')),
    ('machine_guns', _('Machine Guns')),
    ('assault_rifles', _('Assault Rifles')),
    ('heavy_weapons', _('Heavy Weapons')),
    ('thrown_weapons', _('Thrown Weapons')),
    ('melee', _('Melee')),
    ('mounted_weapons', _('Mounted Weapons')),
)

WEAPON_LOCATIONS = Choices(
    ('ammu_nation', _('Ammu Nation')),
    ('weapon_workshop', _('Weapon Workshop')),
    ('stolen_found', _('Is Stolen/Found')),
    ('bonus_reward', _('Bonus Reward')),
    ('unacquirable', _('Cannot be acquired')),
    ('merry_weather_security_services', _('Merry Weather Security Services')),
)

WEAPON_MODIFICATIONS = Choices(
    ('can_be_modified', _('Can be modified')),
    ('cannot_be_modified', _('Cannot be modified')),
)
