from model_utils import Choices
from django.utils.translation import ugettext_lazy as _


GAME_EDITION_CHOICES = Choices(
    ('gta_online', _('GTA Online')),
    ('story_mode', _('Story Mode')),
    ('returning_player_bonus', _('Returning Player Bonus')),
    ('criminal_enterprise_starter_pack',
        _('Criminal Enterprise Starter Pack')),
    ('mission_only', _('Mission Only')),
    ('collectors_edition', _('Collectors Edition')),
    ('all_editions', _('All Editions')),
)
