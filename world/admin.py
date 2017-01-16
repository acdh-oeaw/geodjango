from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Area, Source

admin.site.register(Area, LeafletGeoAdmin)
admin.site.register(Source)