from django.apps import apps
from django.contrib import admin

from .models import Vehicle


for model in apps.get_app_config('vehicles').models.values():
    if model not in [Vehicle]:
        admin.site.register(model)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'vehicle_class', 'special_features',
                    'speed_rating', 'acceleration_rating', 'handling_rating',
                    'braking_rating')
    display = 'Vehicle'


admin.site.register(Vehicle, VehicleAdmin)
