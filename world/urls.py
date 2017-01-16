from django.conf.urls import url
from . import views
from . import dal_views

urlpatterns = [
    url(r'^area/$', views.AreaFilterView.as_view(),
        name='area_list'),
    url(
        r'^area/(?P<pk>[0-9]+)$', views.AreaDetailView.as_view(),
        name='area_detail'),
    url(
        r'^area/create/$', views.AreaCreate.as_view(),
        name='area_create'),
    url(
        r'^area/update/(?P<pk>[0-9]+)$', views.AreaUpdate.as_view(),
        name='area_update'),
        url(r'^source/$', views.SourceFilterView.as_view(),
        name='source_list'),
    url(
        r'^source/(?P<pk>[0-9]+)$', views.SourceDetailView.as_view(),
        name='source_detail'),
    url(
        r'^source/create/$', views.SourceCreate.as_view(),
        name='source_create'),
    url(
        r'^source/update/(?P<pk>[0-9]+)$', views.SourceUpdate.as_view(),
        name='source_update'),
]
