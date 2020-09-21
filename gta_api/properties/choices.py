from model_utils import Choices
from django.utils.translation import ugettext_lazy as _


PROPERTY_TYPE_CHOICES = Choices(
    ('apartments', _('Apartments')),
    ('arcades', _('Arcades')),
    ('arena_workshop', _('Arena Workshops')),
    ('bunkers', _('Bunkers')),
    ('casino_penthouse', _('Casino Penhouse')),
    ('command_centers', _('Command Centers')),
    ('crate_warehouses', _('Crate Warehouses')),
    ('executive_office_garages', _('Executive Office Garages')),
    ('executive_offices', _('Executive Offices')),
    ('facilities', _('Facilities')),
    ('garages', _('Garages')),
    ('hangers', _('Hangers')),
    ('mc_businesses', _('MC Businesses')),
    ('mc_clubhouses', _('MC Clubhouses')),
    ('nightclubs', _('Nighclubs')),
    ('vehicle_warehouses', _('Vehicle Warehouses')),
    ('yachts', _('Yachts'))
)

PROPERTY_LOCATION_CHOICES = Choices(
    ('blaine_county', _('Blaine County')),
    ('downtown_los_santos', _('Downtown Los Santos')),
    ('east_los_santos', _('East Los Santos')),
    ('north_los_santos', _('North Los Santos')),
    ('south_los_santos', _('South Los Santos')),
    ('west_los_santos', _('West Los Santos')),
)

PROPERTY_STYLE_CHOICES = Choices(
    ('club_house_one_story', _('Clubhouse - One Story')),
    ('club_house_two_story', _('Clubhouse - Two Story')),
    ('high_end', _('High End')),
    ('high_end_custom', _('High End - Custom')),
    ('high_end_stilt_house', _('High-End - Stilt House')),
    ('high_end_updated', _('High-End - Updated')),
    ('low_end', _('Low-End')),
    ('medium', _('Medium')),
    ('warehouse_large', _('Warehouse - Large')),
    ('warehouse_medium', _('Warehouse - Medium')),
    ('warehouse_small', _('Warehouse - Small')),
)

PROPERTY_AVAILABLE_FROM_CHOICES = Choices(
    ('dynasty8_real_estate', _('Dynasty 8 Real Estate')),
    ('maze_bank_foreclosures', _('Maze Bank Foreclosures')),
    ('securoserv', _('SecuroServ')),
    ('the_open_road', _('The Open Road')),
    ('dynasty8_executive', _('Dynasty 8 Executive')),
    ('war_stock_cache_carry', _('Warstock Cache & Carry')),
    ('dock_tease', _('DockTease')),
    ('diamond_casino_resort', _('The Diamond Casino & Resort')),
    ('arena_war_tv', _('ArenaWar.tv')),
)
