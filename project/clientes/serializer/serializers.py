from rest_framework import serializers
from clientes.models import clientes

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = clientes
        fields = '__all__'