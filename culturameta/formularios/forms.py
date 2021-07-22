from django import forms
from django.forms import ModelForm, ClearableFileInput
from .models import Pqrsd, EncuestaTransparencia

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class PqrsdForm(forms.ModelForm):
    class Meta:
        model = Pqrsd
        fields = '__all__'
        exclude = ('user',)


class EncuestaTransparenciaForm(forms.ModelForm):
    class Meta:
        model = EncuestaTransparencia
        fields = '__all__'
        exclude = ('user',)