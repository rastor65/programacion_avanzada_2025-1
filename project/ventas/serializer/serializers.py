from rest_framework import serializers
from ventas.models import ventas

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ventas
        fields = ['id', 'product', 'client', 'total_products', 'amount', 'registered_by', 'date']
        read_only_fields = ['amount', 'date', 'registered_by']  # <- Esto es importante

    def validate(self, data):
        product = data.get('product')
        total_products = data.get('total_products')
        if product and total_products and total_products > product.stock:
            raise serializers.ValidationError("No hay suficiente stock disponible para esta cantidad de venta.")
        return data

