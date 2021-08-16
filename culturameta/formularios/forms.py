from django import forms
from django.forms import ModelForm, ClearableFileInput
from .models import Pqrsd, EncuestaTransparencia, Torneo


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

class TorneoForm(forms.ModelForm):
    email = forms.EmailField(label='Correo electrónico',
                           widget=forms.Textarea(attrs={"placeholder": "Correo Electrónico",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))
    name = forms.CharField(label='Nombres y apellidos',
                    widget=forms.Textarea(attrs={"placeholder": "Nombres y Apellidos",
                                                  "class": "new-class-name two",
                                                  "id": "my-id-for-textarea",
                                                  "rows": 1,
                                                  'cols': 80
                                                  }))
    agrupacion = forms.CharField(label='Nombre de la agrupación (si aplica)',
                           widget=forms.Textarea(attrs={"placeholder": "Nombre de la agrupación (si aplica)",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))
    seudonimo = forms.CharField(label='Seudónimo (si aplica)',
                                 widget=forms.Textarea(attrs={"placeholder": "Seudónimo (si aplica)",
                                                              "class": "new-class-name two",
                                                              "id": "my-id-for-textarea",
                                                              "rows": 1,
                                                                'cols': 80
                                                              }))
    identification = forms.CharField(label='Número de identificación',
                                widget=forms.Textarea(attrs={"placeholder": "Número de identificación",
                                                             "class": "new-class-name two",
                                                             "id": "my-id-for-textarea",
                                                             "rows": 1,
                                                               'cols': 80
                                                             }))
    expedicion = forms.CharField(label='Lugar de Expedición',
                                     widget=forms.Textarea(attrs={"placeholder": "Lugar de Expedición",
                                                                  "class": "new-class-name two",
                                                                  "id": "my-id-for-textarea",
                                                                  "rows": 1,
                                                                  'cols': 80
                                                                  }))
    country = forms.CharField(label='País de residencia',
                                 widget=forms.Textarea(attrs={"placeholder": "País de residencia",
                                                              "class": "new-class-name two",
                                                              "id": "my-id-for-textarea",
                                                              "rows": 1,
                                                              'cols': 80
                                                              }))
    region = forms.CharField(label='Ciudad de residencia',
                                 widget=forms.Textarea(attrs={"placeholder": "Ciudad de residencia",
                                                              "class": "new-class-name two",
                                                              "id": "my-id-for-textarea",
                                                              "rows": 1,
                                                              'cols': 80
                                                              }))
    city = forms.CharField(label='Municipio',
                             widget=forms.Textarea(attrs={"placeholder": "Municipio",
                                                          "class": "new-class-name two",
                                                          "id": "my-id-for-textarea",
                                                          "rows": 1,
                                                          'cols': 80
                                                          }))
    adress = forms.CharField(label='Dirección residencia',
                           widget=forms.Textarea(attrs={"placeholder": "Dirección residencia",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))
    phone = forms.CharField(label='Teléfono fijo',
                           widget=forms.Textarea(attrs={"placeholder": "Teléfono fijo",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))
    phone_movil = forms.CharField(label='Teléfono celular',
                           widget=forms.Textarea(attrs={"placeholder": "Teléfono celular",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))

    obra1 = forms.CharField(label='Escriba el nombre de la obra N°1 y/o arreglo que presentará al concurso según lo solicitado en las bases: (No Aplica para las modalidades de, Pareja de Baile y Copleros).',
                           widget=forms.Textarea(attrs={"placeholder": "Escriba el nombre de la obra N°1 y/o arreglo que presentará al concurso según lo solicitado en las bases: (No Aplica para las modalidades de, Pareja de Baile y Copleros).",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 2,
                                                        'cols': 80
                                                        }))
    obra2 = forms.CharField(label='Escriba el nombre de la obra N°2 y/o arreglo que presentará al concurso según lo solicitado en las bases: (No Aplica para las modalidades de, Pareja de Baile y Copleros).',
                            widget=forms.Textarea(attrs={"placeholder": "Escriba el nombre de la obra N°2 y/o arreglo que presentará al concurso según lo solicitado en las bases: (No Aplica para las modalidades de, Pareja de Baile y Copleros).",
                                                         "class": "new-class-name two",
                                                         "id": "my-id-for-textarea",
                                                         "rows": 2,
                                                         'cols': 80
                                                         }))
    class Meta:
        model = Torneo
        fields = '__all__'
        widgets = {
            'archivo': CustomClearableFileInput,
            'archivo1': CustomClearableFileInput,
            'archivo2': CustomClearableFileInput,
            'archivo3': CustomClearableFileInput
        }
