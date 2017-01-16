import django_filters
from dal import autocomplete
from .models import Area, Source

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


class AreaListFilter(django_filters.FilterSet):

    name = django_filters.ModelMultipleChoiceFilter(
        widget=autocomplete.Select2Multiple(url='world-ac:area-ac'),
        queryset=Area.objects.all(),
        #action='my_custom_filter',
        lookup_expr='icontains',
        label='Name',
        help_text=False,
    )

    class Meta:
        model = Area


class SourceListFilter(django_filters.FilterSet):

    class Meta:
        model = Source
        fields = ['name', 'original_url', 'downloaded']