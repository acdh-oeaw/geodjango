from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import RegionBorder


class RegionBorderSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        model = RegionBorder
        geo_field = "geom"
        fields = ['woe_label', 'woe_name', 'admin', 'iso_a2', 'gn_id', 'adm0_a3']
