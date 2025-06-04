from django.db import models
from autenticacion.models import *
from asignaturas.models import MatriculaCurso

# Create your models here.
class Asistencia(TimeStampedModel):
    # Mantenemos el campo usuario temporalmente para la migración
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='asistencias_old',
        verbose_name="Usuario",
        null=True,
        blank=True
    )
    # Nuevo campo matricula que será obligatorio después de la migración
    matricula = models.ForeignKey(
        MatriculaCurso,
        on_delete=models.CASCADE,
        related_name='asistencias',
        verbose_name="Matrícula del Estudiante",
        help_text="Matrícula del estudiante en el curso",
        null=True,
        blank=True
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
        # Asegurar que no haya duplicados de asistencia para la misma matrícula en la misma fecha y hora
        unique_together = ['matricula', 'fecha', 'hora']

    def __str__(self):
        if self.matricula:
            return f"{self.matricula.estudiante} - {self.matricula.curso} - {self.fecha} {self.hora} - {self.get_estado_display()}"
        return f"{self.usuario} - {self.fecha} {self.hora} - {self.get_estado_display()}"

    def clean(self):
        from django.core.exceptions import ValidationError
        
        # Asegurarse de que al menos uno de los campos esté presente
        if not self.usuario and not self.matricula:
            raise ValidationError('Debe especificar un usuario o una matrícula')
            
        # Si hay matrícula, verificar que esté activa
        if self.matricula and self.matricula.estado != 'ACTIVO':
            raise ValidationError('No se puede registrar asistencia para una matrícula que no está activa')
