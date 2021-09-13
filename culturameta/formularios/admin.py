from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Tiposolicitud, Nivel, Meta, TypeDocument, Pqrsd, EncuestaTransparencia, Modalidad, Propuesta, \
    Torneo, \
    Perfil, Programa, Componente, Presupuesto, Region
from django.contrib import admin
from django.contrib.auth.models import User

@admin.register(Tiposolicitud)
class TiposolicitudAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class TiposolicitudResource(resources.ModelResource):
   class Meta:
    model = Tiposolicitud
@admin.register(Modalidad)
class ModalidadAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class ModalidadResource(resources.ModelResource):
   class Meta:
    model = Modalidad

@admin.register(Propuesta)
class PropuestaAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class PropuestaResource(resources.ModelResource):
   class Meta:
    model = Propuesta

@admin.register(Torneo)
class TorneoAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'email','name', 'agrupacion','seudonimo','type_document', 'identification','expedicion','country', 'region','city', 'adress','phone','phone_movil', 'modalidad','obra1', 'obra2','propuesta','archivo', 'archivo1','link','archivo2','archivo3', 'archivo4',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class TorneoResource(resources.ModelResource):
   class Meta:
    model = Torneo

@admin.register(Nivel)
class NivelAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class NivelResource(resources.ModelResource):
   class Meta:
    model = Nivel


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


@admin.register(Pqrsd)
class PqrsdAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'tiposolicitud','name','last_name','type_document','identification','email','phone','asunto',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class PqrsdResource(resources.ModelResource):
    class Meta:
        model = Pqrsd

@admin.register(EncuestaTransparencia)
class EncuestaTransparenciaAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'encontro','noencontro','facil','nivel','sugerencia',)
    list_display_links = ('pk',)
    list_editable = ('encontro',)
    list_filter = ('encontro',)


class EncuestaTransparenciaResource(resources.ModelResource):
    class Meta:
        model = EncuestaTransparencia

@admin.register(Perfil)
class PerfilAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    list_filter = ('name',)


class PerfilResource(resources.ModelResource):
    class Meta:
        model = Perfil
@admin.register(Region)
class RegionAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    list_filter = ('name',)


class RegionResource(resources.ModelResource):
    class Meta:
        model = Region
@admin.register(Programa)
class ProgramaAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    list_filter = ('name',)


class ProgramaResource(resources.ModelResource):
    class Meta:
        model = Programa

@admin.register(Componente)
class ComponenteAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    list_filter = ('name',)


class ComponenteResource(resources.ModelResource):
    class Meta:
        model = Componente


@admin.register(Meta)
class MetaAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    list_filter = ('name',)


class MetaResource(resources.ModelResource):
    class Meta:
        model = Meta


@admin.register(Presupuesto)
class PresupuestoAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name','email','phone','descripcion',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    list_filter = ('name',)


class PresupuestoResource(resources.ModelResource):
    class Meta:
        model = Presupuesto