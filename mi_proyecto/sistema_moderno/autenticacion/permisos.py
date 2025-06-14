from rest_framework.permissions import BasePermission

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
        try:
            return hasattr(request.user, 'perfil') and request.user.perfil.rol == 'admin'
        except:
            return False
