from django import forms
from django.forms import ModelForm, ClearableFileInput, SelectDateWidget
from django.forms.fields import DateField
from .models import AgentCultural, Area, Entidad
from django.contrib.admin.widgets import AdminDateWidget

class XYZ_DateInput(forms.DateInput):
    input_type = "date"
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        # kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)
class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'
NIVEL_CHOICES = (
        ('INTERNACIONAL', 'INTERNACIONAL'),
        ('NACIONAL', 'NACIONAL'),
        ('DEPARTAMENTAL', 'DEPARTAMENTAL'),
        ('MUNICIPAL', 'MUNICIPAL'),

    )
class AgentCulturalForm(forms.ModelForm):
    DOY = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
           '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
           '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
           '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
           '2012', '2013', '2014', '2015')
    name = forms.CharField(label='1.1. NOMBRES',
                           widget=forms.Textarea(attrs={"placeholder": "1.1. NOMBRES",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))
    last_name = forms.CharField(label='1.2. APELLIDOS',
                           widget=forms.Textarea(attrs={"placeholder": "1.2. APELLIDOS",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))
    artistic_name = forms.CharField(label='1.3. NOMBRE ARTÍSTICO',
                           widget=forms.Textarea(attrs={"placeholder": "1.3. NOMBRE ARTÍSTICO",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))
    lugar_nacimiento = forms.CharField(label='1.6. LUGAR DE NACIMIENTO',
                                    widget=forms.Textarea(attrs={"placeholder": "1.6. LUGAR DE NACIMIENTO",
                                                                 "class": "new-class-name two",
                                                                 "id": "my-id-for-textarea",
                                                                 "rows": 1,
                                                                 'cols': 80
                                                                 }))
    identification = forms.CharField(label='1.8. NÚMERO DE DOCUMENTO',
                                       widget=forms.Textarea(attrs={"placeholder": "1.8. NÚMERO DE DOCUMENTO",
                                                                    "class": "new-class-name two",
                                                                    "id": "my-id-for-textarea",
                                                                    "rows": 1,
                                                                    'cols': 80
                                                                    }))
    lugar_expedicion = forms.CharField(label='1.9. LUGAR DE EXPEDICIÓN',
                                       widget=forms.Textarea(attrs={"placeholder": "1.9. LUGAR DE EXPEDICIÓN",
                                                                    "class": "new-class-name two",
                                                                    "id": "my-id-for-textarea",
                                                                    "rows": 1,
                                                                    'cols': 80
                                                                    }))
    tarjeta_profesional = forms.CharField(label='1.10. TARJETA PROFESIONAL',
                                       widget=forms.Textarea(attrs={"placeholder": "1.10. TARJETA PROFESIONAL",
                                                                    "class": "new-class-name two",
                                                                    "id": "my-id-for-textarea",
                                                                    "rows": 1,
                                                                    'cols': 80
                                                                    }))
    passport = forms.CharField(label='1.12. PASAPORTE',
                                          widget=forms.Textarea(attrs={"placeholder": "1.12. PASAPORTE",
                                                                       "class": "new-class-name two",
                                                                       "id": "my-id-for-textarea",
                                                                       "rows": 1,
                                                                       'cols': 80
                                                                       }))
    adress = forms.CharField(label='2.3. DIRECCIÓN DE VIVIENDA',
                                          widget=forms.Textarea(attrs={"placeholder": "2.3. DIRECCIÓN DE VIVIENDA",
                                                                       "class": "new-class-name two",
                                                                       "id": "my-id-for-textarea",
                                                                       "rows": 1,
                                                                       'cols': 80
                                                                       }))
    adress2 = forms.CharField(label='2.4. DIRECCIÓN DE CORRESPONDENCIA',
                             widget=forms.Textarea(attrs={"placeholder": "2.4. DIRECCIÓN DE CORRESPONDENCIA",
                                                          "class": "new-class-name two",
                                                          "id": "my-id-for-textarea",
                                                          "rows": 1,
                                                          'cols': 80
                                                          }))
    phone = forms.CharField(label='2.5. TELÉFONO',
                              widget=forms.Textarea(attrs={"placeholder": "2.5. TELÉFONO",
                                                           "class": "new-class-name two",
                                                           "id": "my-id-for-textarea",
                                                           "rows": 1,
                                                           'cols': 80
                                                           }))
    phone_movil = forms.CharField(label='2.6. CELULAR ',
                            widget=forms.Textarea(attrs={"placeholder": "2.6. CELULAR ",
                                                         "class": "new-class-name two",
                                                         "id": "my-id-for-textarea",
                                                         "rows": 1,
                                                         'cols': 80
                                                         }))
    email = forms.EmailField(label='Correo electrónico',
                             widget=forms.Textarea(attrs={"placeholder": "Correo Electrónico",
                                                          "class": "new-class-name two",
                                                          "id": "my-id-for-textarea",
                                                          "rows": 1,
                                                          'cols': 80
                                                          }))
    cual_practica = forms.CharField(label='3.4. ¿CUÁL?',
                                  widget=forms.Textarea(attrs={"placeholder": "3.4. ¿CUÁL?",
                                                               "class": "new-class-name two",
                                                               "id": "my-id-for-textarea",
                                                               "rows": 1,
                                                               'cols': 80
                                                               }))
    web = forms.CharField(label='2.8. PÁGINA WEB',
                          widget=forms.Textarea(attrs={"placeholder": "2.8. PÁGINA WEB ",
                                                       "class": "new-class-name two",
                                                       "id": "my-id-for-textarea",
                                                       "rows": 1,
                                                       'cols': 80
                                                       }))
    name_entity = forms.CharField(label='3.7. NOMBRE DE LA ORGANIZACIÓN ARTÍSTICA O CULTURAL',
                          widget=forms.Textarea(attrs={"placeholder": "3.7. NOMBRE DE LA ORGANIZACIÓN ARTÍSTICA O CULTURAL ",
                                                       "class": "new-class-name two",
                                                       "id": "my-id-for-textarea",
                                                       "rows": 1,
                                                       'cols': 80
                                                       }))
    titulo = forms.CharField(label='3.10.TÍTULO RECIBIDO',
                                  widget=forms.Textarea(
                                      attrs={"placeholder": "3.7. NOMBRE DE LA ORGANIZACIÓN ARTÍSTICA O CULTURAL ",
                                             "class": "new-class-name two",
                                             "id": "my-id-for-textarea",
                                             "rows": 1,
                                             'cols': 80
                                             }))
    entidad_educativa = forms.CharField(label='3.12. NOMBRE DE ENTIDAD EDUCATIVA',
                                  widget=forms.Textarea(
                                      attrs={"placeholder": "3.12. NOMBRE DE ENTIDAD EDUCATIVA ",
                                             "class": "new-class-name two",
                                             "id": "my-id-for-textarea",
                                             "rows": 1,
                                             'cols': 80
                                             }))
    reseña_trayectoria = forms.CharField(label='3.13. RESEÑA TRAYECTORIA ARTÍSTICA',
                                        widget=forms.Textarea(
                                            attrs={"placeholder": "3.13. RESEÑA TRAYECTORIA ARTÍSTICA",
                                                   "class": "new-class-name two",
                                                   "id": "my-id-for-textarea",
                                                   "rows": 1,
                                                   'cols': 80
                                                   }))
    cual_vinculacion = forms.CharField(label='4.3.1. ¿CUÁL TIPO DE VINCULACIÓN?:',
                                         widget=forms.Textarea(
                                             attrs={"placeholder": "4.3.1. ¿CUÁL TIPO DE VINCULACIÓN?:",
                                                    "class": "new-class-name two",
                                                    "id": "my-id-for-textarea",
                                                    "rows": 1,
                                                    'cols': 80
                                                    }))
    porcentaje = forms.CharField(label='4.6. ¿QUÉ PORCENTAJE DE SUS INGREOS PROVIENEN DE LA ACTIVIDAD ARTÍSTICA Y CULTURAL?',
                                       widget=forms.Textarea(
                                           attrs={"placeholder": "4.6. ¿QUÉ PORCENTAJE DE SUS INGREOS PROVIENEN DE LA ACTIVIDAD ARTÍSTICA Y CULTURAL?",
                                                  "class": "new-class-name two",
                                                  "id": "my-id-for-textarea",
                                                  "rows": 1,
                                                  'cols': 80
                                                  }))
    servicios = forms.CharField(
        label='Servicios que ofreces',
        widget=forms.Textarea(
            attrs={"placeholder": "Servicios que ofreces",
                   "class": "new-class-name two",
                   "id": "my-id-for-textarea",
                   "rows": 1,
                   'cols': 80
                   }))
    facebook = forms.CharField(
        label='Facebook',
        widget=forms.Textarea(
            attrs={"placeholder": "Facebook",
                   "class": "new-class-name two",
                   "id": "my-id-for-textarea",
                   "rows": 1,
                   'cols': 80
                   }))

    instagram = forms.CharField(
        label='Instagram',
        widget=forms.Textarea(
            attrs={"placeholder": "4.6. ¿QUÉ PORCENTAJE DE SUS INGREOS PROVIENEN DE LA ACTIVIDAD ARTÍSTICA Y CULTURAL?",
                   "class": "new-class-name two",
                   "id": "my-id-for-textarea",
                   "rows": 1,
                   'cols': 80
                   }))

    class Meta:
        model = AgentCultural
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'expedicion_tarjeta': XYZ_DateInput(format=["%Y-%m-%d"], ),
            'vencimiento_passport': XYZ_DateInput(format=["%Y-%m-%d"], ),
            'vinculacion_entidad': XYZ_DateInput(format=["%Y-%m-%d"], ),
            'ano_titulo': XYZ_DateInput(format=["%Y-%m-%d"], ),
            'archivo': CustomClearableFileInput
        }

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