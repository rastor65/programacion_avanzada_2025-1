from django.db import models
from apps.autenticacion.models import TimeStampedModel, Usuario
from apps.ejercicios.models import Ejercicio, SesionPractica

class Respuesta(TimeStampedModel):
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    sesion = models.ForeignKey(SesionPractica, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    respuesta_usuario = models.FloatField()
    es_correcta = models.BooleanField(default=False)
    tiempo_respuesta = models.IntegerField(help_text="Tiempo en segundos")
    
    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"
    
    def __str__(self):
        return f"Respuesta de {self.usuario} a ejercicio {self.ejercicio.id}"

class ResultadoSesion(TimeStampedModel):
    sesion = models.OneToOneField(SesionPractica, on_delete=models.CASCADE, related_name='resultado')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total_ejercicios = models.IntegerField()
    ejercicios_correctos = models.IntegerField()
    porcentaje_acierto = models.FloatField()
    tiempo_promedio_respuesta = models.FloatField(help_text="Tiempo promedio en segundos")
    
    class Meta:
        verbose_name = "Resultado de Sesión"
        verbose_name_plural = "Resultados de Sesiones"
    
    def __str__(self):
        return f"Resultado de {self.usuario} - {self.sesion.creado_en}"

class Estadistica(TimeStampedModel):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total_sesiones = models.IntegerField(default=0)
    total_ejercicios = models.IntegerField(default=0)
    ejercicios_correctos = models.IntegerField(default=0)
    porcentaje_acierto_global = models.FloatField(default=0)
    tiempo_promedio_global = models.FloatField(default=0, help_text="Tiempo promedio en segundos")
    
    class Meta:
        verbose_name = "Estadística"
        verbose_name_plural = "Estadísticas"
    
    def __str__(self):
        return f"Estadísticas de {self.usuario}"
