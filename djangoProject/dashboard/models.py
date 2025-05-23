from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proveedores(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    nombre_contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, unique=True)
    correo = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)    

class Productos(models.Model):
    categoria = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio_entrada = models.DecimalField(max_digits=10, decimal_places=2)
    precio_salida = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_de_ingreso = models.DateTimeField(auto_now_add=True)
    id_proveedor = models.ForeignKey(Proveedores, null=True, on_delete=models.SET_NULL)
    estado = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, unique=True)
    correo = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)