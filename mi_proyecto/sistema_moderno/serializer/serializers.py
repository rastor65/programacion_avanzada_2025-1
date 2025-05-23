from rest_framework import serializers
from django.contrib.auth.models import User
from autenticacion.models import *

class RolSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre']


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rol
        fields= ['id', 'nombre', 'descripcion']
