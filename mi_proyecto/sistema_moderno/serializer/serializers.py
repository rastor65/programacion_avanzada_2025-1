from rest_framework import serializers
from django.contrib.auth.models import User
from autenticacion.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from notificaciones.models import *
from asistencias.models import *
from notas.models import *
from comportamiento.models import *
from rest_framework.validators import UniqueTogetherValidator
from asignaturas.models import Asignatura, Curso, Horario, MatriculaCurso, AsignaturaCurso


# Serializers en Clase y tambien de guia de auth
# RolSimpleSerializer:
class RolSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre']

# RolCompletoSerializer:
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rol
        fields= ['id', 'nombre', 'descripcion']


# Serializer en casa

# UsuarioSerializer:

class UsuarioSerializer(serializers.ModelSerializer):
    rol_nombre = serializers.CharField(source='rol.nombre', read_only=True)
    rol_id = serializers.IntegerField(source='rol.id', read_only=True)
    roles = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = ['id', 'nombres', 'apellidos', 'promedio', 'disponibilidad', 'rol_id', 'rol_nombre', 'roles']

    def get_roles(self, obj):
        from autenticacion.models import UsuarioRol # Evitar importación circular
        
        asignaciones = UsuarioRol.objects.filter(usuario=obj).select_related('rol')

        return [
            {
                "id": ar.rol.id,
                "nombre": ar.rol.nombre,
            }
            for ar in asignaciones
        ]


# RegisterSerializer:

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'email', 'nombres', 'apellidos', 'promedio', 'disponibilidad']

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        email = validated_data.pop('email')

        user = User.objects.create_user(username=username, password=password, email=email)

        try:
            rol_estudiante = Rol.objects.get(nombre_iexact="Usuario")
        except Rol.DoesNotExist:
            raise serializers.ValidationError("El rol 'Usuario' no está configurado en el sistema.")
        
        usuario = Usuario.objects.create(
            user=user,
            rol=rol_estudiante,
            **validated_data
        )
        return usuario

# UsuarioRolSerializer:

class UsuarioRolSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    rol = serializers.PrimaryKeyRelatedField(queryset=Rol.objects.all())


    class Meta:
        model = UsuarioRol
        fields = ['id', 'usuario', 'rol', 'asignado_en']


# LoginSerializer:
class LoginSerializer(TokenObtainPairSerializer):
    username = serializers.CharField()
    password = serializers.CharField()



# Serializers Notificaciones
class TipoNotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoNotificacion
        fields = ['id', 'nombre', 'mensaje', 'prioridad']

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = ['id', 'usuario', 'tipo', 'titulo', 'mensaje', 'leido', 'fecha']
        read_only_fields = ['fecha']



# Serializers Asistencias
class AsistenciaSerializer(serializers.ModelSerializer):
    estudiante_nombre = serializers.SerializerMethodField()
    curso_detalle = serializers.SerializerMethodField()
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)

    class Meta:
        model = Asistencia
        fields = [
            'id', 'matricula', 'estudiante_nombre', 'curso_detalle',
            'fecha', 'hora', 'estado', 'estado_display',
            'justificacion', 'validada', 'creado_en', 'actualizado_en'
        ]
        read_only_fields = ['creado_en', 'actualizado_en']

    def get_estudiante_nombre(self, obj):
        if obj.matricula:
            return f"{obj.matricula.estudiante.nombres} {obj.matricula.estudiante.apellidos}"
        return f"{obj.usuario.nombres} {obj.usuario.apellidos}" if obj.usuario else "Sin asignar"

    def get_curso_detalle(self, obj):
        if obj.matricula:
            return str(obj.matricula.curso)
        return "Sin asignar"

class AsistenciaListSerializer(serializers.ModelSerializer):
    estudiante_nombre = serializers.SerializerMethodField()
    curso_detalle = serializers.SerializerMethodField()
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)

    class Meta:
        model = Asistencia
        fields = [
            'id', 'estudiante_nombre', 'curso_detalle',
            'fecha', 'hora', 'estado', 'estado_display', 'validada'
        ]

    def get_estudiante_nombre(self, obj):
        if obj.matricula:
            return f"{obj.matricula.estudiante.nombres} {obj.matricula.estudiante.apellidos}"
        return f"{obj.usuario.nombres} {obj.usuario.apellidos}" if obj.usuario else "Sin asignar"

    def get_curso_detalle(self, obj):
        if obj.matricula:
            return str(obj.matricula.curso)
        return "Sin asignar"


# Serializers Notas
class PeriodoAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodoAcademico
        fields = ['id', 'nombre', 'numero', 'año_lectivo', 'fecha_inicio', 'fecha_fin', 'activo']

class TipoActividadSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TipoActividad
        fields = ['id', 'nombre', 'descripcion', 'porcentaje']

    def validate_porcentaje(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("El porcentaje debe estar entre 0 y 100")
        return value

class ActividadSerializer(serializers.ModelSerializer):
    tipo_nombre = serializers.CharField(source='tipo.nombre', read_only=True)
    tipo_porcentaje = serializers.FloatField(source='tipo.porcentaje', read_only=True)
    periodo_nombre = serializers.CharField(source='periodo.nombre', read_only=True)

    class Meta:
        model = Actividad
        fields = [
            'id', 'nombre', 'tipo', 'tipo_nombre', 'tipo_porcentaje',
            'periodo', 'periodo_nombre', 'fecha_asignacion',
            'fecha_entrega', 'descripcion'
        ]

class NotaSerializer(serializers.ModelSerializer):
    estudiante_nombre = serializers.SerializerMethodField()
    actividad_nombre = serializers.CharField(source='actividad.nombre', read_only=True)
    tipo_actividad = serializers.CharField(source='actividad.tipo.nombre', read_only=True)
    tipo_porcentaje = serializers.FloatField(source='actividad.tipo.porcentaje', read_only=True)
    periodo = serializers.CharField(source='actividad.periodo.nombre', read_only=True)

    class Meta:
        model = Nota
        fields = [
            'id', 'estudiante', 'estudiante_nombre',
            'actividad', 'actividad_nombre', 'tipo_actividad',
            'tipo_porcentaje', 'periodo', 'valor', 'observaciones',
            'es_recuperacion', 'creado_en', 'actualizado_en'
        ]

    def get_estudiante_nombre(self, obj):
        return f"{obj.estudiante.nombres} {obj.estudiante.apellidos}"

    def validate_valor(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError("El valor de la nota debe estar entre 0 y 10")
        return round(value, 2)  # Redondear a 2 decimales

class BoletinPeriodoSerializer(serializers.Serializer):
    periodo = PeriodoAcademicoSerializer()
    notas_por_tipo = serializers.DictField()
    promedio_periodo = serializers.FloatField()


# Serializers Comportamiento
class TipoFaltaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFalta
        fields = '__all__'

class RegistroComportamientoSerializer(serializers.ModelSerializer):
    estudiante_nombre = serializers.SerializerMethodField()
    registrado_por_nombre = serializers.SerializerMethodField()
    tipo_falta_detalle = TipoFaltaSerializer(source='tipo_falta', read_only=True)

    class Meta:
        model = RegistroComportamiento
        fields = '__all__'
        extra_fields = ['estudiante_nombre', 'registrado_por_nombre', 'tipo_falta_detalle']

    def get_estudiante_nombre(self, obj):
        return f"{obj.estudiante.nombres} {obj.estudiante.apellidos}"

    def get_registrado_por_nombre(self, obj):
        if obj.registrado_por:
            return f"{obj.registrado_por.nombres} {obj.registrado_por.apellidos}"
        return None

class CompromisoSerializer(serializers.ModelSerializer):
    registro_detalle = RegistroComportamientoSerializer(source='registro', read_only=True)

    class Meta:
        model = Compromiso
        fields = '__all__'
        extra_fields = ['registro_detalle']


# Serializers Asignaturas
class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = [
            'id', 'codigo', 'nombre', 
            'descripcion', 'area_estudio'
        ]

class CursoSerializer(serializers.ModelSerializer):
    nivel_display = serializers.CharField(source='get_nivel_display', read_only=True)
    periodo_display = serializers.CharField(source='get_periodo_display', read_only=True)

    class Meta:
        model = Curso
        fields = [
            'id', 'nivel', 'nivel_display', 
            'paralelo', 'cupo_maximo', 'estado',
            'periodo', 'periodo_display'
        ]

class AsignaturaCursoSerializer(serializers.ModelSerializer):
    curso_detalle = serializers.CharField(source='curso.__str__', read_only=True)
    asignatura_detalle = serializers.CharField(source='asignatura.__str__', read_only=True)

    class Meta:
        model = AsignaturaCurso
        fields = [
            'id', 'curso', 'curso_detalle',
            'asignatura', 'asignatura_detalle',
            'horas_semanales', 'fecha_inicio', 'fecha_fin'
        ]


class HorarioSerializer(serializers.ModelSerializer):
    dia_display = serializers.CharField(source='get_dia_display', read_only=True)
    curso = serializers.SerializerMethodField()
    asignatura = serializers.SerializerMethodField()
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Horario
        fields = [
            'id', 'curso', 'asignatura', 'periodo',
            'dia', 'dia_display', 'hora_inicio', 'hora_fin'
        ]

    def get_curso(self, obj):
        if obj.asignatura_curso:
            curso = obj.asignatura_curso.curso
            return f"{curso.get_nivel_display()}-{curso.paralelo}"
        return None

    def get_asignatura(self, obj):
        if obj.asignatura_curso:
            return obj.asignatura_curso.asignatura.nombre
        return None

    def get_periodo(self, obj):
        if obj.asignatura_curso:
            return obj.asignatura_curso.curso.get_periodo_display()
        return None

class MatriculaCursoSerializer(serializers.ModelSerializer):
    estudiante_nombre = serializers.SerializerMethodField()
    curso_detalle = serializers.SerializerMethodField()
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)

    class Meta:
        model = MatriculaCurso
        fields = [
            'id', 'estudiante', 'estudiante_nombre',
            'curso', 'curso_detalle',
            'fecha_matricula', 'estado', 'estado_display'
        ]

    def get_estudiante_nombre(self, obj):
        return f"{obj.estudiante.nombres} {obj.estudiante.apellidos}"

    def get_curso_detalle(self, obj):
        return str(obj.curso)


