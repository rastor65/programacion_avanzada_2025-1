from django.contrib import admin
from .models import Respuesta, ResultadoSesion, Estadistica

@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'ejercicio', 'respuesta_usuario', 'es_correcta', 'tiempo_respuesta')
    list_filter = ('es_correcta', 'usuario')
    search_fields = ('usuario__nombres', 'usuario__apellidos')

@admin.register(ResultadoSesion)
class ResultadoSesionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'sesion', 'total_ejercicios', 'ejercicios_correctos', 
                    'porcentaje_acierto', 'tiempo_promedio_respuesta')
    list_filter = ('usuario',)
    search_fields = ('usuario__nombres', 'usuario__apellidos')

@admin.register(Estadistica)
class EstadisticaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'total_sesiones', 'total_ejercicios', 'ejercicios_correctos',
                    'porcentaje_acierto_global', 'tiempo_promedio_global')
    list_filter = ('usuario',)
    search_fields = ('usuario__nombres', 'usuario__apellidos')
