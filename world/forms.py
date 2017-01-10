from django import forms
from leaflet.forms.widgets import LeafletWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import RegionBorder, WorldBorder, AustriaBorders, Area


class GenericFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.add_input(Submit('Filter', 'Filter'))


class RegionBorderForm(forms.ModelForm):
    class Meta:
        model = RegionBorder
        fields = "__all__"
        widgets = {'geom': LeafletWidget(attrs={
            'settings_overrides': {
                'DEFAULT_CENTER': (6.0, 45.0),
            }
        })}

    def __init__(self, *args, **kwargs):
        super(RegionBorderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-1'
        self.helper.field_class = 'col-md-11'
        self.helper.add_input(Submit('submit', 'save'),)


class WorldBorderForm(forms.ModelForm):
    class Meta:
        model = WorldBorder
        fields = "__all__"
        widgets = {'geom': LeafletWidget(attrs={
            'settings_overrides': {
                'DEFAULT_CENTER': (6.0, 45.0),
            }
        })}

    def __init__(self, *args, **kwargs):
        super(WorldBorderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-1'
        self.helper.field_class = 'col-md-11'
        self.helper.add_input(Submit('submit', 'save'),)


class AustriaBordersForm(forms.ModelForm):
    class Meta:
        model = AustriaBorders
        fields = "__all__"
        widgets = {'geom': LeafletWidget(attrs={
            'settings_overrides': {
                'DEFAULT_CENTER': (6.0, 45.0),
            }
        })}

    def __init__(self, *args, **kwargs):
        super(AustriaBordersForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-1'
        self.helper.field_class = 'col-md-11'
        self.helper.add_input(Submit('submit', 'save'),)


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = "__all__"
        widgets = {'geom': LeafletWidget(attrs={
            'settings_overrides': {
                'DEFAULT_CENTER': (6.0, 45.0),
            }
        })}

    def __init__(self, *args, **kwargs):
        super(AreaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-1'
        self.helper.field_class = 'col-md-11'
        self.helper.add_input(Submit('submit', 'save'),)