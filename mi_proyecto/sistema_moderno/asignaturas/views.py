from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Asignatura, Curso, Horario
from serializer.serializers import (
    AsignaturaSerializer, CursoSerializer,
    HorarioSerializer, CursoDetalladoSerializer
)

# Create your views here.


class AsignaturaListCreateView(generics.ListCreateAPIView):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer
    permission_classes = [IsAuthenticated]

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
        asignatura_id = self.request.query_params.get('asignatura', None)
        if asignatura_id is not None:
            queryset = queryset.filter(asignatura_id=asignatura_id)
        return queryset

class CursoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticated]

class CursoDetalladoView(generics.RetrieveAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoDetalladoSerializer
    permission_classes = [IsAuthenticated]

# Vistas para Horarios
class HorarioListCreateView(generics.ListCreateAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Horario.objects.all()
        curso_id = self.request.query_params.get('curso', None)
        dia = self.request.query_params.get('dia', None)
        
        if curso_id is not None:
            queryset = queryset.filter(curso_id=curso_id)
        if dia is not None:
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
        curso_id = self.kwargs['curso_id']
        return Horario.objects.filter(curso_id=curso_id)
