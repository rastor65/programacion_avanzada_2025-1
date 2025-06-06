from rest_framework import serializers
from .models import Pedido, PedidoProducto

class PedidoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoProducto
        fields = ['producto', 'cantidad']

class PedidoSerializer(serializers.ModelSerializer):
    items = PedidoProductoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'fecha', 'entregado', 'items']
        read_only_fields = ['usuario', 'fecha', 'entregado']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        usuario = self.context['request'].user.perfil
        pedido = Pedido.objects.create(usuario=usuario)
        for item in items_data:
            PedidoProducto.objects.create(pedido=pedido, **item)
        return pedido

