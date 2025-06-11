from django.db import models
from autenticacion.models import Usuario
from notas.models import *
from asignaturas.models import PeriodoAcademico  # Importar PeriodoAcademico desde asignaturas.models

# Create your models here.

class TipoFalta(models.Model):
    NIVELES = [
        ('LEVE', 'Falta Leve'),
        ('GRAVE', 'Falta Grave'),
        ('MUY_GRAVE', 'Falta Muy Grave')
    ]
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel = models.CharField(max_length=30, choices=NIVELES)
    
    class Meta:
        verbose_name = "Tipo de Falta"
        verbose_name_plural = "Tipos de Faltas"
        ordering = ['nivel', 'nombre']
    
    def __str__(self):
        return f"{self.get_nivel_display()} - {self.nombre}"

class RegistroComportamiento(models.Model):
    TIPOS = [
        ('POSITIVO', 'Observación Positiva'),
        ('NEGATIVO', 'Observación Negativa')
    ]
    
    estudiante = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='registros_comportamiento'
    )
    periodo = models.ForeignKey(
        PeriodoAcademico,
        on_delete=models.CASCADE
    )
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=30, choices=TIPOS)
    descripcion = models.TextField()
    tipo_falta = models.ForeignKey(
        TipoFalta,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Solo aplica para observaciones negativas"
    )
    registrado_por = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        related_name='registros_realizados'
    )
    
    class Meta:
        verbose_name = "Registro de Comportamiento"
        verbose_name_plural = "Registros de Comportamiento"
        ordering = ['-fecha']
    
    def __str__(self):
        return f"{self.estudiante} - {self.get_tipo_display()} - {self.fecha.strftime('%d/%m/%Y')}"

class Compromiso(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En Proceso'),
        ('CUMPLIDO', 'Cumplido'),
        ('INCUMPLIDO', 'Incumplido')
    ]
    
    registro = models.ForeignKey(
        RegistroComportamiento,
        on_delete=models.CASCADE,
        related_name='compromisos'
    )
    descripcion = models.TextField()
    fecha_compromiso = models.DateField()
    fecha_seguimiento = models.DateField()
    estado = models.CharField(
        max_length=15,
        choices=ESTADOS,
        default='PENDIENTE'
    )
    observaciones = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Compromiso"
        verbose_name_plural = "Compromisos"
        ordering = ['fecha_compromiso']
    
    def __str__(self):
        return f"Compromiso de {self.registro.estudiante} - {self.fecha_compromiso}"
