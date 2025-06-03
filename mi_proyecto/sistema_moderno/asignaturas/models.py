from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Asignatura(models.Model):
    codigo = models.CharField(
        max_length=30, 
        unique=True,
        help_text="Código único de la asignatura"
    )
    nombre = models.CharField(
        max_length=100,
        help_text="Nombre de la asignatura"
    )
    descripcion = models.TextField(
        blank=True,
        help_text="Descripción detallada de la asignatura"
    )
    area_estudio = models.CharField(
        max_length=100,
        help_text="Área de estudio de la asignatura"
    )
    fecha_inicio = models.DateTimeField(
        help_text="Fecha de inicio de la asignatura"
    )
    fecha_fin = models.DateTimeField(
        help_text="Fecha de finalización de la asignatura"
    )

    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.area_estudio}"

class Curso(models.Model):
    NIVEL_CHOICES = [
        ('1', 'Primero'),
        ('2', 'Segundo'),
        ('3', 'Tercero'),
        ('4', 'Cuarto'),
        ('5', 'Quinto'),
        ('6', 'Sexto'),
        ('7', 'Séptimo'),
        ('8', 'Octavo'),
        ('9', 'Noveno'),
        ('10', 'Décimo'),
        ('11', 'Once')
    ]

    asignatura = models.ForeignKey(
        Asignatura,
        on_delete=models.CASCADE,
        related_name='cursos'
    )
    nivel = models.CharField(
        max_length=2,
        choices=NIVEL_CHOICES,
        help_text="Grado escolar del curso"
    )
    paralelo = models.CharField(
        max_length=2,
        help_text="Número del grupo (01, 02, etc.)"
    )
    cupo_maximo = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Cupo máximo de estudiantes"
    )
    estado = models.BooleanField(
        default=True,
        help_text="Estado del curso (activo/inactivo)"
    )

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        unique_together = ['asignatura', 'nivel', 'paralelo']
        ordering = ['nivel', 'paralelo']

    def clean(self):
        # Asegurarse de que el paralelo siempre tenga dos dígitos
        if self.paralelo and len(self.paralelo) == 1:
            self.paralelo = f"0{self.paralelo}"
        super().clean()

    def __str__(self):
        return f"{self.asignatura.nombre} - {self.get_nivel_display()}-{self.paralelo}"

class Horario(models.Model):
    DIAS_SEMANA = [
        ('LUN', 'Lunes'),
        ('MAR', 'Martes'),
        ('MIE', 'Miércoles'),
        ('JUE', 'Jueves'),
        ('VIE', 'Viernes')
    ]

    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='horarios'
    )
    dia = models.CharField(
        max_length=3,
        choices=DIAS_SEMANA,
        help_text="Día de la semana"
    )
    hora_inicio = models.TimeField(
        help_text="Hora de inicio de la clase"
    )
    hora_fin = models.TimeField(
        help_text="Hora de finalización de la clase"
    )

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"
        ordering = ['dia', 'hora_inicio']
        unique_together = ['curso', 'dia', 'hora_inicio']

    def __str__(self):
        return f"{self.curso} - {self.get_dia_display()} {self.hora_inicio.strftime('%H:%M')} - {self.hora_fin.strftime('%H:%M')}"
