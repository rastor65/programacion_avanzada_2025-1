from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from .models import Usuario

class JWTAuthCookieMiddleware:
    """
    Middleware que detecta tokens JWT en cookies y los asigna al encabezado HTTP_AUTHORIZATION
    para que DRF los reconozca automáticamente.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Si la solicitud es para el admin, no interferimos con el sistema de autenticación
        if request.path.startswith('/admin/'):
            return self.get_response(request)
            
        # Intentamos obtener el token de las cookies
        token = request.COOKIES.get('access_token')
        if token:
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {token}'
            
        # Seguir con el flujo normal de la petición
        return self.get_response(request)


class RolMiddleware:
    """
    Middleware para manejar restricciones de acceso basadas en roles.
    Redirige a los usuarios según su rol cuando intentan acceder a áreas restringidas.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Procesar la solicitud solo si el usuario está autenticado
        if request.user.is_authenticated:
            # Verificar si estamos en una ruta protegida
            path = request.path
            
            # No aplicar restricciones a admin/, autenticación o recursos estáticos
            if (path.startswith('/admin/') or 
                path.startswith('/auth/login') or 
                path.startswith('/auth/register') or 
                path.startswith('/static/') or 
                path == '/'):
                return self.get_response(request)
            
            # Obtener el rol actual
            rol = self._get_rol_usuario(request.user)
            
            # Verificar accesos a dashboards específicos
            if path.startswith('/auth/dashboard/admin/') and rol != 'admin':
                messages.error(request, 'No tienes permiso para acceder al panel de administrador')
                return self._redirigir_segun_rol(request, rol)
                
            if path.startswith('/auth/dashboard/profesor/') and rol not in ['admin', 'profesor']:
                messages.error(request, 'No tienes permiso para acceder al panel de profesor')
                return self._redirigir_segun_rol(request, rol)
                
            if path.startswith('/auth/dashboard/estudiante/') and rol != 'estudiante':
                messages.error(request, 'No tienes permiso para acceder al panel de estudiante')
                return self._redirigir_segun_rol(request, rol)
        
        # Continuar con el flujo normal
        return self.get_response(request)
    
    def _get_rol_usuario(self, user):
        """Obtener el rol actual del usuario consultando directamente la base de datos"""
        # Si es superuser o staff, se considera admin
        if user.is_superuser or user.is_staff:
            return 'admin'
            
        try:
            # Consultar directamente el rol del usuario
            usuario = Usuario.objects.get(user=user)
            return usuario.rol
        except Usuario.DoesNotExist:
            return None
        except Exception:
            return None
    
    def _redirigir_segun_rol(self, request, rol):
        """Redirigir al usuario según su rol"""
        if rol == 'admin':
            return redirect('admin_dashboard')
        elif rol == 'profesor':
            return redirect('profesor_dashboard') 
        elif rol == 'estudiante':
            return redirect('estudiante_dashboard')
        else:
            # Si no tiene rol válido, redirigir a login
            messages.error(request, 'Tu cuenta no tiene un rol válido. Por favor contacta al administrador.')
            return redirect('login')