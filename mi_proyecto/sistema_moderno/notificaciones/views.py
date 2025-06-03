from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from autenticacion.permisos import IsAdminRole
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from serializer.serializers import TipoNotificacionSerializer, NotificacionSerializer

# Create your views here 

# Tipos de notificaciones
class TipoNotificacionListCreateView(generics.ListCreateAPIView):
    queryset = TipoNotificacion.objects.all()
    permission_classes = [IsAuthenticated, IsAdminRole]
    serializer_class = TipoNotificacionSerializer

    def get_queryset(self):
        return TipoNotificacion.objects.all().order_by('-prioridad')


# Para Actualizar tipo de notificaciones (editar)
class TipoNotificacionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoNotificacion.objects.all()
    serializer_class = TipoNotificacionSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]



# Notificaciones
class NotificacionListCreateView(generics.ListCreateAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notificacion.objects.filter(usuario=self.request.user.perfil).order_by('-fecha')

    def perform_create(self, serializer):
        # Verificar si el usuario tiene un rol que permite enviar notificaciones
        roles_permitidos = ['Administrador', 'Profesor',]
        user_rol = self.request.user.perfil.rol
        
        if not user_rol or user_rol.nombre not in roles_permitidos:
            raise permissions.PermissionDenied(
                "No tienes permiso para crear notificaciones, lo siento. "
            )
        serializer.save()


# Para Actualizar notificaciones (editar)
class NotificacionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Si es admin o profesor puede ver todas las notificaciones que creó
        roles_permitidos = ['Administrador', 'Profesor']
        user_rol = self.request.user.perfil.rol

        if user_rol and user_rol.nombre in roles_permitidos:
            return Notificacion.objects.filter(usuario=self.request.user.perfil)
        else:
            # Para otros roles (estudiantes, padres), solo pueden ver sus notificaciones recibidas
            return Notificacion.objects.filter(usuario=self.request.user.perfil)


# Para las notificaciones leidas
class MarcarNotificacionLeidaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        notificacion = get_object_or_404(Notificacion, pk=pk, usuario=request.user.perfil)
        notificacion.leido = True
        notificacion.save()
        return Response({'status': 'Notificación marcada como leida'}, status=status.HTTP_200_OK)



# Para marcar todas las notificaciones como leidas
class MarcarTodasLeidasView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Notificacion.objects.filter(
            usuario=request.user.perfil,
            leido=False
        ).update(leido=True)
        return Response({'status': 'Todas las notificaciones marcadas como leidas'}, status=status.HTTP_200_OK)
