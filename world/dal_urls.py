from django.conf.urls import url
from . import views
from . import dal_views


urlpatterns = [
    url(
        r'^area-names/$', dal_views.AreaNamesAC.as_view(), name='area_names',
    ),
    url(
        r'^area-ac/$', dal_views.AreaModelAC.as_view(), name='area-ac',
    ),
]