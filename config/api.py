from django.urls import include, path


urlpatterns = [
     path('', include('vehicles.urls')),
     path('', include('weapons.urls')),
     path('', include('properties.urls')),
]
