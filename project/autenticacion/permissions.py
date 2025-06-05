from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminRole(BasePermission):
    ADMIN_NAMES = ['administrador', 'admin']
    def has_permission(self, request, view):
        user = request.user
        perfil = getattr(user, 'perfil', None)
        return perfil and perfil.rol and perfil.rol.nombre.lower() in self.ADMIN_NAMES

class IsSupervisorReadOnly(BasePermission):
    SUPERVISOR_NAMES = ['supervisor']

    def has_permission(self, request, view):
        user = request.user
        perfil = getattr(user, 'perfil', None)
        # Permitir solo métodos seguros (GET, HEAD, OPTIONS)
        return (
            perfil and perfil.rol and perfil.rol.nombre.lower() in self.SUPERVISOR_NAMES
            and request.method in SAFE_METHODS
        )

class IsAdminOrSupervisorReadOnly(BasePermission):
    ADMIN_NAMES = ['administrador', 'admin']
    SUPERVISOR_NAMES = ['supervisor']

    def has_permission(self, request, view):
        user = request.user
        perfil = getattr(user, 'perfil', None)

        if not perfil or not perfil.rol:
            return False

        rol_nombre = perfil.rol.nombre.lower()

        if rol_nombre in self.ADMIN_NAMES:
            # Administrador tiene acceso completo
            return True
        elif rol_nombre in self.SUPERVISOR_NAMES:
            # Supervisor solo acceso a métodos seguros
            return request.method in SAFE_METHODS

        return False

class IsCompradorOrSupervisorReadOnlyOrAdmin(BasePermission):
    ADMIN_NAMES = ['administrador', 'admin']
    COMPRADOR_NAMES = ['comprador']
    SUPERVISOR_NAMES = ['supervisor']

    def has_permission(self, request, view):
        user = request.user
        perfil = getattr(user, 'perfil', None)

        if not perfil or not perfil.rol:
            return False

        rol_nombre = perfil.rol.nombre.lower()

        if rol_nombre in self.ADMIN_NAMES:
            # Administrador sin restricciones
            return True
        elif rol_nombre in self.COMPRADOR_NAMES:
            # Comprador acceso completo
            return True
        elif rol_nombre in self.SUPERVISOR_NAMES:
            # Supervisor solo métodos seguros
            return request.method in SAFE_METHODS

        return False


class IsVendedorOrSupervisorReadOnlyOrAdmin(BasePermission):
    ADMIN_NAMES = ['administrador', 'admin']
    VENDEDOR_NAMES = ['vendedor']
    SUPERVISOR_NAMES = ['supervisor']

    def has_permission(self, request, view):
        user = request.user
        perfil = getattr(user, 'perfil', None)

        if not perfil or not perfil.rol:
            return False

        rol_nombre = perfil.rol.nombre.lower()

        if rol_nombre in self.ADMIN_NAMES:
            # Administrador sin restricciones
            return True
        elif rol_nombre in self.VENDEDOR_NAMES:
            # Vendedor acceso completo
            return True
        elif rol_nombre in self.SUPERVISOR_NAMES:
            # Supervisor solo métodos seguros
            return request.method in SAFE_METHODS

        return False

class IsSupervisorOrAdmin(BasePermission):
    ADMIN_NAMES = ['administrador', 'admin']
    SUPERVISOR_NAMES = ['supervisor']

    def has_permission(self, request, view):
        user = request.user
        perfil = getattr(user, 'perfil', None)

        if not perfil or not perfil.rol:
            return False

        rol_nombre = perfil.rol.nombre.lower()

        return rol_nombre in self.ADMIN_NAMES or rol_nombre in self.SUPERVISOR_NAMES

