from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from serializer.serializers import *
from autenticacion.permisos import IsAdminRole

# Create your views here.


class AsignaturaListCreateView(generics.ListCreateAPIView):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        queryset = Asignatura.objects.all()
        area = self.request.query_params.get('area', None)
        nivel = self.request.query_params.get('nivel', None)
        
        if area:
            queryset = queryset.filter(area_estudio=area)
        if nivel:
            queryset = queryset.filter(niveles_especificos__contains=[nivel])
        return queryset

class AsignaturaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer
    permission_classes = [IsAuthenticated]


# Vistas para Cursos
class CursoListCreateView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Curso.objects.all()
        nivel = self.request.query_params.get('nivel', None)
        
        if nivel:
            queryset = queryset.filter(nivel=nivel)
        return queryset

class CursoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticated]



# Vistas para Horarios
class HorarioListCreateView(generics.ListCreateAPIView):
    serializer_class = HorarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Horario.objects.all()
        curso_id = self.request.query_params.get('curso', None)
        asignatura_id = self.request.query_params.get('asignatura', None)
        dia = self.request.query_params.get('dia', None)
        
        if curso_id:
            queryset = queryset.filter(curso_id=curso_id)
        if asignatura_id:
            queryset = queryset.filter(asignatura_id=asignatura_id)
        if dia:
            queryset = queryset.filter(dia=dia)
            
        return queryset

class HorarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    permission_classes = [IsAuthenticated]

class HorarioPorCursoView(generics.ListAPIView):
    serializer_class = HorarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        curso_id = self.kwargs.get('curso_id')
        return Horario.objects.filter(curso_id=curso_id).select_related('asignatura', 'curso')


# Vistas de Matrículas en Cursos
class MatriculaCursoListCreateView(generics.ListCreateAPIView):
    serializer_class = MatriculaCursoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = MatriculaCurso.objects.all()
        estudiante_id = self.request.query_params.get('estudiante', None)
        curso_id = self.request.query_params.get('curso', None)
        estado = self.request.query_params.get('estado', None)
        
        if estudiante_id:
            queryset = queryset.filter(estudiante_id=estudiante_id)
        if curso_id:
            queryset = queryset.filter(curso_id=curso_id)
        if estado:
            queryset = queryset.filter(estado=estado)
            
        return queryset

class MatriculaCursoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MatriculaCurso.objects.all()
    serializer_class = MatriculaCursoSerializer
    permission_classes = [IsAuthenticated]

class MatriculasPorEstudianteView(generics.ListAPIView):
    serializer_class = MatriculaCursoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        estudiante_id = self.kwargs['estudiante_id']
        return MatriculaCurso.objects.filter(
            estudiante_id=estudiante_id,
            estado='ACTIVO'
        )
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream


# Vistas de Asignaturas en Cursos
class AsignaturaCursoListCreateView(generics.ListCreateAPIView):
    serializer_class = AsignaturaCursoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = AsignaturaCurso.objects.all()
        curso_id = self.request.query_params.get('curso', None)
        asignatura_id = self.request.query_params.get('asignatura', None)
        
        if curso_id:
            queryset = queryset.filter(curso_id=curso_id)
        if asignatura_id:
            queryset = queryset.filter(asignatura_id=asignatura_id)
            
        return queryset

class AsignaturaCursoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AsignaturaCurso.objects.all()
    serializer_class = AsignaturaCursoSerializer
    permission_classes = [IsAuthenticated]
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
