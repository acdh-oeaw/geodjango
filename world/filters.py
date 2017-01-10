import django_filters
from dal import autocomplete
from .models import WorldBorder, RegionBorder, AustriaBorders, Area

django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('iexact', 'Is equal to (case insensitive)'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than/before'),
    ('gt', 'Greater than/after'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('icontains', 'Contains (case insensitive)'),
    ('not_contains', 'Does not contain'),
]


class AustriaBordersListFilter(django_filters.FilterSet):

    class Meta:
        model = AustriaBorders


class WorldBorderListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains', label='Country',
        help_text=False, widget=autocomplete.ListSelect2(url='world:country_names')
    )

    class Meta:
        model = WorldBorder
        fields = ['name']


class RegionBorderListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains', label='Region Name',
        help_text=False, widget=autocomplete.ListSelect2(url='world:region_names')
    )
    admin = django_filters.CharFilter(
        lookup_expr='icontains', label='Country',
        help_text=False, widget=autocomplete.ListSelect2(url='world:country_names')
    )

    class Meta:
        model = RegionBorder
        fields = ['admin', 'name']


class AreaListFilter(django_filters.FilterSet):

    class Meta:
        model = Area