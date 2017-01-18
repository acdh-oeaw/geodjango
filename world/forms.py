from django import forms
from leaflet.forms.widgets import LeafletWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Area, Source


class GenericFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.add_input(Submit('Filter', 'Filter'))


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


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = "__all__"
        widgets = {'geom': LeafletWidget(attrs={
            'settings_overrides': {
                'DEFAULT_CENTER': (6.0, 45.0),
            }
        })}

    def __init__(self, *args, **kwargs):
        super(SourceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-1'
        self.helper.field_class = 'col-md-11'
        self.helper.add_input(Submit('submit', 'save'),)
