from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import WorldBorder, RegionBorder, AustriaBorders, Area

admin.site.register(WorldBorder, LeafletGeoAdmin)
admin.site.register(RegionBorder, LeafletGeoAdmin)
admin.site.register(AustriaBorders, LeafletGeoAdmin)
admin.site.register(Area, LeafletGeoAdmin)
