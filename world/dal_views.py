from dal import autocomplete
from .models import Area


class AreaNamesAC(autocomplete.Select2ListView):

    def get_list(self):
        regions = Area.objects.filter(name__icontains=self.q)
        names = set([x.name for x in regions])
        return names


class AreaModelAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Area.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
            
        return qs