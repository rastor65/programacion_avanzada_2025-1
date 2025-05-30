from rest_framework import serializers
from django.contrib.auth.models import User
from autenticacion.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Serializers en Clase
class RolSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre']


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
        fields = ['id', 'nombres', 'apellidos', 'promedio', 'disponibilidad','rol_id', 'rol_nombre',  'roles']

    def get_roles(self, obj):
        from autenticacion.models import UsuarioRol # evita import circular
        asignaciones = UsuarioRol.objects.filter(usuario=obj).select_related('rol')
        return [{'id': ar.rol.id, 'nombre': ar.rol.nombre} for ar in asignaciones]

# RegisterSerializer:

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    emial = serializers.EmailField(write_only=True)

    class Meta:
        models = Usuario
        fields = ['username', 'password', 'email', 'nombres', 'apellidos', 'promedio', 'disponibilidad']

    def create(self, validated_data):

        username = validated_data.pop('username')  
        password = validated_data.pop('password')
        email = validated_data.pop('email')

        user = User.objects.create_user(username=username, password=password, email=email)
        
        try:
            rol_estudiante = Rol.objects.get(nombre__iexact="Usuario")
        except Rol.DoesNotExist:
            raise serializers.ValidationError("El rol 'Usuario' no está configurado en el sistema")
        
        usuario = Usuario.objects.create(
            user=user,
            rol=rol_estudiante,
            **validated_data
        )

        return usuario

# UsuarioRolSerializer:

class UsuarioRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRol
        fields = ['id', 'usuario', 'rol', 'asignado_en']


#LoginSerializer
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


