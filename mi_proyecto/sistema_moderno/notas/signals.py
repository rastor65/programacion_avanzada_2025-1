from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Nota
from notificaciones.models import Notificacion

@receiver(post_save, sender=Nota)
def crear_notificacion_nota(sender, instance, created, **kwargs):
    """
    Crea una notificación automática cuando se crea o actualiza una nota.
    """
    accion = "creada" if created else "actualizada"
    
    # Crear notificación para el estudiante
    Notificacion.objects.create(
        usuario=instance.estudiante,
        titulo=f"Nueva nota {accion}",
        mensaje=f"Se ha {accion} una nota en la actividad {instance.actividad.nombre}. " \
                f"Valor: {instance.valor}",
        tipo="nota"
    )
    
    # Si hay observaciones, crear una notificación adicional
    if instance.observaciones:
        Notificacion.objects.create(
            usuario=instance.estudiante,
            titulo=f"Observaciones en nota de {instance.actividad.nombre}",
            mensaje=instance.observaciones,
            tipo="observacion"
        ) 