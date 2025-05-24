from rest_framework import serializers
from django.contrib.auth.models import User
from autenticacion.models import *

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
    roles = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = ['id', 'nombres', 'apellidos', 'promedio', 'disponibilidad', 'roles']

    def get_roles(self, obj):
        asignaciones = UsuarioRol.objects.filter(usuario=obj).select_related('rol')
        return [{'id': r.rol.id, 'nombre': r.rol.nombre} for r in asignaciones]

# RegisterSerializer:

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    emial = serializers.EmailField(write_only=True)

    class Meta:
        models = Usuario
        fields = ['username', 'password', 'email', 'nombres', 'apellidos', 'promedio', 'disponibilidad']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.pop['username'],
            password=validated_data.pop('password'),
            email=validated_data.pop('email')
        )
        rol_estudiante = Rol.objects.get(nombre__iexact='Estudiante')
        usuario = Usuario.objects.create(user=user, rol=rol_estudiante, **validated_data)
        return usuario

# UsuarioRolSerializer:

class UsuarioRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRol
        fields = ['id', 'usuario', 'rol', 'asignado_en']
