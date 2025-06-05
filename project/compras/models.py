from django.db import models
from productos.models import productos
from proveedores.models import proveedores
from autenticacion.models import Usuario

class compras(models.Model):
    product = models.ForeignKey(productos, on_delete = models.CASCADE)
    supplier = models.ForeignKey(proveedores, on_delete = models.CASCADE)
    total_products = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    registered_by = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.total_products} - by {self.registered_by}"

    def save(self, *args, **kwargs):
        is_new = self._state.adding  # True si es creación nueva

        # Obtener el stock anterior para comparación en caso de edición
        old_total = 0
        if not is_new:
            old_instance = compras.objects.get(pk=self.pk)
            old_total = old_instance.total_products

        if self.product:
            self.supplier = self.product.supplier
            self.amount = self.product.cost_price * self.total_products

        super().save(*args, **kwargs)

        # Calcular diferencia
        diff = self.total_products - old_total
        if diff != 0:
            self.product.stock += diff
            self.product.save()

