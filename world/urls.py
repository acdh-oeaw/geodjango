from django.conf.urls import url
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import WorldBorder

urlpatterns = [
    url(r'^$', TemplateView.as_view(
        template_name='world/regions.html'), name='regions'),
    url(
        r'^data.geojson$',
        GeoJSONLayerView.as_view(
            model=WorldBorder, properties=(
                'name')
        ), name='data')
]
