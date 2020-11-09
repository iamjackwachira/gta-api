from django.contrib import admin

from .models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'property_type', 'state',
                    'purchase_price', 'vehicle_capacity')
    display = 'Property'


admin.site.register(Property, PropertyAdmin)
