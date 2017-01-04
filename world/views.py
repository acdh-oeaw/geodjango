from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import RegionBorder, AustriaBorders, WorldBorder
from .forms import RegionBorderForm, AustriaBordersForm, WorldBorderForm


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
