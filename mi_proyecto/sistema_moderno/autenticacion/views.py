from rest_framework import generics, status
from serializer.serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .permisos import IsAdminRole
from django.http import JsonResponse 
from rest_framework.views import APIView

# Views en clases
class RolListCreateView(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class RolRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


# Views en la casa
# RegisterView:

class RegisterView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegisterSerializer

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
    permission_classes = [IsAuthenticated, IsAdminRole]  


# Views IA
# UsuarioListView:
class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]  # Solo administradores pueden ver la lista de usuarios

# LogoutView:
class LogoutView(generics.GenericAPIView):

    def post(self, request):
        response = JsonResponse({"mensaje ": "Sesion cerrada correctamente" })
        response.delete_cookie('access_token')
        return response

# LoginCookieView
class CookieLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            response = JsonResponse({"mensaje": "Inicio de sesión exitoso"})
            response.set_cookie('access_token', str(refresh.access_token), httponly=True)
            return response
        else:
            return JsonResponse({"error": "Credenciales inválidas"}, status=401)


# Create your views here.
