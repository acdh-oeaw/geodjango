import django_tables2 as tables
from django_tables2.utils import A
from .models import Area, Source


class AreaTable(tables.Table):
    name = tables.LinkColumn('world:area_detail', args=[A('pk')])

    class Meta:
        model = Area
        fields = ['name']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class SourceTable(tables.Table):
    name = tables.LinkColumn('world:source_detail', args=[A('pk')])

    class Meta:
        model = Source
        fields = ['name']
        attrs = {"class": "table table-hover table-striped table-condensed"}