from django.db import models
from proveedores.models import proveedores

class categorias(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name

class productos(models.Model):
    category = models.ForeignKey(categorias, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(proveedores, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
