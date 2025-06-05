from django.db import models
from productos.models import productos
from clientes.models import clientes
from autenticacion.models import Usuario

class ventas(models.Model):
    product = models.ForeignKey(productos, on_delete=models.CASCADE)
    client = models.ForeignKey(clientes, on_delete=models.CASCADE)
    total_products = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    registered_by = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.total_products} - by {self.registered_by}"

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        old_total = 0

        if not is_new:
            old_instance = ventas.objects.get(pk=self.pk)
            old_total = old_instance.total_products

        # Calcular diferencia antes de usarla
        diff = self.total_products - old_total

        if self.product:
            self.amount = self.product.sale_price * self.total_products

        # Validación para evitar stock negativo
        if diff > self.product.stock:
            raise ValueError("No hay suficiente stock disponible para esta cantidad de venta.")

        super().save(*args, **kwargs)

        # Ajustar el stock solo si hay diferencia
        if diff != 0:
            self.product.stock -= diff
            self.product.save()




