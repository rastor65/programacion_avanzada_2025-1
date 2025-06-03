from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'area_estudio', 'fecha_inicio', 'fecha_fin')
    list_filter = ('area_estudio',)
    search_fields = ('codigo', 'nombre', 'descripcion', 'area_estudio')
    fieldsets = (
        ('Información Básica', {
            'fields': ('codigo', 'nombre', 'descripcion', 'area_estudio')
        }),
        ('Fechas', {
            'fields': ('fecha_inicio', 'fecha_fin')
        }),
    )

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('asignatura', 'nivel', 'paralelo', 'cupo_maximo', 'estado')
    list_filter = ('asignatura', 'nivel', 'estado')
    search_fields = ('asignatura__nombre', 'nivel', 'paralelo')
    list_editable = ('estado',)

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('curso', 'dia', 'hora_inicio', 'hora_fin')
    list_filter = ('dia', 'curso__asignatura')
    search_fields = ('curso__asignatura__nombre', 'curso__nivel', 'curso__paralelo')
    ordering = ('dia', 'hora_inicio')
