from django.apps import apps
from django.contrib import admin

from .models import Weapon


for model in apps.get_app_config('weapons').models.values():
    if model not in [Weapon]:
        admin.site.register(model)


class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'ammo_capacity', 'available_from',
                    'purchase_price', 'damage_rating', 'accuracy_rating',
                    'range_rating')
    display = 'Weapon'


admin.site.register(Weapon, WeaponAdmin)
