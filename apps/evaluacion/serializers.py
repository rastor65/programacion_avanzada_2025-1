from rest_framework import serializers
from .models import Respuesta, ResultadoSesion, Estadistica
from apps.ejercicios.models import Ejercicio, SesionPractica

class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = ['id', 'ejercicio', 'sesion', 'usuario', 'respuesta_usuario', 
                  'es_correcta', 'tiempo_respuesta']
        read_only_fields = ['es_correcta']
    
    def create(self, validated_data):
        ejercicio = validated_data['ejercicio']
        respuesta_usuario = validated_data['respuesta_usuario']
        
        # Verificar si la respuesta es correcta (con margen de error para decimales)
        es_correcta = abs(ejercicio.resultado_correcto - respuesta_usuario) < 0.01
        
        # Crear la respuesta con el resultado de la verificación
        respuesta = Respuesta.objects.create(
            **validated_data,
            es_correcta=es_correcta
        )
        
        return respuesta

class ResultadoSesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoSesion
        fields = ['id', 'sesion', 'usuario', 'total_ejercicios', 'ejercicios_correctos',
                  'porcentaje_acierto', 'tiempo_promedio_respuesta']
        read_only_fields = ['total_ejercicios', 'ejercicios_correctos', 
                           'porcentaje_acierto', 'tiempo_promedio_respuesta']

class EstadisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadistica
        fields = ['id', 'usuario', 'total_sesiones', 'total_ejercicios', 
                  'ejercicios_correctos', 'porcentaje_acierto_global', 
                  'tiempo_promedio_global']
        read_only_fields = ['total_sesiones', 'total_ejercicios', 'ejercicios_correctos',
                           'porcentaje_acierto_global', 'tiempo_promedio_global']

class FinalizarSesionSerializer(serializers.Serializer):
    sesion_id = serializers.IntegerField()
    tiempo_total = serializers.IntegerField()
