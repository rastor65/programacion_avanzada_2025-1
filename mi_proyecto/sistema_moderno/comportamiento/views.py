from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count, Q
from .models import *
from serializer.serializers import *
from autenticacion.models import Usuario

class TipoFaltaListCreateView(generics.ListCreateAPIView):
    queryset = TipoFalta.objects.all()
    serializer_class = TipoFaltaSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegistroComportamientoListCreateView(generics.ListCreateAPIView):
    serializer_class = RegistroComportamientoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil'):
            if self.request.user.perfil.rol.nombre == 'Estudiante':
                return RegistroComportamiento.objects.filter(estudiante=self.request.user.perfil)
            else:
                queryset = RegistroComportamiento.objects.all()
                # Filtros opcionales
                periodo_id = self.request.query_params.get('periodo', None)
                estudiante_id = self.request.query_params.get('estudiante', None)
                tipo = self.request.query_params.get('tipo', None)
                nivel_falta = self.request.query_params.get('nivel_falta', None)

                if periodo_id:
                    queryset = queryset.filter(periodo_id=periodo_id)
                if estudiante_id:
                    queryset = queryset.filter(estudiante_id=estudiante_id)
                if tipo:
                    queryset = queryset.filter(tipo=tipo)
                if nivel_falta:
                    queryset = queryset.filter(tipo_falta__nivel=nivel_falta)

                return queryset
        return RegistroComportamiento.objects.none()

    def perform_create(self, serializer):
        serializer.save(registrado_por=self.request.user.perfil)

class CompromisoListCreateView(generics.ListCreateAPIView):
    serializer_class = CompromisoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil'):
            if self.request.user.perfil.rol.nombre == 'Estudiante':
                return Compromiso.objects.filter(registro__estudiante=self.request.user.perfil)
            else:
                queryset = Compromiso.objects.all()
                # Filtros opcionales
                estado = self.request.query_params.get('estado', None)
                estudiante_id = self.request.query_params.get('estudiante', None)

                if estado:
                    queryset = queryset.filter(estado=estado)
                if estudiante_id:
                    queryset = queryset.filter(registro__estudiante_id=estudiante_id)

                return queryset
        return Compromiso.objects.none()

class ResumenComportamientoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, estudiante_id=None, periodo_id=None):
        # Si no se especifica estudiante_id y el usuario es estudiante, usa su ID
        if estudiante_id is None and hasattr(request.user, 'perfil') and request.user.perfil.rol.nombre == 'Estudiante':
            estudiante_id = request.user.perfil.id
        
        # Si aún no hay estudiante_id o periodo_id, error
        if estudiante_id is None:
            return Response(
                {'error': 'Debe especificar el estudiante'},
                status=status.HTTP_400_BAD_REQUEST
            )

        estudiante = get_object_or_404(Usuario, id=estudiante_id)
        
        # Filtrar por período si se especifica
        registros = RegistroComportamiento.objects.filter(estudiante=estudiante)
        if periodo_id:
            registros = registros.filter(periodo_id=periodo_id)

        # Conteo de observaciones por tipo
        resumen_observaciones = {
            'positivas': registros.filter(tipo='POSITIVO').count(),
            'negativas': registros.filter(tipo='NEGATIVO').count()
        }

        # Conteo de faltas por nivel
        resumen_faltas = registros.filter(
            tipo='NEGATIVO'
        ).values(
            'tipo_falta__nivel'
        ).annotate(
            total=Count('id')
        )

        # Estado de compromisos
        compromisos = Compromiso.objects.filter(
            registro__estudiante=estudiante
        )
        if periodo_id:
            compromisos = compromisos.filter(registro__periodo_id=periodo_id)

        resumen_compromisos = compromisos.values(
            'estado'
        ).annotate(
            total=Count('id')
        )

        data = {
            'estudiante': f"{estudiante.nombres} {estudiante.apellidos}",
            'observaciones': resumen_observaciones,
            'faltas_por_nivel': {
                item['tipo_falta__nivel']: item['total'] 
                for item in resumen_faltas
            },
            'estado_compromisos': {
                item['estado']: item['total'] 
                for item in resumen_compromisos
            }
        }
        
        return Response(data)
