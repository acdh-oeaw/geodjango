from django.conf.urls import url
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import WorldBorder
from . import views, data_views

urlpatterns = [
    url(r'^region/$', views.RegionBorderListView.as_view(),
        name='region_list'),
    url(
        r'^region/(?P<pk>[0-9]+)$', views.RegionBorderDetailView.as_view(),
        name='region_detail'),
    url(
        r'^region/create/$', views.RegionBorderCreate.as_view(),
        name='region_create'),
    url(
        r'^region/update/(?P<pk>[0-9]+)$', views.RegionBorderUpdate.as_view(),
        name='region_update'),

    url(r'^regions.data/', data_views.region_view, name='region_view'),
    url(r'^$', TemplateView.as_view(
        template_name='world/regions.html'), name='regions'),
    url(
        r'^data.geojson$', GeoJSONLayerView.as_view(
            model=WorldBorder, properties=('name')), name='data')
]
