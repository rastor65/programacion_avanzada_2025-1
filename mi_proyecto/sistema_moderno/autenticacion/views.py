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
from rest_framework import generics, permisos, status
from .models import Usuario
from rest_framework_simplejwt.authentication import JWTAuthentication

# Views en clases
class RolListCreateView(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [permisos.IsAuthenticated]



class RolRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [permisos.IsAuthenticated]


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
    permission_classes = [permisos.IsAuthenticated, IsAdminRole]  


# Views IA
# UsuarioListView:
class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]  # Solo administradores pueden ver la lista de usuarios
    
class UsuarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

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

        if user is None:
            return Response({"detail": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        response = Response({
            "message": "Autenticación con cookies exitosa",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        })

        response.set_cookie(key='access_token', value=access_token, httponly=True, secure=False, samesite='Lax', max_age=60 * 60,)
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True, secure=False, samesite='Lax', max_age=60 * 60 * 24,)

        return response
    
# VERIFICACION DE AUTENTICACION
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
        
        return Response({ 
            "message": f" Hola, {validated_user.username}, estas autenticado <3"
        })
    
# CERRAR SESION
class LogoutView(APIView):
    def post(self, request):
        response = Response({"message": "Sesión cerrada correctamente."})

        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        return response



# Create your views here.
