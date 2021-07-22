from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Tiposolicitud, Nivel, TypeDocument, Pqrsd, EncuestaTransparencia
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