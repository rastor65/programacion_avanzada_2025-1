from django.contrib import admin
from .models import *

@admin.register(PeriodoAcademico)
class PeriodoAcademicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero', 'año_lectivo', 'fecha_inicio', 'fecha_fin', 'activo')
    list_filter = ('año_lectivo', 'activo')
    search_fields = ('nombre',)
    ordering = ('-año_lectivo', 'numero')

@admin.register(TipoActividad)
class TipoActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'porcentaje', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'periodo', 'fecha_asignacion', 'fecha_entrega')
    list_filter = ('tipo', 'periodo', 'fecha_entrega')
    search_fields = ('nombre', 'descripcion')
    ordering = ('periodo', 'fecha_entrega')
    date_hierarchy = 'fecha_entrega'

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'actividad', 'valor', 'es_recuperacion', 'creado_en')
    list_filter = (
        'actividad__periodo',
        'actividad__tipo',
        'es_recuperacion',
        'actividad__fecha_entrega'
    )
    search_fields = (
        'estudiante__nombres',
        'estudiante__apellidos',
        'actividad__nombre',
        'observaciones'
    )
    ordering = ('-actividad__fecha_entrega',)
    raw_id_fields = ('estudiante', 'actividad')
    date_hierarchy = 'creado_en'
