from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import RegionBorder, WorldBorder, AustriaBorders


class RegionBorderForm(forms.ModelForm):
    class Meta:
        model = RegionBorder
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(RegionBorderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class WorldBorderForm(forms.ModelForm):
    class Meta:
        model = WorldBorder
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(WorldBorderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class AustriaBordersForm(forms.ModelForm):
    class Meta:
        model = AustriaBorders
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AustriaBordersForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)
