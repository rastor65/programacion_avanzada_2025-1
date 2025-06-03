from django.db import models
from autenticacion.models import *

# Create your models here.
class Asistencia(TimeStampedModel):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='asistencias',
        verbose_name="Usuario"
    )
    fecha = models.DateField(verbose_name="Fecha")
    hora = models.TimeField(verbose_name="Hora")
    estado = models.CharField(
        max_length=30,
        choices=[
            ('PRESENTE', 'Presente'),
            ('AUSENTE', 'Ausente'),
            ('TARDE', 'Tardanza'),
            ('JUSTIFICADA', 'Con Justificación')
        ],

    )
    justificacion = models.TextField(
        null=True,
        blank=True,
        verbose_name="Justificación"
    )
    validada = models.BooleanField(
        default=False,
        verbose_name="¿Validada?"
    )

    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"
        ordering = ['-fecha', '-hora']
        # Asegurar que no haya duplicados de asistencia para el mismo usuario en la misma fecha y hora
        unique_together = ['usuario', 'fecha', 'hora']

    def __str__(self):
        return f"{self.usuario} - {self.fecha} {self.hora} - {self.get_estado_display()}"
