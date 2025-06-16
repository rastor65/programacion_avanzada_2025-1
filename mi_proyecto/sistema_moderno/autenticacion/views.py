from serializer.serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from .permisos import IsAdminRole
from django.http import JsonResponse 
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from .models import Usuario
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from serializer.serializers import UserSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from django.utils import timezone
from datetime import timedelta
import json
from notas.models import Nota
from asignaturas.models import Asignatura, Curso





# Views en clases y en guia de auth
# Roles 
class RolListCreateView(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [permissions.IsAuthenticated]  

class RolRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [permissions.IsAuthenticated]




# Views en la casa
# RegisterView:

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = Usuario.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()
        user = usuario.user

        refresh = RefreshToken.for_user(user)

        return Response (
            {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'nombres': usuario.nombres,
                    'apellidos': usuario.apellidos,
                }
            }
        )
    
# UsuarioRolCreateView:

class UsuarioRolCreateView(generics.ListCreateAPIView):
    queryset = UsuarioRol.objects.all()
    serializer_class = UsuarioRolSerializer
    permission_classes = [permissions.IsAuthenticated]  


# Views IA
# UsuarioListView:
class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]  # Solo administradores pueden ver la lista de usuarios
    
class UsuarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# LogoutView:
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# LoginCookieView
class CookieLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({"detail": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        response = Response({
            "mensaje": "Autenticación con cookies exitosa",
            user: {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        })

        response.set_cookie(key='access_token', value=access_token, httponly=True, secure=True, samesite='Lax', max_age=60 * 60,) # 1 hora
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True, secure=True, samesite='Lax', max_age=60 * 60 * 24,) # 1 día
        return response


# Verificacion de Autenticacion:
class HelloFromCookieView(APIView):
    
    def get(self, request):
        access_token = request.COOKIES.get('access_token')

        if not access_token:
            return Response({"detail": "No se encontró el token en cookies"}, status=401)
        
        
        jwt_authenticator = JWTAuthentication()
        try:
            validated_user, token = jwt_authenticator.authenticate(request._request)
        except Exception as e:
                return Response({"detail": f"Token inválido: {str(e)}"}, status=401)
        
        return Response({"message": f"Hola, {validated_user.user.username}, esta autenticado <3"})

            
            


# Create your views here.

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Usuario.objects.all()
        rol = self.request.query_params.get('rol', None)
        
        if rol:
            queryset = queryset.filter(rol__nombre=rol)
        return queryset

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

# Vista para login con template
@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Intentar autenticar primero con el nombre de usuario
        user = authenticate(request, username=username, password=password)
        
        # Si no funciona, verificar si es un correo electrónico
        if user is None and '@' in username:
            try:
                user_obj = User.objects.get(email=username)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None
        
        if user is not None:
            login(request, user)
            
            # Asegurar que el usuario tenga un perfil
            try:
                # Intentar obtener el perfil directamente de la base de datos
                # esto evita problemas con caché de relaciones
                perfil = Usuario.objects.get(user=user)
            except Usuario.DoesNotExist:
                # Si no tiene perfil, crear uno
                if user.is_superuser or user.is_staff:
                    perfil = Usuario.objects.create(
                        user=user,
                        rol='admin',
                        nombres=user.first_name or user.username,
                        apellidos=user.last_name or '',
                        email=user.email
                    )
                else:
                    perfil = Usuario.objects.create(
                        user=user,
                        rol='estudiante',
                        nombres=user.first_name or user.username,
                        apellidos=user.last_name or '',
                        email=user.email
                    )
                print(f"Perfil creado para el usuario {user.username} durante el login")
            
            # Redirigir según el rol
            if user.is_superuser or user.is_staff:
                return redirect('admin_dashboard')
            elif perfil.rol == 'admin':
                return redirect('admin_dashboard')
            elif perfil.rol == 'profesor':
                return redirect('profesor_dashboard')
            elif perfil.rol == 'estudiante':
                return redirect('estudiante_dashboard')
            else:
                messages.warning(request, 'Usuario sin rol específico asignado, se le ha asignado rol de estudiante por defecto')
                perfil.rol = 'estudiante'
                perfil.save()
                return redirect('estudiante_dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'autenticacion/login.html')

# Vista para registro con template y roles dinámicos
@csrf_protect
def register_view(request):
    # Obtener roles disponibles para el formulario
    roles = list(Rol.objects.all().order_by('id'))
    
    # Para depuración
    print(f"\n=== ROLES DISPONIBLES EN REGISTER VIEW ===")
    print(f"Total de roles: {len(roles)}")
    for rol in roles:
        print(f"ID: {rol.id}, Nombre: '{rol.nombre}', Descripción: '{rol.descripcion}'")
    
    context = {'roles': roles, 'form': {}}
    
    if request.method == 'POST':
        nombres = request.POST.get('nombres', '').strip()
        email = request.POST.get('email', '').strip()
        rol_id = request.POST.get('rol', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        accept_terms = request.POST.get('acceptTerms', None)
        errores = {}

        # Para depuración
        print(f"\n=== DATOS DEL FORMULARIO ===")
        print(f"Nombres: {nombres}")
        print(f"Email: {email}")
        print(f"Rol ID: {rol_id}")
        print(f"Términos aceptados: {accept_terms}")

        # Validaciones
        if not nombres or len(nombres) < 3:
            errores['nombres'] = 'Ingresa tu nombre completo (mínimo 3 caracteres).'
        if not email or '@' not in email:
            errores['email'] = 'Ingresa un correo electrónico válido.'
        if not rol_id:
            errores['rol'] = 'Selecciona tu rol en el colegio.'
        if not password1 or len(password1) < 8:
            errores['password1'] = 'La contraseña debe tener al menos 8 caracteres.'
        if password1 != password2:
            errores['password2'] = 'Las contraseñas no coinciden.'
        if not accept_terms:
            errores['acceptTerms'] = 'Debes aceptar los términos y condiciones.'
        if User.objects.filter(email=email).exists():
            errores['email'] = 'Este correo ya está registrado.'

        if errores:
            context['errores'] = errores
            context['form'] = request.POST
            return render(request, 'autenticacion/register.html', context)

        # Obtener nombre y apellido
        nombres_split = nombres.split()
        first_name = nombres_split[0]
        last_name = ' '.join(nombres_split[1:]) if len(nombres_split) > 1 else ''

        # Crear usuario con nombre de usuario único basado en email
        username = email.split('@')[0]
        # Si ya existe un usuario con ese username, añadir un número
        base_username = username
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1

        # Crear el usuario de Django
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password1),
            first_name=first_name,
            last_name=last_name
        )
        
        # Obtener el rol seleccionado
        rol_nombre = 'estudiante'  # Valor por defecto
        try:
            rol = Rol.objects.get(id=int(rol_id))
            rol_nombre = rol.nombre.lower()
            print(f"Rol encontrado: {rol_nombre}")
        except (ValueError, Rol.DoesNotExist) as e:
            print(f"Error al buscar rol: {e}")
            # Si hay error, usamos el rol por defecto
        
        # Verificar si el usuario ya tiene perfil (creado por la señal)
        try:
            if hasattr(user, 'perfil'):
                # Actualizar el rol en el perfil existente
                user.perfil.rol = rol_nombre
                user.perfil.nombres = first_name
                user.perfil.apellidos = last_name
                user.perfil.email = email
                user.perfil.save()
                print(f"Perfil existente actualizado con rol: {rol_nombre}")
            else:
                # Crear perfil manualmente
                Usuario.objects.create(
                    user=user,
                    rol=rol_nombre,
                    nombres=first_name,
                    apellidos=last_name,
                    email=email
                )
                print(f"Nuevo perfil creado con rol: {rol_nombre}")
        except Exception as e:
            print(f"Error al gestionar perfil: {e}")
            # En caso de error, intentar crear el perfil de todas formas
            try:
                Usuario.objects.create(
            user=user,
                    rol=rol_nombre,
                    nombres=first_name,
                    apellidos=last_name,
                    email=email
                )
                print("Perfil creado en bloque de excepción")
            except Exception as e2:
                print(f"Error crítico al crear perfil: {e2}")
        
        # Mensaje de éxito y redirección
        messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
        return redirect('login')
    
    return render(request, 'autenticacion/register.html', context)

@login_required
def admin_dashboard(request):
    # Comprobar si el usuario es superuser o tiene el rol de administrador
    is_admin = request.user.is_superuser
    if not is_admin and hasattr(request.user, 'perfil'):
        is_admin = request.user.perfil.rol == 'admin'
    
    if not is_admin:
        messages.error(request, 'No tienes permiso para acceder al panel de administrador')
        return redirect('login')
    
    # Estadísticas generales (corregido para evitar errores)
    try:
        total_estudiantes = User.objects.filter(perfil__rol='estudiante').count()
        total_profesores = User.objects.filter(perfil__rol='profesor').count()
        total_cursos = Curso.objects.count()
        
        # Cálculo de porcentajes y tendencias
        mes_anterior = timezone.now() - timedelta(days=30)
        nuevos_profesores = User.objects.filter(perfil__rol='profesor', date_joined__gte=mes_anterior).count()
        
        # Datos para el gráfico de distribución (simulados si la relación no existe)
        estudiantes_data = []
        try:
            grados = Curso.objects.values_list('nivel', flat=True).distinct()
            for grado in grados:
                count = User.objects.filter(perfil__rol='estudiante', perfil__matriculas__curso__nivel=grado).count()
                estudiantes_data.append({
                    "grado": f"{grado}° Grado",
                    "cantidad": count
                })
        except Exception:
            # Datos demo si hay error
            estudiantes_data = [
                {"grado": "1° Grado", "cantidad": 15},
                {"grado": "2° Grado", "cantidad": 20},
                {"grado": "3° Grado", "cantidad": 18}
            ]
        
        # Datos para el gráfico de rendimiento académico
        meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
        rendimiento_data = []
        for i in range(6):
            try:
                mes = timezone.now() - timedelta(days=30*i)
                promedio = Nota.objects.filter(
                    fecha__year=mes.year,
                    fecha__month=mes.month
                ).aggregate(Avg('valor'))['valor__avg'] or 0
                rendimiento_data.append({
                    "mes": meses[i],
                    "promedio": round(promedio, 2)
                })
            except Exception:
                rendimiento_data.append({
                    "mes": meses[i],
                    "promedio": 7.5 # valor demo
                })
        
        # Pagos pendientes (simulado)
        pagos_pendientes = 32
        porcentaje_pagos = 8.3
        
    except Exception as e:
        # Valores por defecto si hay errores
        print(f"Error al obtener estadísticas: {e}")
        total_estudiantes = 0
        total_profesores = 0
        total_cursos = 0
        nuevos_profesores = 0
        estudiantes_data = []
        rendimiento_data = []
        pagos_pendientes = 0
        porcentaje_pagos = 0
    
    context = {
        'total_estudiantes': total_estudiantes,
        'total_profesores': total_profesores,
        'total_cursos': total_cursos,
        'nuevos_profesores': nuevos_profesores,
        'cursos_por_grado': 6,  # Valor fijo por ahora
        'pagos_pendientes': pagos_pendientes,
        'porcentaje_pagos': porcentaje_pagos,
        'estudiantes_data': json.dumps(estudiantes_data),
        'rendimiento_data': json.dumps(rendimiento_data),
        'user': request.user
    }
    
    return render(request, 'dashboard/admin_dashboard.html', context)

@login_required
def profesor_dashboard(request):
    # Comprobar si el usuario tiene rol de profesor
    is_profesor = False
    if hasattr(request.user, 'perfil'):
        is_profesor = request.user.perfil.rol == 'profesor'
    
    if not is_profesor:
        messages.error(request, 'No tienes permiso para acceder al panel de profesor')
        return redirect('login')
    
    # Agregar contexto básico
    context = {
        'user': request.user
    }
    return render(request, 'dashboard/profesor_dashboard.html', context)

@login_required
def estudiante_dashboard(request):
    # Comprobar si el usuario tiene rol de estudiante
    is_estudiante = False
    if hasattr(request.user, 'perfil'):
        is_estudiante = request.user.perfil.rol == 'estudiante'
    
    if not is_estudiante:
        messages.error(request, 'No tienes permiso para acceder al panel de estudiante')
        return redirect('login')
    
    # Agregar contexto básico
    context = {
        'user': request.user
    }
    return render(request, 'dashboard/estudiante_dashboard.html', context)
