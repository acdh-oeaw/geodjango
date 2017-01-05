from dal import autocomplete
from .models import RegionBorder


class CountryNamesAC(autocomplete.Select2ListView):

    def get_list(self):
        regions = RegionBorder.objects.filter(admin__icontains=self.q)
        country_names = set([x.admin for x in regions])
        return country_names
