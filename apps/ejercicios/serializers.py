from rest_framework import serializers
from .models import TipoOperacion, NivelDificultad, Ejercicio, SesionPractica

class TipoOperacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOperacion
        fields = '__all__'

class NivelDificultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelDificultad
        fields = '__all__'

class EjercicioSerializer(serializers.ModelSerializer):
    tipo_operacion_nombre = serializers.CharField(source='tipo_operacion.nombre', read_only=True)
    tipo_operacion_simbolo = serializers.CharField(source='tipo_operacion.simbolo', read_only=True)
    nivel_dificultad_nombre = serializers.CharField(source='nivel_dificultad.nombre', read_only=True)
    
    class Meta:
        model = Ejercicio
        fields = ['id', 'tipo_operacion', 'nivel_dificultad', 'operando1', 'operando2', 
                  'resultado_correcto', 'tipo_operacion_nombre', 'tipo_operacion_simbolo', 
                  'nivel_dificultad_nombre']

class SesionPracticaSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.CharField(source='usuario.nombres', read_only=True)
    nivel_dificultad_nombre = serializers.CharField(source='nivel_dificultad.nombre', read_only=True)
    tipo_operacion_nombre = serializers.CharField(source='tipo_operacion.nombre', read_only=True)
    
    class Meta:
        model = SesionPractica
        fields = ['id', 'usuario', 'nivel_dificultad', 'tipo_operacion', 'cantidad_ejercicios',
                  'tiempo_total', 'completada', 'usuario_nombre', 'nivel_dificultad_nombre',
                  'tipo_operacion_nombre', 'creado_en']

class GenerarEjerciciosSerializer(serializers.Serializer):
    nivel_dificultad_id = serializers.IntegerField()
    tipo_operacion_id = serializers.IntegerField(required=False)
    cantidad = serializers.IntegerField(min_value=1, max_value=50, default=10)
