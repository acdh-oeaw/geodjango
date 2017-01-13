import django_tables2 as tables
from django_tables2.utils import A
from .models import WorldBorder, RegionBorder, AustriaBorders, Area, Source


class WorldBorderTable(tables.Table):
    name = tables.LinkColumn('world:world_detail', args=[A('pk')])

    class Meta:
        model = WorldBorder
        fields = ['name']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class RegionBorderTable(tables.Table):
    name = tables.LinkColumn('world:region_detail', args=[A('pk')])
    admin = tables.Column(verbose_name='Country')

    class Meta:
        model = RegionBorder
        fields = ['name']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class AustriaBordersTable(tables.Table):
    kg = tables.LinkColumn('world:austria_detail', args=[A('pk')], verbose_name='Gemeinde')
    pg = tables.Column(verbose_name='polit. Gemeinde')
    pb = tables.Column(verbose_name='polit. Bezirk')
    bl = tables.Column(verbose_name='Bundesland')

    class Meta:
        model = AustriaBorders
        fields = ['kg']
        attrs = {"class": "table table-hover table-striped table-condensed"}


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