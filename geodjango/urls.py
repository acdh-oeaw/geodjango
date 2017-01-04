"""geodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from world import api_views

router = routers.DefaultRouter()
router.register(r'regions', api_views.RegionBorderViewSet, base_name='region')
router.register(r'world', api_views.WorldBorderViewSet, base_name='world')
router.register(r'austria', api_views.AustriaBordersViewSet, base_name='austria')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('webpage.urls', namespace='webpage')),
    url(r'^datamodel/', include('django_spaghetti.urls', namespace='datamodel')),
    url(r'^world/', include('world.urls', namespace='world')),
]
