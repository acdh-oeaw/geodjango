from django.http import HttpResponse
from django.core.serializers import serialize
from .models import RegionBorder


def region_view(request):
    regions_as_geojson = serialize('geojson', RegionBorder.objects.filter(id__in=[290]))
    return HttpResponse(regions_as_geojson, content_type='json')
