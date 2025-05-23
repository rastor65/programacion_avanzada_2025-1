from django.db import models
from django.contrib.auth.models import User
from productos.models import Perfume

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.username}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.CASCADE)
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.perfume.nombre} x {self.cantidad}"

# Create your models here.
