from rest_framework import serializers
from productos.models import categorias, productos

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categorias
        fields = '__all__'

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = productos
        fields = '__all__'