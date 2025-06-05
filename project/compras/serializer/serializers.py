from rest_framework import serializers
from compras.models import compras

class compraSerializer(serializers.ModelSerializer):
    class Meta:
        model = compras
        fields = ['id', 'product', 'total_products', 'amount', 'supplier', 'registered_by', 'date']
        read_only_fields = ['amount', 'supplier', 'registered_by', 'date']