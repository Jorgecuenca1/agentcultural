from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Country, Region, City, Zone, TypeDocument, Genero, GroupEtnico, Disability, PopulationGroup, \
    HealthRegimen, HousingStratum, MonthlyIncome, PensionRegimen, Sector, Area, Formacion, Activity, AgentCultural, \
    Manifestation, Victima, Entidad, Regimen, Subregimen, Naturaleza, Caracterentidad, NivelEntidad, FormacionE

from django.contrib import admin
from django.contrib.auth.models import User

admin.site.site_header = "SIDECU"
admin.site.site_title = "SIDECU"
admin.site.index_title = "BIENVENIDOS AL PORTAL DE SIDECU"


@admin.register(Regimen)
class RegimenAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class RegimenResource(resources.ModelResource):
   class Meta:
    model = Regimen

@admin.register(Subregimen)
class SubregimenAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class SubregimenResource(resources.ModelResource):
   class Meta:
    model = Subregimen

@admin.register(Naturaleza)
class NaturalezaAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class NaturalezaResource(resources.ModelResource):
   class Meta:
    model = Naturaleza

@admin.register(Caracterentidad)
class CaracterentidadAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class CaracterentidadResource(resources.ModelResource):
   class Meta:
    model = Caracterentidad

@admin.register(NivelEntidad)
class NivelEntidadAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class NivelEntidadResource(resources.ModelResource):
   class Meta:
    model = NivelEntidad

@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class CountryResource(resources.ModelResource):
   class Meta:
    model = Country


@admin.register(Region)
class RegionAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class RegionResource(resources.ModelResource):
   class Meta:
    model = Region


@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class CityResource(resources.ModelResource):
   class Meta:
    model = City

@admin.register(Zone)
class ZoneAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class ZoneResource(resources.ModelResource):
   class Meta:
    model = Zone

@admin.register(TypeDocument)
class TypeDocumentAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class TypeDocumentResource(resources.ModelResource):
   class Meta:
    model = TypeDocument

@admin.register(Genero)
class GeneroAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class GeneroResource(resources.ModelResource):
   class Meta:
    model = Genero

@admin.register(GroupEtnico)
class GroupEtnicoAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class GroupEtnicoResource(resources.ModelResource):
   class Meta:
    model = GroupEtnico

@admin.register(Disability)
class DisabilityAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class DisabilityResource(resources.ModelResource):
   class Meta:
    model = Disability

@admin.register(PopulationGroup)
class PopulationGroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class PopulationGroupResource(resources.ModelResource):
   class Meta:
    model = PopulationGroup

@admin.register(HousingStratum)
class HousingStratumAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class HousingStratumResource(resources.ModelResource):
   class Meta:
    model = HousingStratum


@admin.register(HealthRegimen)
class HealthRegimenAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class HealthRegimenResource(resources.ModelResource):
   class Meta:
    model = HealthRegimen

@admin.register(PensionRegimen)
class PensionRegimenAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class PensionRegimenResource(resources.ModelResource):
   class Meta:
    model = PensionRegimen

@admin.register(MonthlyIncome)
class MonthlyIncomeAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class MonthlyIncomeResource(resources.ModelResource):
   class Meta:
    model = MonthlyIncome

@admin.register(Sector)
class SectorAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class SectorResource(resources.ModelResource):
   class Meta:
    model = Sector

@admin.register(Area)
class AreaAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class AreaResource(resources.ModelResource):
   class Meta:
    model = Area

@admin.register(Formacion)
class FormacionAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class FormacionResource(resources.ModelResource):
   class Meta:
    model = Formacion
class FormacionEAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class FormacionEResource(resources.ModelResource):
   class Meta:
    model = FormacionE
@admin.register(Activity)
class ActivityAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class ActivityResource(resources.ModelResource):
   class Meta:
    model = Activity

@admin.register(Manifestation)
class ManifestationAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class ManifestationResource(resources.ModelResource):
   class Meta:
    model = Manifestation
@admin.register(Victima)
class VictimaAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class VictimaResource(resources.ModelResource):
   class Meta:
    model = Victima

@admin.register(AgentCultural)
class AgentCulturalAdmin(ImportExportModelAdmin):
    readonly_fields = ('created',)
    list_display = (
    'pk', 'tipo','user', 'name', 'last_name','artistic_name', 'gender',  'lugar_nacimiento', 'type_document',  'identification', 'lugar_expedicion',
    'tarjeta_profesional', 'expedicion_tarjeta', 'passport', 'expedicion_passport', 'vencimiento_passport', 'posee_discapacidad', 'disability', 'posee_etnico', 'etnico','esvictima',
    'victima',  'zona', 'adress','adress2', 'email','web',  'forma_practica', 'area2','practica', 'pertenece_entidad', 'vinculacion_entidad',
    'name_entity', 'nivel_educacion', 'titulo','ano_titulo',  'otra_actividad','fuente_ingreso',  'regimen_salud', 'health_regimen',
    'regimen_pension',  'regimen_arl', 'created',)
    list_display_links = ('pk',)

    search_fields = ( 'identification','name', 'other_name', 'last_name', 'last_name2',)
    #list_filter = ('user',)
    fieldsets = (
        ('DATOS DE IDENTIFICACIÓN', {
            'fields': (( 'tipo','user', 'name', 'last_name','artistic_name', 'gender', 'birthday', 'lugar_nacimiento', 'type_document',  'identification', 'lugar_expedicion',
            'tarjeta_profesional', 'expedicion_tarjeta', 'passport', 'expedicion_passport', 'vencimiento_passport', 'posee_discapacidad', 'disability', 'posee_etnico', 'etnico','esvictima',
            'victima',),
                       ),

        }),
        ('DATOS DE UBICACIÓN', {
            'fields': (( 'city', 'zona', 'adress','adress2', 'phone', 'phone_movil', 'email','web',),),

        }),
        ('CARACTERÍSTICAS GENERALES', {
            'fields': (('desarrollo_practica', 'forma_practica', 'area2','practica','vigia_patrimonio','portador_manifestacion', 'manifestation', 'cual_practica', 'pertenece_entidad', 'vinculacion_entidad',
    'name_entity', 'tipo_formacion', 'nivel_educacion', 'titulo','ano_titulo', 'entidad_educativa', 'reseña_trayectoria','servicios','facebook','instagram',),),

        }),
        ('INFORMACIÓN SOCIO ECONÓMICA', {
            'fields': ('tipo_vivienda','housing_stratum', 'tipo_vinculacion', 'cual_vinculacion', 'otra_actividad','fuente_ingreso', 'porcentaje', 'regimen_salud', 'health_regimen',
    'regimen_pension', 'pension_regimen', 'regimen_arl',),

        }),

        ('DOCUMENTOS', {
            'fields': (('sisben','terminosycondiciones','beps','created')),

        }),

    )


class AgentCulturalResource(resources.ModelResource):
   class Meta:
    model = AgentCultural

@admin.register(Entidad)
class EntidadAdmin(ImportExportModelAdmin):


    list_display = (
    'pk', 'user', 'name', 'sigla', 'nit', 'reseña', 'nombre_representante', 'apellidos_representante',
    'type_document', 'identification', 'lugar_expedicion', 'nombre_contacto', 'apellidos_contacto', 'cargo',
    'state', 'city',  'zona', 'direccion', 'correspondencia', 'phone_movil', 'phone', 'apartado_aereo', 'email',
    'pagina_web', 'practica', 'formacion', 'tipo_produccion', 'personeria', 'naturaleza', 'caracter_entidad', 'regimen', 'subregimen','dependencia','entidad_dependiente','nivel','red',
    'name_red','nivel_red','acceso_internet','espacio','infraestructura_discapacitados','interes_cultural','nivel_interescultural','espacios_actividades',
    'genero_empleo','tipo_empleo','cantidad_noremunerado','duracion_noremunerados','cantidad_remunerado','duracion_remunerados','cantidadremunerado_ops',
    'cantidadremunerado_laboral','cantidadrecurso_humano','actividad_principal','otra_actividad','area_artistica','numero_obras','practicas','acceso',
    'proyectos','grupos_edad','grupos_poblacion','organizacion_actividades','etnico','personas_discapacidad','formacion','modalidad','created',)
    list_display_links = ('pk',)
    fieldsets = (
        ('1. DATOS DE IDENTIFICACIÓN', {
            'fields': (('user', 'name', 'sigla', 'nit','date', 'reseña',),
                       ),

        }),
        ('2. DATOS DEL REPRESENTANTE LEGAL', {
            'fields': (('nombre_representante', 'apellidos_representante','cargo_representante',
                    'type_document', 'identification', 'lugar_expedicion',),),

        }),
        ('3. DATOS DEL CONTACTO DE LA ORGANIZACIÓN', {
            'fields': (('nombre_contacto', 'apellidos_contacto', 'cargo',
        'state', 'city',  'zona', 'direccion', 'correspondencia', 'phone_movil', 'phone', 'apartado_aereo', 'email',
         'pagina_web',),),

        }),
        ('4. DATOS JURÌDICOS', {
            'fields': ('practica', 'formacion', 'tipo_produccion', 'personeria', 'naturaleza', 'caracter_entidad','objeto_social', 'regimen', 'subregimen','dependencia','entidad_dependiente','nivel','red',
             'name_red','nivel_red',),

        }),

        ('5. INFRAESTRUTURA', {
            'fields': ((
                'acceso_internet', 'espacio','infraestructura_discapacitados','interes_cultural','nivel_interescultural','espacios_actividades',)),

        }),

        ('6. EMPLEO', {
            'fields': ((
                'genero_empleo','tipo_empleo','cantidad_noremunerado','duracion_noremunerados','cantidad_remunerado','duracion_remunerados','cantidadremunerado_ops',
              'cantidadremunerado_laboral','cantidadrecurso_humano',)),

        }),
        ('7. ACTIVIDADES', {
            'fields': ((
                'actividad_principal', 'otra_actividad', 'area_artistica', 'numero_obras', 'practicas', 'ultimo_año', 'acceso',
                'proyectos', 'grupos_edad', 'grupos_poblacion', 'organizacion_actividades', 'etnico',
                'personas_discapacidad',)),

        }),
        ('8. FORMACION', {
            'fields': ((
                'imparte_formacion', 'modalidad', )),

        }),



    )

    search_fields = ( 'name', 'sigla', 'nit',)
    #list_filter = ('user',)



class EntidadResource(resources.ModelResource):
   class Meta:
    model = Entidad