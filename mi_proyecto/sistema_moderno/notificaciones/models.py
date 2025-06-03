from django.db import models
from autenticacion.models import *


# Create your models here.
class TipoNotificacion(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    mensaje = models.TextField(verbose_name="Mensaje")
    prioridad = models.CharField(
        max_length=30,
        choices=[
            ('BAJA', 'Baja'),
            ('MEDIA', 'Media'),
            ('ALTA', 'Alta'),
            ('URGENTE', 'Urgente')
        ],
        default='MEDIA',
        verbose_name="Prioridad"
    )

    class Meta:
        verbose_name = "Tipo de Notificación"
        verbose_name_plural = "Tipos de Notificaciones"
        ordering = ['-prioridad']

    def __str__(self):
        return f"{self.nombre} ({self.get_prioridad_display()})"



class Notificacion(TimeStampedModel):
    usuario = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        related_name='notificaciones',
        verbose_name="Usuario"
    )
    tipo = models.ForeignKey(
        TipoNotificacion,
        on_delete=models.PROTECT,
        related_name='notificaciones',
        verbose_name="Tipo de Notificación"
    )
    titulo = models.CharField(max_length=100, verbose_name="Título")
    mensaje = models.TextField(verbose_name="Mensaje")
    leido = models.BooleanField(default=False, verbose_name="¿Leído?")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de envío")

    class Meta:
        verbose_name = "Notificación"
        verbose_name_plural = "Notificaciones"
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.titulo} - {self.usuario} - {self.fecha} - {self.tipo}"
