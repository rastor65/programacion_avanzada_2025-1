from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import *
from .models import *
from autenticacion.models import Usuario
from django.shortcuts import get_object_or_404
from serializer.serializers import *
from asignaturas.models import PeriodoAcademico  # Importar PeriodoAcademico si es necesario
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from django.db import transaction

# Create your views here.

<<<<<<< Updated upstream
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
=======
>>>>>>> Stashed changes
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
        try:
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
            
            # Verificar permisos
            if request.user.perfil.rol.nombre == 'Estudiante' and request.user.perfil.id != estudiante_id:
                return Response(
                    {'error': 'No tiene permisos para ver este boletín'},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            # Obtener todas las notas del estudiante en el período
            notas = Nota.objects.filter(
                estudiante=estudiante,
                actividad__periodo=periodo
            ).select_related('actividad', 'actividad__tipo')

            # Agrupar notas por tipo de actividad
            tipos_actividad = TipoActividad.objects.all()
            notas_por_tipo = {}
            promedio_periodo = 0
            suma_porcentajes = 0
            total_actividades = 0
            actividades_completadas = 0
            
            for tipo in tipos_actividad:
                notas_tipo = notas.filter(actividad__tipo=tipo)
                if notas_tipo.exists():
                    promedio_tipo = round(notas_tipo.aggregate(Avg('valor'))['valor__avg'], 2)
                    notas_por_tipo[tipo.nombre] = {
                        'promedio': promedio_tipo,
                        'porcentaje': tipo.porcentaje,
                        'notas': NotaSerializer(notas_tipo, many=True).data,
                        'total_actividades': notas_tipo.count(),
                        'recuperaciones': notas_tipo.filter(es_recuperacion=True).count()
                    }
                    promedio_periodo += (promedio_tipo * (tipo.porcentaje / 100))
                    suma_porcentajes += tipo.porcentaje
                    total_actividades += notas_tipo.count()
                    actividades_completadas += notas_tipo.count()

            # Si no hay notas para todos los tipos, ajustar el promedio
            if suma_porcentajes < 100:
                promedio_periodo = (promedio_periodo * 100) / suma_porcentajes if suma_porcentajes > 0 else 0

            # Preparar respuesta
            data = {
                'periodo': PeriodoAcademicoSerializer(periodo).data,
                'estudiante': {
                    'id': estudiante.id,
                    'nombre_completo': f"{estudiante.nombres} {estudiante.apellidos}",
                    'identificacion': estudiante.identificacion
                },
                'notas_por_tipo': notas_por_tipo,
                'promedio_periodo': round(promedio_periodo, 2),
                'porcentaje_evaluado': round(suma_porcentajes, 2),
                'estadisticas': {
                    'total_actividades': total_actividades,
                    'actividades_completadas': actividades_completadas,
                    'actividades_pendientes': total_actividades - actividades_completadas,
                    'recuperaciones_totales': notas.filter(es_recuperacion=True).count()
                }
            }
            
            return Response(data)
            
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class NotaMasivaView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        """
        Crea notas masivamente para todos los estudiantes de una actividad.
        Formato esperado:
        {
            "actividad_id": 1,
            "notas": [
                {"estudiante_id": 1, "valor": 8.5, "observaciones": "Buen trabajo"},
                {"estudiante_id": 2, "valor": 7.0, "observaciones": ""}
            ]
        }
        """
        try:
            actividad_id = request.data.get('actividad_id')
            notas_data = request.data.get('notas', [])
            
            if not actividad_id or not notas_data:
                return Response({
                    'error': 'Se requiere actividad_id y lista de notas'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            actividad = get_object_or_404(Actividad, id=actividad_id)
            notas_creadas = []
            errores = []
            
            # Validar que el usuario tenga permiso para crear notas
            if not request.user.perfil.rol.nombre in ['Profesor', 'Administrador']:
                return Response({
                    'error': 'No tiene permisos para crear notas'
                }, status=status.HTTP_403_FORBIDDEN)
            
            for nota_data in notas_data:
                try:
                    estudiante_id = nota_data.get('estudiante_id')
                    valor = nota_data.get('valor')
                    observaciones = nota_data.get('observaciones', '')
                    
                    if not estudiante_id or valor is None:
                        errores.append(f"Datos incompletos para estudiante {estudiante_id}")
                        continue
                    
                    # Validar que el estudiante existe
                    estudiante = get_object_or_404(Usuario, id=estudiante_id)
                    
                    # Validar que el valor está en el rango correcto
                    if not 0 <= float(valor) <= 10:
                        errores.append(f"Valor de nota inválido para estudiante {estudiante_id}: {valor}")
                        continue
                    
                    # Crear o actualizar la nota
                    nota, created = Nota.objects.update_or_create(
                        estudiante=estudiante,
                        actividad=actividad,
                        defaults={
                            'valor': valor,
                            'observaciones': observaciones
                        }
                    )
                    
                    # Validar la nota antes de guardar
                    nota.full_clean()
                    nota.save()
                    
                    notas_creadas.append(NotaSerializer(nota).data)
                    
                except Exception as e:
                    errores.append(f"Error al procesar nota para estudiante {estudiante_id}: {str(e)}")
            
            response_data = {
                'message': f'Se crearon/actualizaron {len(notas_creadas)} notas exitosamente',
                'notas': notas_creadas
            }
            
            if errores:
                response_data['errores'] = errores
                return Response(response_data, status=status.HTTP_207_MULTI_STATUS)
            
            return Response(response_data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
