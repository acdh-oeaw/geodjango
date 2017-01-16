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
        object_ids = [x.id for x in Area.objects.all()]
        self_id = int(self.kwargs['pk'])
        if self_id == object_ids[-1]:
            next_entry = None
        else:
            next_entry = object_ids[object_ids.index(self_id) + 1]
        context["next_entry"] = next_entry

        if object_ids.index(self_id) == 0:
            previous_entry = None
        else:
            previous_entry = object_ids[object_ids.index(self_id) - 1]
        context["previous_entry"] = previous_entry
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

