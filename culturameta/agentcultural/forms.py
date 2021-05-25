from django import forms
from django.forms import ModelForm, ClearableFileInput
from .models import AgentCultural, Area, Entidad

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class AgentCulturalForm(forms.ModelForm):
    class Meta:
        model = AgentCultural
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'archivo': CustomClearableFileInput
        }
        name = forms.CharField(label='Nombre:',max_length=15,
                                    widget=forms.TextInput())
        date = forms.DateInput()
        areas = forms.ModelMultipleChoiceField(
        queryset=Area.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class EntidadForm(forms.ModelForm):
    class Meta:
        model = Entidad
        fields = '__all__'
        exclude = ('user',)