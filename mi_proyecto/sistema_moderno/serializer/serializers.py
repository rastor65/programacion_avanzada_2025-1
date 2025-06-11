from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from autenticacion.models import Usuario, Rol, UsuarioRol
from asignaturas.models import Asignatura, Curso, Horario, MatriculaCurso
from notas.models import TipoActividad, Actividad, Nota, PeriodoAcademico
from notificaciones.models import TipoNotificacion, Notificacion
from asistencias.models import Asistencia
from comportamiento.models import TipoFalta, RegistroComportamiento, Compromiso
from rest_framework.views import APIView


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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']

class UsuarioSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'user', 'rol', 'nombres', 'apellidos', 'promedio', 'disponibilidad']
        read_only_fields = ['id']


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
    tipo_nombre = serializers.CharField(source='tipo.nombre', read_only=True)
    prioridad = serializers.CharField(source='tipo.prioridad', read_only=True)
    usuario_nombre = serializers.CharField(source='usuario.__str__', read_only=True)

    class Meta:
        model = Notificacion
        fields = [
            'id', 'usuario', 'usuario_nombre',
            'tipo', 'tipo_nombre', 'prioridad',
            'titulo', 'mensaje', 'leido',
            'fecha', 'creado_en'
        ]
        read_only_fields = ['fecha', 'creado_en']

    def create(self, validated_data):
        # Si no se especifica un tipo, usar el tipo por defecto para notas
        if 'tipo' not in validated_data:
            tipo, _ = TipoNotificacion.objects.get_or_create(
                nombre='nota',
                defaults={
                    'mensaje': 'Notificación de nota',
                    'prioridad': 'MEDIA'
                }
            )
            validated_data['tipo'] = tipo
        return super().create(validated_data)



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

class AsistenciaMasivaSerializer(serializers.Serializer):
    curso_id = serializers.IntegerField()
    fecha = serializers.DateField()
    hora = serializers.TimeField()
    asistencias = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()
        )
    )

    def validate_curso_id(self, value):
        from asignaturas.models import Curso
        if not Curso.objects.filter(id=value).exists():
            raise serializers.ValidationError("El curso especificado no existe")
        return value

    def validate_asistencias(self, value):
        if not value:
            raise serializers.ValidationError("Debe proporcionar al menos una asistencia")
        for asistencia in value:
            if 'matricula_id' not in asistencia or 'estado' not in asistencia:
                raise serializers.ValidationError("Cada asistencia debe tener matricula_id y estado")
        return value

    def create(self, validated_data):
        from asistencias.models import Asistencia
        from asignaturas.models import MatriculaCurso
        curso_id = validated_data['curso_id']
        fecha = validated_data['fecha']
        hora = validated_data['hora']
        asistencias_data = validated_data['asistencias']
        asistencias_creadas = []
        for asistencia_data in asistencias_data:
            matricula = MatriculaCurso.objects.get(id=asistencia_data['matricula_id'])
            asistencia, _ = Asistencia.objects.update_or_create(
                matricula=matricula,
                fecha=fecha,
                hora=hora,
                defaults={'estado': asistencia_data['estado']}
            )
            asistencias_creadas.append(asistencia)
        return asistencias_creadas


# Serializers Notas
class PeriodoAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodoAcademico
        fields = ['id', 'nombre', 'numero', 'año_lectivo', 'fecha_inicio', 'fecha_fin', 'activo']

class TipoActividadSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TipoActividad
        fields = ['id', 'nombre', 'descripcion', 'porcentaje']
        read_only_fields = ['id']

class ActividadSerializer(serializers.ModelSerializer):
    tipo_nombre = serializers.CharField(source='tipo.nombre', read_only=True)
    class Meta:
        model = Actividad
        fields = ['id', 'tipo', 'tipo_nombre', 'nombre', 'descripcion', 'fecha_asignacion', 'fecha_entrega', 'periodo']
        read_only_fields = ['id']

class NotaSerializer(serializers.ModelSerializer):
    estudiante_nombre = serializers.CharField(source='estudiante.user.get_full_name', read_only=True)
    actividad_nombre = serializers.CharField(source='actividad.nombre', read_only=True)

    class Meta:
        model = Nota
        fields = [
            'id', 'estudiante', 'estudiante_nombre', 'actividad', 'actividad_nombre', 'valor', 'observaciones', 'es_recuperacion'
        ]
        read_only_fields = ['id']

class NotaMasivaSerializer(serializers.Serializer):
    actividad_id = serializers.IntegerField()
    notas = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()
        )
    )

    def validate_actividad_id(self, value):
        try:
            return Actividad.objects.get(id=value)
        except Actividad.DoesNotExist:
            raise serializers.ValidationError("La actividad especificada no existe")

    def validate_notas(self, value):
        if not value:
            raise serializers.ValidationError("Debe proporcionar al menos una nota")
        
        for nota in value:
            if 'estudiante_id' not in nota:
                raise serializers.ValidationError("Cada nota debe tener un estudiante_id")
            if 'valor' not in nota:
                raise serializers.ValidationError("Cada nota debe tener un valor")
            try:
                valor = float(nota['valor'])
                if valor < 0 or valor > 10:
                    raise serializers.ValidationError(f"El valor {valor} debe estar entre 0 y 10")
            except ValueError:
                raise serializers.ValidationError(f"El valor {nota['valor']} no es un número válido")
        
        return value

    def create(self, validated_data):
        actividad = validated_data['actividad_id']
        notas_data = validated_data['notas']
        notas_creadas = []
        
        for nota_data in notas_data:
            estudiante = get_object_or_404(Usuario, id=nota_data['estudiante_id'])
            nota, _ = Nota.objects.update_or_create(
                estudiante=estudiante,
                actividad=actividad,
                defaults={
                    'valor': float(nota_data['valor']),
                    'observaciones': nota_data.get('observaciones', ''),
                    'es_recuperacion': nota_data.get('es_recuperacion', False)
                }
            )
            notas_creadas.append(nota)
        
        return notas_creadas


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
        fields = ['id', 'codigo', 'nombre', 'descripcion', 'area_estudio', 'nivel_educativo', 'niveles_especificos', 'horas_semanales']
        read_only_fields = ['id']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nivel', 'paralelo', 'cupo_maximo', 'estado']
        read_only_fields = ['id']

class HorarioSerializer(serializers.ModelSerializer):
    curso_nombre = serializers.CharField(source='curso.nombre_completo', read_only=True)
    asignatura_nombre = serializers.CharField(source='asignatura.nombre', read_only=True)

    class Meta:
        model = Horario
        fields = ['id', 'curso', 'curso_nombre', 'asignatura', 'asignatura_nombre', 'dia', 'hora_inicio', 'hora_fin']
        read_only_fields = ['id']

class MatriculaCursoSerializer(serializers.ModelSerializer):
    estudiante_nombre = serializers.CharField(source='estudiante.user.get_full_name', read_only=True)
    curso_nombre = serializers.CharField(source='curso.nombre_completo', read_only=True)

    class Meta:
        model = MatriculaCurso
        fields = ['id', 'estudiante', 'estudiante_nombre', 'curso', 'curso_nombre', 'fecha_matricula', 'estado']
        read_only_fields = ['id']

class EmptySerializer(serializers.Serializer):
    pass

class LogoutView(APIView):
    serializer_class = EmptySerializer
    ...


