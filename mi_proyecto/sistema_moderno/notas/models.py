from django.db import models
from autenticacion.models import *
from django.core.validators import *
from asignaturas.models import PeriodoAcademico

# Create your models here.

class TipoActividad(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción", null=True, blank=True)
    porcentaje = models.FloatField(
        verbose_name="Porcentaje de la evaluación",
        help_text="Porcentaje que representa esta actividad en la calificación del período",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        verbose_name = "Tipo de Actividad"
        verbose_name_plural = "Tipos de Actividades"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.porcentaje}%)"

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.porcentaje < 0 or self.porcentaje > 100:
            raise ValidationError('El porcentaje debe estar entre 0 y 100')

class Actividad(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    tipo = models.ForeignKey(
        TipoActividad,
        on_delete=models.PROTECT,
        related_name='actividades',
        verbose_name="Tipo de Actividad"
    )
    periodo = models.ForeignKey(
        PeriodoAcademico,
        on_delete=models.CASCADE,
        related_name='actividades',
        verbose_name="Período Académico",
        null=True,  # Temporalmente opcional para migrar
        blank=True
    )
    fecha_asignacion = models.DateField(verbose_name="Fecha de asignación")
    fecha_entrega = models.DateField(verbose_name="Fecha de entrega")
    descripcion = models.TextField(verbose_name="Descripción", null=True, blank=True)

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ['periodo', 'fecha_entrega']

    def __str__(self):
        return f"{self.nombre} - {self.tipo} ({self.periodo})"

class Nota(TimeStampedModel):
    estudiante = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='notas',
        verbose_name="Estudiante"
    )
    actividad = models.ForeignKey(
        Actividad,
        on_delete=models.CASCADE,
        related_name='notas',
        verbose_name="Actividad"
    )
    valor = models.FloatField(
        verbose_name="Valor de la nota",
        help_text="Valor numérico de la nota (0-10). Se permite hasta 2 decimales",
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    observaciones = models.TextField(
        null=True,
        blank=True,
        verbose_name="Observaciones",
        help_text="Observaciones o comentarios sobre la nota"
    )
    es_recuperacion = models.BooleanField(
        default=False,
        verbose_name="¿Es recuperación?",
        help_text="Indica si la nota se puede recuperar"
    )

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"
        ordering = ['-actividad__fecha_entrega']
        unique_together = ['estudiante', 'actividad']

    def __str__(self):
        return f"{self.estudiante} - {self.actividad} - {self.valor}"

    def clean(self):
        from django.core.exceptions import ValidationError
        from django.utils import timezone
        
        # Validar rango de nota
        if self.valor < 0 or self.valor > 10:
            raise ValidationError('El valor de la nota debe estar entre 0 y 10')
        
        # Redondear a 2 decimales
        self.valor = round(self.valor, 2)
        
        # Validar que la fecha de la nota no sea anterior a la fecha de asignación
        if hasattr(self, 'actividad') and self.actividad:
            if timezone.now().date() < self.actividad.fecha_asignacion:
                raise ValidationError('No se puede registrar una nota antes de la fecha de asignación de la actividad')
            
            # Validar que no haya más de una recuperación por actividad
            if self.es_recuperacion:
                recuperaciones = Nota.objects.filter(
                    estudiante=self.estudiante,
                    actividad=self.actividad,
                    es_recuperacion=True
                ).exclude(id=self.id)
                if recuperaciones.exists():
                    raise ValidationError('Ya existe una nota de recuperación para esta actividad')

# El modelo PeriodoAcademico ha sido eliminado de esta app. Usar el de asignaturas.
# Elimina cualquier ForeignKey o referencia a PeriodoAcademico en otros modelos de esta app.
