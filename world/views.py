from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django_tables2 import SingleTableView, RequestConfig
from .models import Area, Source
from .forms import AreaForm, SourceForm, GenericFilterFormHelper
from .filters import SourceListFilter, AreaListFilter
from .tables import AreaTable, SourceTable


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


class AreaFilterView(GenericListView):
    model = Area
    table_class = AreaTable
    template_name = 'world/area_filter.html'
    filter_class = AreaListFilter
    formhelper_class = GenericFilterFormHelper


class SourceFilterView(GenericListView):
    model = Source
    table_class = SourceTable
    template_name = 'world/source_filter.html'
    filter_class = SourceListFilter
    formhelper_class = GenericFilterFormHelper


class AreaDetailView(DetailView):

    model = Area
    template_name = 'world/area_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AreaDetailView, self).get_context_data(**kwargs)
        try:
            context["next_entry"] = Area.objects.filter(id__gt=int(self.kwargs['pk']))[0].pk
        except:
            context["next_entry"] = None
        prev = [x.id for x in Area.objects.filter(id__lt=int(self.kwargs['pk']))][-1]
        try:
            Area.objects.get(id=int(prev)-1)
            context["previous_entry"] = prev
        except:
            context["previous_entry"] = None
        print(context['previous_entry'])
        return context


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


class SourceDetailView(DetailView):

    model = Source
    template_name = 'world/source_detail.html'


class SourceListView(ListView):

    model = Source
    template_name = 'world/source_list.html'


class SourceCreate(CreateView):

    model = Source
    template_name = 'world/source_create.html'
    form_class = SourceForm


class SourceUpdate(UpdateView):

    model = Source
    form_class = SourceForm
    template_name = 'world/source_create.html'
