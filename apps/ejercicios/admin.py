from django.contrib import admin
from .models import TipoOperacion, NivelDificultad, Ejercicio, SesionPractica

@admin.register(TipoOperacion)
class TipoOperacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'simbolo', 'descripcion')
    search_fields = ('nombre', 'simbolo')

@admin.register(NivelDificultad)
class NivelDificultadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rango_min', 'rango_max', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
    list_display = ('tipo_operacion', 'nivel_dificultad', 'operando1', 'operando2', 'resultado_correcto')
    list_filter = ('tipo_operacion', 'nivel_dificultad')
    search_fields = ('tipo_operacion__nombre',)

@admin.register(SesionPractica)
class SesionPracticaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nivel_dificultad', 'tipo_operacion', 'cantidad_ejercicios', 'tiempo_total', 'completada')
    list_filter = ('nivel_dificultad', 'tipo_operacion', 'completada')
    search_fields = ('usuario__nombres', 'usuario__apellidos')
