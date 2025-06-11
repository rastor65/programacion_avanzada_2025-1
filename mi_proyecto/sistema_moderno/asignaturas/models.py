from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class PeriodoAcademico(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.PositiveSmallIntegerField()
    año_lectivo = models.PositiveIntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Período Académico"
        verbose_name_plural = "Períodos Académicos"
        ordering = ['-año_lectivo', 'numero']
        unique_together = ('numero', 'año_lectivo')

    def __str__(self):
        return f"{self.nombre} ({self.año_lectivo})"


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
        unique_together = ['nivel', 'paralelo']  # Elimina 'periodo'
        ordering = ['nivel', 'paralelo']  # Elimina 'periodo'

    def clean(self):
        if self.paralelo and len(self.paralelo) == 1:
            self.paralelo = f"0{self.paralelo}"
        super().clean()

    def __str__(self):
        return f"{self.get_nivel_display()}-{self.paralelo}"  # Elimina referencia a periodo


# Asignatura
class Asignatura(models.Model):
    NIVELES_CHOICES = [
        ('PRIMARIA', 'Primaria'),
        ('BACHILLERATO', 'Bachillerato'),
        ('TODOS', 'Todos los niveles')
    ]

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
    nivel_educativo = models.CharField(
        max_length=20,
        choices=NIVELES_CHOICES,
        default='TODOS',
        help_text="Nivel educativo en el que se imparte la asignatura"
    )
    niveles_especificos = models.JSONField(
        default=list,
        help_text="Lista de niveles específicos donde se imparte la asignatura (ej: ['6', '7', '8'] para grados 6-8)"
    )
    horas_semanales = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Número de horas semanales de la asignatura",
        default=1
    )

    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.area_estudio}"

    def clean(self):
        from django.core.exceptions import ValidationError
        
        # Validar que los niveles específicos sean válidos
        if self.nivel_educativo == 'PRIMARIA':
            niveles_validos = ['1', '2', '3', '4', '5']
        elif self.nivel_educativo == 'BACHILLERATO':
            niveles_validos = ['6', '7', '8', '9', '10', '11']
        else:  # TODOS
            niveles_validos = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
        
        for nivel in self.niveles_especificos:
            if nivel not in niveles_validos:
                raise ValidationError(f'El nivel {nivel} no es válido para el nivel educativo {self.nivel_educativo}')

    def se_imparte_en_nivel(self, nivel):
        """
        Verifica si la asignatura se imparte en un nivel específico
        """
        if self.nivel_educativo == 'TODOS':
            return True
        return str(nivel) in self.niveles_especificos

    def get_cursos_disponibles(self):
        """
        Retorna los cursos disponibles para esta asignatura
        """
        from .models import Curso
        return Curso.objects.filter(nivel__in=self.niveles_especificos)


# Horario de una asignatura en un curso
class Horario(models.Model):
    DIAS_SEMANA = [
        ('LUN', 'Lunes'),
        ('MAR', 'Martes'),
        ('MIE', 'Miércoles'),
        ('JUE', 'Jueves'),
        ('VIE', 'Viernes')
    ]

    asignatura = models.ForeignKey(
        Asignatura,
        on_delete=models.CASCADE,
        related_name='horarios',
        help_text="Asignatura para este horario",
        null=True,  
        blank=True  
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='horarios',
        help_text="Curso para este horario"
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
        unique_together = ['asignatura', 'curso', 'dia', 'hora_inicio']

    def __str__(self):
        return f"{self.asignatura} - {self.curso} - {self.get_dia_display()} {self.hora_inicio.strftime('%H:%M')} - {self.hora_fin.strftime('%H:%M')}"

    def clean(self):
        from django.core.exceptions import ValidationError
        
        # Validar que la asignatura se imparte en el nivel del curso
        if not self.asignatura.se_imparte_en_nivel(self.curso.nivel):
            raise ValidationError(f'La asignatura {self.asignatura} no se imparte en el nivel {self.curso.get_nivel_display()}')
        
        # Validar que no haya solapamiento de horarios
        horarios_solapados = Horario.objects.filter(
            curso=self.curso,
            dia=self.dia
        ).exclude(id=self.id)
        
        for horario in horarios_solapados:
            if (self.hora_inicio <= horario.hora_fin and self.hora_fin >= horario.hora_inicio):
                raise ValidationError(
                    f'El horario se solapa con {horario.asignatura} ({horario.hora_inicio}-{horario.hora_fin})'
                )


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


class Nota(models.Model):
    estudiante = models.ForeignKey('autenticacion.Usuario', on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    periodo_academico = models.ForeignKey(PeriodoAcademico, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(10)])
