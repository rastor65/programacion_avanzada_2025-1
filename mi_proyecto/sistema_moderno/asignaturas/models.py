from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Curso
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

    PERIODO_CHOICES = [
        ('P1', 'Primer Periodo'),
        ('P2', 'Segundo Periodo'),
        ('P3', 'Tercer Periodo'),
        ('P4', 'Cuarto Periodo'),
    ]

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
    periodo = models.CharField(
        max_length=2,
        choices=PERIODO_CHOICES,
        help_text="Periodo académico del curso",
        default='P1'
    )

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        unique_together = ['nivel', 'paralelo', 'periodo']
        ordering = ['periodo', 'nivel', 'paralelo']

    def clean(self):
        if self.paralelo and len(self.paralelo) == 1:
            self.paralelo = f"0{self.paralelo}"
        super().clean()

    def __str__(self):
        return f"{self.get_nivel_display()}-{self.paralelo} ({self.get_periodo_display()})"


# Asignatura
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

    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.area_estudio}"



# Asignatura en un curso
class AsignaturaCurso(models.Model):
    # Curso donde se va a dar la asignatura
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='asignaturas',
        help_text="Curso al que pertenece esta asignatura"
    )
    asignatura = models.ForeignKey(
        Asignatura,
        on_delete=models.CASCADE,
        related_name='cursos',
        help_text="Asignatura impartida en este curso"
    )
    horas_semanales = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Número de horas semanales de la asignatura"
    )
    fecha_inicio = models.DateField(
        help_text="Fecha de inicio de la asignatura en este curso"
    )
    fecha_fin = models.DateField(
        help_text="Fecha de finalización de la asignatura en este curso"
    )

    class Meta: 
        verbose_name = "Asignatura en Curso"
        verbose_name_plural = "Asignaturas en Cursos"
        unique_together = ['curso', 'asignatura']
        ordering = ['curso', 'asignatura']

    def __str__(self):
        return f"{self.curso} - {self.asignatura}"



# Horario de una asignatura en un curso
class Horario(models.Model):
    DIAS_SEMANA = [
        ('LUN', 'Lunes'),
        ('MAR', 'Martes'),
        ('MIE', 'Miércoles'),
        ('JUE', 'Jueves'),
        ('VIE', 'Viernes')
    ]

    asignatura_curso = models.ForeignKey(
        AsignaturaCurso,
        on_delete=models.CASCADE,
        related_name='horarios',
        help_text="Asignatura del curso para este horario",
        null=True,  
        blank=True  
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
        unique_together = ['asignatura_curso', 'dia', 'hora_inicio']

    def __str__(self):
        return f"{self.asignatura_curso} - {self.get_dia_display()} {self.hora_inicio.strftime('%H:%M')} - {self.hora_fin.strftime('%H:%M')}"



# Matrícula de un estudiante en un curso
class MatriculaCurso(models.Model):
    estudiante = models.ForeignKey(
        'autenticacion.Usuario',
        on_delete=models.CASCADE,
        related_name='matriculas',
        help_text="Estudiante matriculado en el curso"
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='matriculas',
        help_text="Curso en el que está matriculado el estudiante"
    )
    fecha_matricula = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora de la matricula"
    )
    estado = models.CharField(
        max_length=30,
        choices=[
            ('ACTIVO', 'Activo'),
            ('RETIRADO', 'Retirado'),
            ('SUSPENDIDO', 'Suspendido')
        ],
        default='ACTIVO',
        help_text="Estado de la matrícula del estudiante"
    )

    class Meta:
        verbose_name = "Matrícula en Curso"
        verbose_name_plural = "Matrículas en Cursos"
        unique_together = ['estudiante', 'curso']
        ordering = ['-fecha_matricula']

    def __str__(self):
        return f"{self.estudiante} - {self.curso} ({self.get_estado_display()})"

    def clean(self):
        if not self.curso.estado:
            raise ValidationError('No se puede matricular en un curso inactivo')
        
        matriculas_activas = MatriculaCurso.objects.filter(
            curso=self.curso,
            estado='ACTIVO'
        ).count()
        
        if matriculas_activas >= self.curso.cupo_maximo and self.estado == 'ACTIVO':
            raise ValidationError('El curso ha alcanzado su cupo máximo de estudiantes')
