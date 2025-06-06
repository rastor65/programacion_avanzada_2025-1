from django.db import models
from autenticacion.models import Usuario
from productos.models import Perfume

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario}"

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad}"

