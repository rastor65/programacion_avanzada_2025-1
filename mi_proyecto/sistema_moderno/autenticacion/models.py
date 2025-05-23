from django.db import models
from django.contrib.auth.models import User

class TimeStampedModel(models.Model):
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en=models.DateTimeField(auto_now=True)

    class Meta:
        abstract= True

class Rol(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.nombre


# Create your models here.
