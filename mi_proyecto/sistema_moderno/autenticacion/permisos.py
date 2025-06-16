from rest_framework.permissions import BasePermission
from django.core.cache import cache
from django.conf import settings
from django.db import connection
from .models import Usuario

class IsAdminRole(BasePermission):
    """
    Permiso que verifica si un usuario tiene rol de administrador.
    También permite el acceso a superusers y staff.
    """

    def has_permission(self, request, view):
        # Verificar si el usuario está autenticado
        if not request.user.is_authenticated:
            return False
            
        # Los superusers y staff siempre tienen permiso
        if request.user.is_superuser or request.user.is_staff:
            return True
            
        # Para usuarios normales, verificamos el rol en el perfil
        # Implementamos consulta directa para evitar problemas de caché
        try:
            # Consultar directamente el rol del usuario
            usuario = Usuario.objects.get(user=request.user)
            return usuario.rol == 'admin'
        except Usuario.DoesNotExist:
            return False
        except Exception as e:
            print(f"Error al verificar permisos: {e}")
            return False


class IsProfesorRole(BasePermission):
    """
    Permiso que verifica si un usuario tiene rol de profesor.
    También permite el acceso a administradores.
    """
    
    def has_permission(self, request, view):
        # Verificar si el usuario está autenticado
        if not request.user.is_authenticated:
            return False
            
        # Los administradores tienen todos los permisos
        if request.user.is_superuser or request.user.is_staff:
            return True
            
        try:
            # Consultar directamente el rol del usuario
            usuario = Usuario.objects.get(user=request.user)
            return usuario.rol in ['admin', 'profesor']
        except Usuario.DoesNotExist:
            return False
        except Exception as e:
            print(f"Error al verificar permisos: {e}")
            return False


class IsEstudianteRole(BasePermission):
    """
    Permiso que verifica si un usuario tiene rol de estudiante.
    """
    
    def has_permission(self, request, view):
        # Verificar si el usuario está autenticado
        if not request.user.is_authenticated:
            return False
            
        try:
            # Consultar directamente el rol del usuario
            usuario = Usuario.objects.get(user=request.user)
            return usuario.rol == 'estudiante'
        except Usuario.DoesNotExist:
            return False
        except Exception as e:
            print(f"Error al verificar permisos: {e}")
            return False
