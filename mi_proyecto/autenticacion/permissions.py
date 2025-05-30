from rest_framework.permissions import BasePermission

class IsAdminRole(BasePermission):
    ADMIN_NAMES = ['administrador', 'admin']

    def has_permission(self, request, view):
        user = request.user
        perfil = getattr(user, 'perfil', None)
        return perfil and perfil.rol and perfil.rol.nombre.lower() in self.ADMIN_NAMES
