from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(TipoFalta)
class TipoFaltaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel')
    list_filter = ('nivel',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nivel', 'nombre')


@admin.register(RegistroComportamiento)
class RegistroComportamientoAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'tipo', 'fecha', 'tipo_falta', 'registrado_por')
    list_filter = ('tipo', 'periodo', 'tipo_falta__nivel')
    search_fields = ('estudiante__nombres', 'estudiante__apellidos', 'descripcion')
    raw_id_fields = ('estudiante', 'registrado_por')
    date_hierarchy = 'fecha'


@admin.register(Compromiso)
class CompromisoAdmin(admin.ModelAdmin):
    list_display = ('registro', 'fecha_compromiso', 'fecha_seguimiento', 'estado')
    list_filter = ('estado', 'fecha_compromiso')
    search_fields = ('descripcion', 'observaciones', 'registro__estudiante__nombres')
    raw_id_fields = ('registro',)
    date_hierarchy = 'fecha_compromiso'
