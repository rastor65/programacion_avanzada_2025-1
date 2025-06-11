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
from asignaturas.models import MatriculaCurso

class AsistenciaListCreateView(generics.ListCreateAPIView):
    serializer_class = AsistenciaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Asistencia.objects.all()
        
        # Filtrar por matrícula
        matricula_id = self.request.query_params.get('matricula', None)
        if matricula_id:
            queryset = queryset.filter(matricula_id=matricula_id)
        
        # Filtrar por curso
        curso_id = self.request.query_params.get('curso', None)
        if curso_id:
            queryset = queryset.filter(matricula__curso_id=curso_id)
            
        # Filtrar por fecha
        fecha = self.request.query_params.get('fecha', None)
        if fecha:
            queryset = queryset.filter(fecha=fecha)
            
        # Filtrar por estado
        estado = self.request.query_params.get('estado', None)
        if estado:
            queryset = queryset.filter(estado=estado)
            
        return queryset

    def create(self, request, *args, **kwargs):
        # Si se proporciona un curso_id, crear asistencias para todos los estudiantes matriculados
        curso_id = request.data.get('curso_id', None)
        if curso_id:
            matriculas = MatriculaCurso.objects.filter(
                curso_id=curso_id,
                estado='ACTIVO'
            )
            
            asistencias = []
            fecha = request.data.get('fecha', timezone.now().date())
            hora = request.data.get('hora', timezone.now().time())
            
            for matricula in matriculas:
                asistencia = Asistencia(
                    matricula=matricula,
                    fecha=fecha,
                    hora=hora,
                    estado='AUSENTE'  # Por defecto todos están ausentes hasta que se marque lo contrario
                )
                asistencias.append(asistencia)
            
            Asistencia.objects.bulk_create(asistencias)
            
            serializer = AsistenciaListSerializer(asistencias, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return super().create(request, *args, **kwargs)

class AsistenciaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer
    permission_classes = [IsAuthenticated]

class AsistenciasPorCursoView(generics.ListAPIView):
    serializer_class = AsistenciaListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        curso_id = self.kwargs['curso_id']
        fecha = self.request.query_params.get('fecha', timezone.now().date())
        
        return Asistencia.objects.filter(
            matricula__curso_id=curso_id,
            fecha=fecha
        ).order_by('matricula__estudiante__apellidos', 'matricula__estudiante__nombres')

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

class AsistenciaMasivaAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AsistenciaMasivaSerializer(data=request.data)
        if serializer.is_valid():
            asistencias = serializer.save()
            return Response({'message': f'Se crearon/actualizaron {len(asistencias)} asistencias exitosamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
