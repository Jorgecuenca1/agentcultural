from django import forms
from django.forms import ModelForm, ClearableFileInput, SelectDateWidget, CheckboxSelectMultiple
from django.forms.fields import DateField
from .models import AgentCultural, Area, Entidad, AGENTEAREA_CHOICES
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
            attrs={"placeholder": "Instagram",
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

            'archivo': CustomClearableFileInput
        }

        date = forms.DateInput()

    def __init__(self, *args, **kwargs):
        super(AgentCulturalForm, self).__init__(*args, **kwargs)
        self.fields['artistic_name'].required = False
        self.fields['gender'].required = False
        self.fields['birthday'].required = False
        self.fields['lugar_nacimiento'].required = False
        self.fields['type_document'].required = False
        self.fields['lugar_expedicion'].required = False
        self.fields['tarjeta_profesional'].required = False
        self.fields['expedicion_tarjeta'].required = False
        self.fields['passport'].required = False
        self.fields['expedicion_passport'].required = False
        self.fields['vencimiento_passport'].required = False
        self.fields['posee_discapacidad'].required = False
        self.fields['disability'].required = False
        self.fields['posee_etnico'].required = False
        self.fields['etnico'].required = False
        self.fields['esvictima'].required = False
        self.fields['victima'].required = False
        self.fields['city'].required = False
        self.fields['zona'].required = False
        self.fields['adress'].required = False
        self.fields['adress2'].required = False
        self.fields['phone'].required = False
        self.fields['phone_movil'].required = False
        self.fields['email'].required = False
        self.fields['web'].required = False
        self.fields['desarrollo_practica'].required = False
        self.fields['forma_practica'].required = False
        self.fields['area2'].required = False
        self.fields['practica'].required = False
        self.fields['cual_practica'].required = False
        self.fields['pertenece_entidad'].required = False
        self.fields['vinculacion_entidad'].required = False
        self.fields['name_entity'].required = False
        self.fields['tipo_formacion'].required = False
        self.fields['nivel_educacion'].required = False
        self.fields['titulo'].required = False
        self.fields['ano_titulo'].required = False
        self.fields['entidad_educativa'].required = False
        self.fields['reseña_trayectoria'].required = False
        self.fields['tipo_vivienda'].required = False
        self.fields['housing_stratum'].required = False
        self.fields['tipo_vinculacion'].required = False
        self.fields['cual_vinculacion'].required = False
        self.fields['otra_actividad'].required = False
        self.fields['fuente_ingreso'].required = False
        self.fields['regimen_salud'].required = False
        self.fields['health_regimen'].required = False
        self.fields['regimen_pension'].required = False
        self.fields['pension_regimen'].required = False
        self.fields['regimen_arl'].required = False
        self.fields['vigia_patrimonio'].required = False
        self.fields['portador_manifestacion'].required = False
        self.fields['manifestation'].required = False
        self.fields['servicios'].required = False
        self.fields['facebook'].required = False
        self.fields['instagram'].required = False
        self.fields['sisben'].required = False
        self.fields['beps'].required = False
        self.fields['terminosycondiciones'].required = False

class EntidadForm(forms.ModelForm):
    class Meta:
        model = Entidad
        fields = '__all__'
        exclude = ('user',)