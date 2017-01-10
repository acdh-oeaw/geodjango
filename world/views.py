from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django_tables2 import SingleTableView, RequestConfig
from .models import RegionBorder, AustriaBorders, WorldBorder, Area
from .forms import RegionBorderForm, AustriaBordersForm, WorldBorderForm
from .filters import *
from .forms import *
from .tables import *


class GenericListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'
    paginate_by = 25

    def get_queryset(self, **kwargs):
        qs = super(GenericListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by}).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


class RegionBorderFilterView(GenericListView):
    model = RegionBorder
    table_class = RegionBorderTable
    template_name = 'world/region_filter.html'
    filter_class = RegionBorderListFilter
    formhelper_class = GenericFilterFormHelper


class AustriaBordersFilterView(GenericListView):
    model = AustriaBorders
    table_class = AustriaBordersTable
    template_name = 'world/austria_filter.html'
    filter_class = AustriaBordersListFilter
    formhelper_class = GenericFilterFormHelper


class WorldBorderFilterView(GenericListView):
    model = WorldBorder
    table_class = WorldBorderTable
    template_name = 'world/world_filter.html'
    filter_class = WorldBorderListFilter
    formhelper_class = GenericFilterFormHelper


class AreaFilterView(GenericListView):
    model = Area
    table_class = AreaTable
    template_name = 'world/area_filter.html'
    filter_class = AreaListFilter
    formhelper_class = GenericFilterFormHelper


class RegionBorderDetailView(DetailView):

    model = RegionBorder
    template_name = 'world/regionborder_detail.html'


class RegionBorderListView(ListView):

    model = RegionBorder
    template_name = 'world/regionborder_list.html'


class RegionBorderCreate(CreateView):

    model = RegionBorder
    template_name = 'world/regionborder_create.html'
    form_class = RegionBorderForm


class RegionBorderUpdate(UpdateView):

    model = RegionBorder
    form_class = RegionBorderForm
    template_name = 'world/regionborder_create.html'


class WorldBorderDetailView(DetailView):

    model = WorldBorder
    template_name = 'world/worldborder_detail.html'

    def get_context_data(self, **kwargs):
        context = super(WorldBorderDetailView, self).get_context_data(**kwargs)
        context["regions"] = RegionBorder.objects.filter(country=self.kwargs.get('pk'))
        return context


class WorldBorderListView(ListView):

    model = WorldBorder
    template_name = 'world/worldborder_list.html'


class WorldBorderCreate(CreateView):

    model = WorldBorder
    template_name = 'world/worldborder_create.html'
    form_class = WorldBorderForm


class WorldBorderUpdate(UpdateView):

    model = WorldBorder
    form_class = WorldBorderForm
    template_name = 'world/worldborder_create.html'


class AustriaBordersDetailView(DetailView):

    model = AustriaBorders
    template_name = 'world/austrianborder_detail.html'


class AustriaBordersListView(ListView):

    model = AustriaBorders
    template_name = 'world/austrianborder_list.html'


class AustriaBordersCreate(CreateView):

    model = AustriaBorders
    template_name = 'world/austrianborder_create.html'
    form_class = AustriaBordersForm


class AustriaBordersUpdate(UpdateView):

    model = AustriaBorders
    form_class = AustriaBordersForm
    template_name = 'world/austrianborder_create.html'


class AreaDetailView(DetailView):

    model = Area
    template_name = 'world/area_detail.html'


class AreaListView(ListView):

    model = Area
    template_name = 'world/area_list.html'


class AreaCreate(CreateView):

    model = Area
    template_name = 'world/area_create.html'
    form_class = AreaForm


class AreaUpdate(UpdateView):

    model = Area
    form_class = AreaForm
    template_name = 'world/area_create.html'

