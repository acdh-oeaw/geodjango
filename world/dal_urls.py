from django.conf.urls import url
from . import views
from . import dal_views


urlpatterns = [
	url(
        r'^country-names/$',
        dal_views.CountryNamesAC.as_view(),
        name='country_names',
    ),
    url(
        r'^region-names/$',
        dal_views.RegionNamesAC.as_view(),
        name='region_names',
    ),
    url(
        r'^area-names/$',
        dal_views.AreaNamesAC.as_view(),
        name='area_names',
    ),
    url(
        r'^area-ac/$', dal_views.AreaModelAC.as_view(), name='area-ac',
    ),
]