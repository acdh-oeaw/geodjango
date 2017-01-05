from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^region/$', views.RegionBorderFilterView.as_view(),
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
    url(
        r'^world/$', views.WorldBorderFilterView.as_view(), name='world_list'),
    url(
        r'^world/(?P<pk>[0-9]+)$', views.WorldBorderDetailView.as_view(),
        name='world_detail'),
    url(
        r'^world/create/$', views.WorldBorderCreate.as_view(), name='world_create'),
    url(
        r'^world/update/(?P<pk>[0-9]+)$', views.WorldBorderUpdate.as_view(),
        name='world_update'),
    url(r'^austria/$', views.AustriaBordersFilterView.as_view(),
        name='austria_list'),
    url(
        r'^austria/(?P<pk>[0-9]+)$', views.AustriaBordersDetailView.as_view(),
        name='austria_detail'),
    url(
        r'^austria/create/$', views.AustriaBordersCreate.as_view(),
        name='austria_create'),
    url(
        r'^austria/update/(?P<pk>[0-9]+)$', views.AustriaBordersUpdate.as_view(),
        name='austria_update'),
]
