from django.db import models
from apps.autenticacion.models import TimeStampedModel, Usuario

class TipoOperacion(models.Model):
    nombre = models.CharField(max_length=50)
    simbolo = models.CharField(max_length=5)
    descripcion = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Tipo de Operación"
        verbose_name_plural = "Tipos de Operaciones"
    
    def __str__(self):
        return self.nombre

class NivelDificultad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    rango_min = models.IntegerField(default=1)
    rango_max = models.IntegerField(default=10)
    
    class Meta:
        verbose_name = "Nivel de Dificultad"
        verbose_name_plural = "Niveles de Dificultad"
    
    def __str__(self):
        return self.nombre

class Ejercicio(TimeStampedModel):
    tipo_operacion = models.ForeignKey(TipoOperacion, on_delete=models.CASCADE)
    nivel_dificultad = models.ForeignKey(NivelDificultad, on_delete=models.CASCADE)
    operando1 = models.FloatField()
    operando2 = models.FloatField()
    resultado_correcto = models.FloatField()
    
    class Meta:
        verbose_name = "Ejercicio"
        verbose_name_plural = "Ejercicios"
    
    def __str__(self):
        return f"{self.operando1} {self.tipo_operacion.simbolo} {self.operando2} = {self.resultado_correcto}"

class SesionPractica(TimeStampedModel):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nivel_dificultad = models.ForeignKey(NivelDificultad, on_delete=models.CASCADE)
    tipo_operacion = models.ForeignKey(TipoOperacion, on_delete=models.CASCADE, null=True, blank=True)
    cantidad_ejercicios = models.IntegerField(default=10)
    tiempo_total = models.IntegerField(default=0, help_text="Tiempo total en segundos")
    completada = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Sesión de Práctica"
        verbose_name_plural = "Sesiones de Práctica"
    
    def __str__(self):
        return f"Sesión de {self.usuario} - {self.creado_en}"
