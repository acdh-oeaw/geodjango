from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Area


class AreaSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        model = Area
        geo_field = "geom"
        fields = ['name', 'geonames_id', 'legacy_properties', 'start_date', 'end_date']
