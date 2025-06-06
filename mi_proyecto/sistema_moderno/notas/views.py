from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import *
from .models import *
from autenticacion.models import Usuario
from django.shortcuts import get_object_or_404
from serializer.serializers import *

# Create your views here.

# Vistas de Periodo Academico
class PeriodoAcademicoListCreateView(generics.ListCreateAPIView):
    queryset = PeriodoAcademico.objects.all()
    serializer_class = PeriodoAcademicoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = PeriodoAcademico.objects.all()
        año = self.request.query_params.get('año', None)
        activo = self.request.query_params.get('activo', None)
        
        if año is not None:
            queryset = queryset.filter(año_lectivo=año)
        if activo is not None:
            queryset = queryset.filter(activo=activo)
        
        return queryset


# Vistas de Tipo de Actividad
class TipoActividadListCreateView(generics.ListCreateAPIView):
    queryset = TipoActividad.objects.all()
    serializer_class = TipoActividadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Validar que la suma de porcentajes no exceda 100%
        total_actual = TipoActividad.objects.aggregate(
            total=Sum('porcentaje')
        )['total'] or 0
        
        nuevo_porcentaje = float(self.request.data.get('porcentaje', 0))
        if total_actual + nuevo_porcentaje > 100:
            raise serializers.ValidationError(
                "La suma de porcentajes de todos los tipos de actividad no puede exceder 100%"
            )
        
        serializer.save()


# Vistas de Actividades 
class ActividadListCreateView(generics.ListCreateAPIView):
    serializer_class = ActividadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Actividad.objects.all()
        periodo_id = self.request.query_params.get('periodo', None)
        tipo_id = self.request.query_params.get('tipo', None)
        
        if periodo_id:
            queryset = queryset.filter(periodo_id=periodo_id)
        if tipo_id:
            queryset = queryset.filter(tipo_id=tipo_id)
            
        return queryset


# Vistas de Notas
class NotaListCreateView(generics.ListCreateAPIView):
    serializer_class = NotaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil'):
            if self.request.user.perfil.rol.nombre == 'Estudiante':
                return Nota.objects.filter(estudiante=self.request.user.perfil)
            else:
                # Filtros opcionales para profesores/admin
                queryset = Nota.objects.all()
                periodo_id = self.request.query_params.get('periodo', None)
                estudiante_id = self.request.query_params.get('estudiante', None)
                tipo_id = self.request.query_params.get('tipo', None)
                actividad_id = self.request.query_params.get('actividad', None)

                if periodo_id:
                    queryset = queryset.filter(actividad__periodo_id=periodo_id)
                if estudiante_id:
                    queryset = queryset.filter(estudiante_id=estudiante_id)
                if tipo_id:
                    queryset = queryset.filter(actividad__tipo_id=tipo_id)
                if actividad_id:
                    queryset = queryset.filter(actividad_id=actividad_id)
                
                return queryset
        return Nota.objects.none()



class NotaDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotaSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil'):
            if self.request.user.perfil.rol.nombre == 'Estudiante':
                return Nota.objects.filter(estudiante=self.request.user.perfil)
            return Nota.objects.all()
        return Nota.objects.none()


# Falta... 
class BoletinPeriodoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, periodo_id=None, estudiante_id=None):
        # Si no se especifica estudiante_id y el usuario es estudiante, usa su ID
        if estudiante_id is None and hasattr(request.user, 'perfil') and request.user.perfil.rol.nombre == 'Estudiante':
            estudiante_id = request.user.perfil.id
        
        # Si aún no hay estudiante_id o periodo_id, error
        if estudiante_id is None or periodo_id is None:
            return Response(
                {'error': 'Debe especificar estudiante y período'},
                status=status.HTTP_400_BAD_REQUEST
            )

        estudiante = get_object_or_404(Usuario, id=estudiante_id)
        periodo = get_object_or_404(PeriodoAcademico, id=periodo_id)
        
        # Obtener todas las notas del estudiante en el período
        notas = Nota.objects.filter(
            estudiante=estudiante,
            actividad__periodo=periodo
        )

        # Agrupar notas por tipo de actividad
        tipos_actividad = TipoActividad.objects.all()
        notas_por_tipo = {}
        promedio_periodo = 0
        suma_porcentajes = 0
        
        for tipo in tipos_actividad:
            notas_tipo = notas.filter(actividad__tipo=tipo)
            if notas_tipo.exists():
                promedio_tipo = round(notas_tipo.aggregate(Avg('valor'))['valor__avg'], 2)
                notas_por_tipo[tipo.nombre] = {
                    'promedio': promedio_tipo,
                    'porcentaje': tipo.porcentaje,
                    'notas': NotaSerializer(notas_tipo, many=True).data
                }
                promedio_periodo += (promedio_tipo * (tipo.porcentaje / 100))
                suma_porcentajes += tipo.porcentaje

        # Si no hay notas para todos los tipos, ajustar el promedio
        if suma_porcentajes < 100:
            promedio_periodo = (promedio_periodo * 100) / suma_porcentajes if suma_porcentajes > 0 else 0

        # Preparar respuesta
        data = {
            'periodo': PeriodoAcademicoSerializer(periodo).data,
            'estudiante': f"{estudiante.nombres} {estudiante.apellidos}",
            'notas_por_tipo': notas_por_tipo,
            'promedio_periodo': round(promedio_periodo, 2),
            'porcentaje_evaluado': round(suma_porcentajes, 2)
        }
        
        return Response(data)
