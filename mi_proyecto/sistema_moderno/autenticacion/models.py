from django.db import models
from django.contrib.auth.models import User


# TimeStampedModel:
class TimeStampedModel(models.Model):
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en=models.DateTimeField(auto_now=True)

    class Meta:
        abstract= True


# Rol:
class Rol(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.nombre


# Usuario:
class Usuario(TimeStampedModel): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True)

    nombres = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)


# UsuarioRol:

class UsuarioRol(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    asignado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'rol')
# Create your models here.
