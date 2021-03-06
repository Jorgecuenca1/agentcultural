from django import forms
from django.forms import ModelForm, ClearableFileInput
from .models import Pqrsd, EncuestaTransparencia, Torneo, Presupuesto, Perfil, Filarmonica
from .models import Tiposolicitud, Nivel, Meta

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class PqrsdForm(forms.ModelForm):
    name = forms.CharField(label='Nombre del remitente',
                           widget=forms.Textarea(attrs={"placeholder": "Nombre del remitente",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))
    last_name = forms.CharField(label='Apellidos del remitente',
                           widget=forms.Textarea(attrs={"placeholder": "Apellidos del remitente",
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
    identification = forms.CharField(label='Identificaci??n',
                                widget=forms.Textarea(attrs={"placeholder": "Identificaci??n",
                                                             "class": "new-class-name two",
                                                             "id": "my-id-for-textarea",
                                                             "rows": 1,
                                                             'cols': 80
                                                             }))
    email = forms.EmailField(label='Correo electr??nico',
                             widget=forms.Textarea(attrs={"placeholder": "Correo Electr??nico",
                                                          "class": "new-class-name two",
                                                          "id": "my-id-for-textarea",
                                                          "rows": 1,
                                                          'cols': 80
                                                          }))
    phone = forms.CharField(label='Celular',
                                     widget=forms.Textarea(attrs={"placeholder": "Celular",
                                                                  "class": "new-class-name two",
                                                                  "id": "my-id-for-textarea",
                                                                  "rows": 1,
                                                                  'cols': 80
                                                                  }))
    asunto = forms.CharField(label='Asunto',
                            widget=forms.Textarea(attrs={"placeholder": "Asunto",
                                                         "class": "new-class-name two",
                                                         "id": "my-id-for-textarea",
                                                         "rows": 1,
                                                         'cols': 80
                                                         }))
    solicitud = forms.CharField(label='Solicitud',
                             widget=forms.Textarea(attrs={"placeholder": "Solicitud",
                                                          "class": "new-class-name two",
                                                          "id": "my-id-for-textarea",
                                                          "rows": 4,
                                                          'cols': 80
                                                          }))

    class Meta:
        model = Pqrsd
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'archivo': CustomClearableFileInput
        }


class EncuestaTransparenciaForm(forms.ModelForm):
    sugerencia= forms.CharField(label='Sugerencia',
                                 widget=forms.Textarea(attrs={"placeholder": "Sugerencia",
                                                              "class": "new-class-name two",
                                                              "id": "my-id-for-textarea",
                                                              "rows": 4,
                                                              'cols': 80
                                                              }))

    class Meta:
        model = EncuestaTransparencia
        fields = '__all__'
        exclude = ('user',)

class TorneoForm(forms.ModelForm):
    email = forms.EmailField(label='Correo electr??nico',
                           widget=forms.Textarea(attrs={"placeholder": "Correo Electr??nico",
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
    agrupacion = forms.CharField(label='Nombre de la agrupaci??n (si aplica)',
                           widget=forms.Textarea(attrs={"placeholder": "Nombre de la agrupaci??n (si aplica)",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))
    seudonimo = forms.CharField(label='Seud??nimo (si aplica)',
                                 widget=forms.Textarea(attrs={"placeholder": "Seud??nimo (si aplica)",
                                                              "class": "new-class-name two",
                                                              "id": "my-id-for-textarea",
                                                              "rows": 1,
                                                                'cols': 80
                                                              }))
    identification = forms.CharField(label='N??mero de identificaci??n',
                                widget=forms.Textarea(attrs={"placeholder": "N??mero de identificaci??n",
                                                             "class": "new-class-name two",
                                                             "id": "my-id-for-textarea",
                                                             "rows": 1,
                                                               'cols': 80
                                                             }))
    expedicion = forms.CharField(label='Lugar de Expedici??n',
                                     widget=forms.Textarea(attrs={"placeholder": "Lugar de Expedici??n",
                                                                  "class": "new-class-name two",
                                                                  "id": "my-id-for-textarea",
                                                                  "rows": 1,
                                                                  'cols': 80
                                                                  }))
    country = forms.CharField(label='Pa??s de residencia',
                                 widget=forms.Textarea(attrs={"placeholder": "Pa??s de residencia",
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
    adress = forms.CharField(label='Direcci??n residencia',
                           widget=forms.Textarea(attrs={"placeholder": "Direcci??n residencia",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))
    phone = forms.CharField(label='Tel??fono fijo',
                           widget=forms.Textarea(attrs={"placeholder": "Tel??fono fijo",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))
    phone_movil = forms.CharField(label='Tel??fono celular',
                           widget=forms.Textarea(attrs={"placeholder": "Tel??fono celular",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))

    obra1 = forms.CharField(label='Escriba el nombre de la obra N??1 y/o arreglo que presentar?? al concurso seg??n lo solicitado en las bases: (No Aplica para las modalidades de, Pareja de Baile y Copleros).',
                           widget=forms.Textarea(attrs={"placeholder": "Escriba el nombre de la obra N??1 y/o arreglo que presentar?? al concurso seg??n lo solicitado en las bases: (No Aplica para las modalidades de, Pareja de Baile y Copleros).",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 2,
                                                        'cols': 80
                                                        }))
    obra2 = forms.CharField(label='Escriba el nombre de la obra N??2 y/o arreglo que presentar?? al concurso seg??n lo solicitado en las bases: (No Aplica para las modalidades de, Pareja de Baile y Copleros).',
                            widget=forms.Textarea(attrs={"placeholder": "Escriba el nombre de la obra N??2 y/o arreglo que presentar?? al concurso seg??n lo solicitado en las bases: (No Aplica para las modalidades de, Pareja de Baile y Copleros).",
                                                         "class": "new-class-name two",
                                                         "id": "my-id-for-textarea",
                                                         "rows": 2,
                                                         'cols': 80
                                                         }))
    link = forms.CharField(label='Adjuntar el link del archivo de wetranfer donde envia el audio formato punto wav, mp3 etc... y v??deo y/o videos (m??nimo una c??mara m??ximo tres c??maras grabando simult??neamente) FHD, 1080p o superior de la propuesta seg??n sea la modalidad seleccionada: *',
                                  widget=forms.Textarea(attrs={"placeholder": "Adjuntar el link del archivo de wetranfer donde envia el audio formato punto wav, mp3 etc... y v??deo y/o videos (m??nimo una c??mara m??ximo tres c??maras grabando simult??neamente) FHD, 1080p o superior de la propuesta seg??n sea la modalidad seleccionada: *",
                                                               "class": "new-class-name two",
                                                               "id": "my-id-for-textarea",
                                                               "rows": 1,
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

class PresupuestoForm(forms.ModelForm):
    name = forms.CharField(label='Nombres y Apellidos*',
                           widget=forms.Textarea(attrs={"placeholder": "Nombres y Apellidos : *",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))
    email = forms.EmailField(label='Correo electr??nico*',
                    widget=forms.Textarea(attrs={"placeholder": "Correo *",
                                                  "class": "new-class-name two",
                                                  "id": "my-id-for-textarea",
                                                  "rows": 1,
                                                  'cols': 80
                                                  }))
    identification = forms.CharField(label='N??mero de identificaci??n *',
                           widget=forms.Textarea(attrs={"placeholder": "N??mero de identificaci??n : *",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))
    phone = forms.CharField(label='Tel??fono fijo o celular',
                           widget=forms.Textarea(attrs={"placeholder": "Tel??fono fijo o celular:",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))

    perfil = forms.ModelChoiceField(label='Tipo de Actor*',queryset=Perfil.objects.all())

    entity = forms.CharField(label='Nombre de la entidad *',
                                     widget=forms.Textarea(attrs={"placeholder": "Si actu?? en representaci??n, indique Nombre de Entidad, instancia,instituci??n,organismo,entre otros",
                                                                  "class": "new-class-name two",
                                                                  "id": "my-id-for-textarea",
                                                                  "rows": 2,
                                                                  'cols': 80
                                                                  }))
    iniciativa = forms.CharField(label='Nombre de la Iniciativa',
                                 widget=forms.Textarea(attrs={"placeholder": "Nombre de la Iniciativa",
                                                              "class": "new-class-name two",
                                                              "id": "my-id-for-textarea",
                                                              "rows": 4,
                                                              'cols': 80
                                                              }))
    planteamiento = forms.CharField(label='2. Planteamiento del Problema',
                                 widget=forms.Textarea(attrs={"placeholder": "2. Planteamiento del Problema:",
                                                              "class": "new-class-name two",
                                                              "id": "my-id-for-textarea",
                                                              "rows": 4,
                                                              'cols': 80
                                                              }))
    objetivo_general = forms.CharField(label='3.1. Objetivo General',
                             widget=forms.Textarea(attrs={"placeholder": "3.1. Objetivo General",
                                                          "class": "new-class-name two",
                                                          "id": "my-id-for-textarea",
                                                          "rows": 4,
                                                          'cols': 80
                                                          }))
    objetivo_especifico = forms.CharField(label='3.2 Objetivos Espec??ficos:',
                           widget=forms.Textarea(attrs={"placeholder": "3.2 Objetivos Espec??ficos:",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 4,
                                                        'cols': 80
                                                        }))
    descripcion = forms.CharField(label='4. Breve Descripci??n de la iniciativa:',
                           widget=forms.Textarea(attrs={"placeholder": "4. Breve Descripci??n de la iniciativa:",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 4,
                                                        'cols': 80
                                                        }))
    beneficiarios = forms.CharField(label='5. Beneficiarios:',
                           widget=forms.Textarea(attrs={"placeholder": "5. Beneficiarios:",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))

    poblacion = forms.CharField(label='5.1. Cantidad Poblacion objetivo:',
                           widget=forms.Textarea(attrs={"placeholder": "5.1. Cantidad Poblacion objetivo:",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 2,
                                                        'cols': 80
                                                        }))
    poblacion_objetivo = forms.CharField(label='5.2. Caracterizaci??n Poblaci??n objetivo (Urbana, rural, con enfoque diferencial, ciclo vida:',
                            widget=forms.Textarea(attrs={"placeholder": "5.2. Caracterizaci??n Poblaci??n objetivo (Urbana, rural, con enfoque diferencial, ciclo vida:",
                                                         "class": "new-class-name two",
                                                         "id": "my-id-for-textarea",
                                                         "rows": 2,
                                                         'cols': 80
                                                         }))
    valor_estimado = forms.CharField(label='6. Valor estimado de la Iniciativa',
                                  widget=forms.Textarea(attrs={"placeholder": "6. Valor estimado de la Iniciativa",
                                                               "class": "new-class-name two",
                                                               "id": "my-id-for-textarea",
                                                                   "rows": 1,
                                                               'cols': 80
                                                                }))
    descripcion_presupuesto = forms.CharField(label='6.1. Breve descripci??n del presupuesto estimado por actividades:',
                                       widget=forms.Textarea(attrs={"placeholder": "6.1. Breve descripci??n del presupuesto estimado por actividades:",
                                                                    "class": "new-class-name two",
                                                                    "id": "my-id-for-textarea",
                                                                    "rows": 1,
                                                                    'cols': 80
                                                                    }))
    ejecucion = forms.CharField(label='7. Tiempo de Ejecuci??n en meses:',
                                              widget=forms.Textarea(attrs={"placeholder": "7. Tiempo de Ejecuci??n en meses:",
                                                                           "class": "new-class-name two",
                                                                           "id": "my-id-for-textarea",
                                                                           "rows": 1,
                                                                           'cols': 80
                                                                           }))
    observaciones = forms.CharField(label='11. Observaciones:',
                                   widget=forms.Textarea(attrs={"placeholder": "11. Observaciones:",
                                                                "class": "new-class-name two",
                                                                "id": "my-id-for-textarea",
                                                                "rows": 2,
                                                                'cols': 80
                                                                }))


    class Meta:
        model = Presupuesto
        fields = '__all__'

class FilarmonicaForm(forms.ModelForm):
    justifique = forms.CharField(label='Justifique su respuesta:',
                            widget=forms.Textarea(attrs={"placeholder": "Justifique su respuesta:",
                                                         "class": "new-class-name two",
                                                         "id": "my-id-for-textarea",
                                                         "rows": 3,
                                                         'cols': 80
                                                         }))
    name = forms.CharField(label='Nombres y Apellidos : *',
                           widget=forms.Textarea(attrs={"placeholder": "Nombres y Apellidos *",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))
    dirige = forms.CharField(label='Programa que dirige:',
                            widget=forms.Textarea(attrs={"placeholder": "Programa que dirige:",
                                                         "class": "new-class-name two",
                                                         "id": "my-id-for-textarea",
                                                         "rows": 1,
                                                         'cols': 80
                                                         }))
    grado = forms.CharField(label='M??ximo grado en m??sica que haya cursado:',
                            widget=forms.Textarea(attrs={"placeholder": "M??ximo grado en m??sica que haya cursado:",
                                                         "class": "new-class-name two",
                                                         "id": "my-id-for-textarea",
                                                         "rows": 1,
                                                         'cols': 80
                                                         }))
    grupo = forms.CharField(label='Grupo que maneja actualmente en el municipio:',
                            widget=forms.Textarea(attrs={"placeholder": "Grupo que maneja actualmente en el municipio:",
                                                         "class": "new-class-name two",
                                                         "id": "my-id-for-textarea",
                                                         "rows": 1,
                                                         'cols': 80
                                                         }))
    email = forms.EmailField(label='Correo electr??nico*',
                    widget=forms.Textarea(attrs={"placeholder": "Correo *",
                                                  "class": "new-class-name two",
                                                  "id": "my-id-for-textarea",
                                                  "rows": 1,
                                                  'cols': 80
                                                  }))

    phone = forms.CharField(label='Tel??fono:',
                           widget=forms.Textarea(attrs={"placeholder": "Tel??fono:",
                                                        "class": "new-class-name two",
                                                        "id": "my-id-for-textarea",
                                                        "rows": 1,
                                                        'cols': 80
                                                        }))


    class Meta:
        model = Filarmonica
        fields = '__all__'
