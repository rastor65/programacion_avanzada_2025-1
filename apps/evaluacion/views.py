from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg, Count, Sum, F
from .models import Respuesta, ResultadoSesion, Estadistica
from .serializers import (
    RespuestaSerializer, ResultadoSesionSerializer,
    EstadisticaSerializer, FinalizarSesionSerializer
)
from apps.ejercicios.models import SesionPractica
from apps.autenticacion.models import Usuario

class RespuestaViewSet(viewsets.ModelViewSet):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        usuario = Usuario.objects.get(user=self.request.user)
        return Respuesta.objects.filter(usuario=usuario)
    
    def perform_create(self, serializer):
        usuario = Usuario.objects.get(user=self.request.user)
        serializer.save(usuario=usuario)

class FinalizarSesionView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = FinalizarSesionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        sesion_id = serializer.validated_data['sesion_id']
        tiempo_total = serializer.validated_data['tiempo_total']
        
        try:
            usuario = Usuario.objects.get(user=request.user)
            sesion = SesionPractica.objects.get(pk=sesion_id, usuario=usuario)
        except (Usuario.DoesNotExist, SesionPractica.DoesNotExist):
            return Response({"error": "Sesión no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        # Actualizar la sesión como completada y guardar el tiempo total
        sesion.completada = True
        sesion.tiempo_total = tiempo_total
        sesion.save()
        
        # Calcular resultados
        respuestas = Respuesta.objects.filter(sesion=sesion)
        total_ejercicios = respuestas.count()
        
        if total_ejercicios == 0:
            return Response({"error": "No hay respuestas registradas para esta sesión"}, 
                           status=status.HTTP_400_BAD_REQUEST)
        
        ejercicios_correctos = respuestas.filter(es_correcta=True).count()
        porcentaje_acierto = (ejercicios_correctos / total_ejercicios) * 100
        tiempo_promedio = respuestas.aggregate(promedio=Avg('tiempo_respuesta'))['promedio'] or 0
        
        # Crear o actualizar el resultado de la sesión
        resultado, created = ResultadoSesion.objects.update_or_create(
            sesion=sesion,
            usuario=usuario,
            defaults={
                'total_ejercicios': total_ejercicios,
                'ejercicios_correctos': ejercicios_correctos,
                'porcentaje_acierto': porcentaje_acierto,
                'tiempo_promedio_respuesta': tiempo_promedio
            }
        )
        
        # Actualizar estadísticas globales del usuario
        estadistica, created = Estadistica.objects.get_or_create(usuario=usuario)
        
        # Recalcular estadísticas
        todas_sesiones = SesionPractica.objects.filter(usuario=usuario, completada=True)
        todas_respuestas = Respuesta.objects.filter(usuario=usuario)
        
        estadistica.total_sesiones = todas_sesiones.count()
        estadistica.total_ejercicios = todas_respuestas.count()
        estadistica.ejercicios_correctos = todas_respuestas.filter(es_correcta=True).count()
        
        if estadistica.total_ejercicios > 0:
            estadistica.porcentaje_acierto_global = (estadistica.ejercicios_correctos / estadistica.total_ejercicios) * 100
            estadistica.tiempo_promedio_global = todas_respuestas.aggregate(promedio=Avg('tiempo_respuesta'))['promedio'] or 0
        
        estadistica.save()
        
        # Devolver resultados
        return Response({
            "mensaje": "Sesión finalizada correctamente",
            "resultado": ResultadoSesionSerializer(resultado).data,
            "estadisticas": EstadisticaSerializer(estadistica).data
        })

class ResultadoSesionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ResultadoSesion.objects.all()
    serializer_class = ResultadoSesionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        usuario = Usuario.objects.get(user=self.request.user)
        return ResultadoSesion.objects.filter(usuario=usuario)

class EstadisticaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Estadistica.objects.all()
    serializer_class = EstadisticaSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        usuario = Usuario.objects.get(user=self.request.user)
        return Estadistica.objects.filter(usuario=usuario)
