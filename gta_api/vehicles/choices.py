from model_utils import Choices
from django.utils.translation import ugettext_lazy as _


DRIVE_TRAIN_CHOICES = Choices(
    ('fwd', _('FWD')),
    ('rwd', _('RWD')),
    ('awd', _('AWD')),
    ('4wd', _('4WD')),
)

SELL_ABILITY_CHOICES = Choices(
    ('purchased_high_end', 'Purchased High End'),
    ('purchased_or_stolen', 'Purchased Or Stolen'),
    ('only_stolen', 'Only Stolen'),
    ('not_sellable', 'Can not Be Sold'),
)

VEHICLE_CLASS_CHOICES = Choices(
    ('boats', _('Boats')),
    ('commercial', _('Commercial')),
    ('compacts', _('Compacts')),
    ('coupes', _('Coupes')),
    ('cycles', _('Cycles')),
    ('emergency', _('Emergency')),
    ('helicopters', _('Helicopters')),
    ('industrial', _('Industrial')),
    ('military', _('Military')),
    ('motorcycles', _('Motorcycles')),
    ('muscle', _('Muscle')),
    ('offroad', _('Off-road')),
    ('openwheel', _('Open-wheel')),
    ('planes', _('Planes')),
    ('sedan', _('Sedan')),
    ('service', _('Service')),
    ('sports', _('Sports')),
    ('sport_classic', _('Sport Classic')),
    ('super', _('Super')),
    ('suv', _('SUV')),
    ('utility', _('Utility')),
    ('vans', _('Vans')),
)

VEHICLE_SPECIAL_FEATURES_CHOICES = Choices(
    ('arena_contender', _('Arena Contender')),
    ('armed', _('Armed Vehicle')),
    ('armored', _('Armored Vehicle')),
    ('covertible_hard_top', _('Covertible Hard Top')),
    ('convertible_soft_top', _('Covertible Soft Top')),
    ('custom_vehicle', _('Custom Vehicle')),
    ('electric', _('Electric Vehicle')),
    ('float_water', _('Float on Water')),
    ('flying_ability', _('Flying Ability')),
    ('gang_vehicle', _('Gang Vehicle')),
    ('hover_ability', _('Hover Ability')),
    ('kers_boost', _('KERS Boost')),
    ('remote_controlled', _('Remote Controlled')),
    ('rocket_boost', _('Rocket Boost')),
    ('special_vehicle', _('Special Vehicle')),
    ('submersible', _('Submersible')),
    ('towing_hitch', _('Towing Hitch')),
    ('vehicle_workshop', _('Vehicle Workshop')),
    ('weaponized', _('Weaponized Vehicle')),
)
