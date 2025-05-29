from django.db import models

# Modelo de tabla clientes
class clients(models.Model):
# ================= Campos de las entidades ================
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    document_id = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
# ==========================================================

# Modelo para la tabla proveedores
class suppliers(models.Model):
# ================= Campos de las entidades ================
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
# ========================================================== 

# Modelo para la tabla productos 
class products(models.Model):
# ================================= Campos de las entidades =====================================
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    ID_supplier = models.ForeignKey('suppliers', on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
# ===============================================================================================