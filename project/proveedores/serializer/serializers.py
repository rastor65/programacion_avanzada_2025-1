from rest_framework import serializers
from proveedores.models import proveedores

class proveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = proveedores
        fields = '__all__'