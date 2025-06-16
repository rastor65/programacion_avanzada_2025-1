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
        else:
            # Si ya existe el perfil, actualizamos los datos básicos para mantener sincronización
            perfil = instance.perfil
            actualizacion_necesaria = False
            
            # Sincronizar nombres
            if perfil.nombres != instance.first_name and instance.first_name:
                perfil.nombres = instance.first_name
                actualizacion_necesaria = True
            
            # Sincronizar apellidos
            if perfil.apellidos != instance.last_name and instance.last_name:
                perfil.apellidos = instance.last_name
                actualizacion_necesaria = True
                
            # Sincronizar email
            if perfil.email != instance.email and instance.email:
                perfil.email = instance.email
                actualizacion_necesaria = True
                
            # Si el usuario es superuser o staff, debe tener rol admin
            if (instance.is_superuser or instance.is_staff) and perfil.rol != 'admin':
                perfil.rol = 'admin'
                actualizacion_necesaria = True
                
            if actualizacion_necesaria:
                perfil.save()
                print(f"Perfil actualizado para el usuario {instance.username}")
            
    except Exception as e:
        print(f"Error al gestionar perfil de usuario ({instance.username}): {e}") 