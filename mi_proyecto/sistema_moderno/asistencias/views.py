from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from serializer.serializers import *
from autenticacion.permisos import IsAdminRole
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.utils import timezone

class AsistenciaListCreateView(generics.ListCreateAPIView):
    serializer_class = AsistenciaListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Si es admin o profesor, puede ver todas las asistencias
        roles_permitidos = ['Administrador', 'Profesor']
        user_rol = self.request.user.perfil.rol

        if user_rol and user_rol.nombre in roles_permitidos:
            return Asistencia.objects.all()
        else:
            # Los estudiantes solo ven sus propias asistencias
            return Asistencia.objects.filter(usuario=self.request.user.perfil)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AsistenciaSerializer
        return AsistenciaListSerializer

    def perform_create(self, serializer):
        # Solo profesores y admin pueden crear asistencias
        roles_permitidos = ['Administrador', 'Profesor']
        user_rol = self.request.user.perfil.rol
        
        if not user_rol or user_rol.nombre not in roles_permitidos:
            raise permissions.PermissionDenied(
                "Solo los profesores y admins pueden registrar asistencias."
            )
        serializer.save()

class AsistenciaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Si es admin o profesor, puede ver todas las asistencias
        roles_permitidos = ['Administrador', 'Profesor']
        user_rol = self.request.user.perfil.rol

        if user_rol and user_rol.nombre in roles_permitidos:
            return Asistencia.objects.all()
        else:
            # Los estudiantes solo ven sus propias asistencias
            return Asistencia.objects.filter(usuario=self.request.user.perfil)

class ValidarAsistenciaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Solo profesores y admin pueden validar asistencias
        roles_permitidos = ['Administrador', 'Profesor']
        user_rol = request.user.perfil.rol
        
        if not user_rol or user_rol.nombre not in roles_permitidos:
            raise permissions.PermissionDenied(
                "Solo los profesores y administradores pueden validar asistencias."
            )

        asistencia = get_object_or_404(Asistencia, pk=pk)
        asistencia.validada = True
        asistencia.save()
        return Response({'status': 'Asistencia validada correctamente'}, status=status.HTTP_200_OK)

class RegistrarAsistenciaHoyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Por ahora esta funcionalidad está deshabilitada hasta definir horarios
        return Response(
            {'error': 'Aun no se establecieron los horarios de clase, trabajamos en ello...'},
            status=status.HTTP_400_BAD_REQUEST
        )
        
        # Verificar si ya existe una asistencia para hoy
        asistencia_existente = Asistencia.objects.filter(
            usuario=request.user.perfil,
            fecha=now.date()
        ).exists()

        if asistencia_existente:
            return Response(
                {'error': 'Ya has registrado tu asistencia hoy'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Crear nueva asistencia
        Asistencia.objects.create(
            usuario=request.user.perfil,
            fecha=now.date(),
            hora=now.time(),
            estado='PRESENTE'
        )

        return Response(
            {'status': 'Asistencia registrada correctamente'},
            status=status.HTTP_201_CREATED
        )
