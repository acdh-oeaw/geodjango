from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import RegionBorder
from .forms import RegionBorderForm


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
