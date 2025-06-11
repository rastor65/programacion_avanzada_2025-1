from serializer.serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from django.contrib.auth import authenticate
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
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import make_password





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
class LogoutView(generics.GenericAPIView):

    def post(self, request):
        response = Response({"message": "Sesión cerrada correctamente."})
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response


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
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/')  # Redirige al dashboard o página principal
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'autenticacion/login.html', {'form': form})

# Vista para registro con template y roles dinámicos
@csrf_protect
def register_view(request):
    roles = Rol.objects.all()
    context = {'roles': roles, 'form': {}}
    if request.method == 'POST':
        nombres = request.POST.get('nombres', '').strip()
        email = request.POST.get('email', '').strip()
        rol_id = request.POST.get('rol', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        accept_terms = request.POST.get('acceptTerms', None)
        errores = {}

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

        # Crear usuario y perfil
        user = User.objects.create(
            username=email,
            email=email,
            password=make_password(password1),
            first_name=nombres.split()[0],
            last_name=' '.join(nombres.split()[1:]) if len(nombres.split()) > 1 else ''
        )
        rol = Rol.objects.get(id=rol_id)
        usuario = Usuario.objects.create(
            user=user,
            rol=rol,
            nombres=nombres,
            apellidos=' '.join(nombres.split()[1:]) if len(nombres.split()) > 1 else '',
        )
        # Mensaje de éxito y redirección
        messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
        return redirect('login')
    return render(request, 'autenticacion/register.html', context)
