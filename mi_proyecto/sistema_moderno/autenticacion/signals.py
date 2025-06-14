from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Usuario

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    """
    Señal que se ejecuta cuando se crea o actualiza un usuario.
    Si el usuario es nuevo, crea su perfil.
    Si el usuario ya existe pero no tiene perfil, lo crea.
    """
    try:
        # Verificamos si el usuario ya tiene perfil
        if not hasattr(instance, 'perfil'):
            # Si el usuario no tiene perfil, creamos uno nuevo
            if instance.is_superuser or instance.is_staff:
                Usuario.objects.create(
                    user=instance,
                    rol='admin',
                    nombres=instance.first_name or instance.username,
                    apellidos=instance.last_name or '',
                    email=instance.email
                )
            else:
                # Por defecto, asignamos rol estudiante
                Usuario.objects.create(
                    user=instance,
                    rol='estudiante',
                    nombres=instance.first_name or instance.username,
                    apellidos=instance.last_name or '',
                    email=instance.email
                )
            print(f"Perfil creado para el usuario {instance.username}")
    except Exception as e:
        print(f"Error al crear perfil de usuario: {e}") 