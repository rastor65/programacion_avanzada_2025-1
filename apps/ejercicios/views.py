import random
import time
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import TipoOperacion, NivelDificultad, Ejercicio, SesionPractica
from .serializers import (
    TipoOperacionSerializer, NivelDificultadSerializer,
    EjercicioSerializer, SesionPracticaSerializer,
    GenerarEjerciciosSerializer
)
from apps.autenticacion.models import Usuario

class TipoOperacionViewSet(viewsets.ModelViewSet):
    queryset = TipoOperacion.objects.all()
    serializer_class = TipoOperacionSerializer
    permission_classes = [IsAuthenticated]

class NivelDificultadViewSet(viewsets.ModelViewSet):
    queryset = NivelDificultad.objects.all()
    serializer_class = NivelDificultadSerializer
    permission_classes = [IsAuthenticated]

class GenerarEjerciciosView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = GenerarEjerciciosSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        nivel_id = serializer.validated_data['nivel_dificultad_id']
        tipo_id = serializer.validated_data.get('tipo_operacion_id')
        cantidad = serializer.validated_data['cantidad']
        
        try:
            nivel = NivelDificultad.objects.get(pk=nivel_id)
            tipo = None if tipo_id is None else TipoOperacion.objects.get(pk=tipo_id)
        except (NivelDificultad.DoesNotExist, TipoOperacion.DoesNotExist):
            return Response({"error": "Nivel de dificultad o tipo de operación no encontrado"}, 
                            status=status.HTTP_404_NOT_FOUND)
        
        # Crear sesión de práctica
        usuario = Usuario.objects.get(user=request.user)
        sesion = SesionPractica.objects.create(
            usuario=usuario,
            nivel_dificultad=nivel,
            tipo_operacion=tipo,
            cantidad_ejercicios=cantidad
        )
        
        # Generar ejercicios
        ejercicios = []
        tipos_operacion = [tipo] if tipo else TipoOperacion.objects.all()
        
        for _ in range(cantidad):
            tipo_op = tipo if tipo else random.choice(tipos_operacion)
            operando1 = random.randint(nivel.rango_min, nivel.rango_max)
            operando2 = random.randint(nivel.rango_min, nivel.rango_max)
            
            # Asegurar que en divisiones no haya divisor 0
            if tipo_op.simbolo == '/' and operando2 == 0:
                operando2 = 1
            
            # Calcular resultado según operación
            if tipo_op.simbolo == '+':
                resultado = operando1 + operando2
            elif tipo_op.simbolo == '-':
                resultado = operando1 - operando2
            elif tipo_op.simbolo == '*':
                resultado = operando1 * operando2
            elif tipo_op.simbolo == '/':
                # Redondear a 2 decimales para divisiones
                resultado = round(operando1 / operando2, 2)
            
            ejercicio = Ejercicio.objects.create(
                tipo_operacion=tipo_op,
                nivel_dificultad=nivel,
                operando1=operando1,
                operando2=operando2,
                resultado_correcto=resultado
            )
            ejercicios.append(ejercicio)
        
        serializer = EjercicioSerializer(ejercicios, many=True)
        return Response({
            "sesion_id": sesion.id,
            "ejercicios": serializer.data
        })

class SesionPracticaViewSet(viewsets.ModelViewSet):
    queryset = SesionPractica.objects.all()
    serializer_class = SesionPracticaSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        usuario = Usuario.objects.get(user=self.request.user)
        return SesionPractica.objects.filter(usuario=usuario)
