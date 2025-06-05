from rest_framework import viewsets
from productos.serializer.serializers import categorySerializer, productoSerializer
from .models import categorias, productos
from rest_framework.permissions import IsAuthenticated
from autenticacion.permissions import IsSupervisorOrAdmin

class categoriaViewSet(viewsets.ModelViewSet):
    queryset = categorias.objects.all()
    serializer_class = categorySerializer
    permission_classes = [IsAuthenticated, IsSupervisorOrAdmin]
class productoViewSet(viewsets.ModelViewSet):
    queryset = productos.objects.all()
    serializer_class = productoSerializer
    permission_classes = [IsAuthenticated, IsSupervisorOrAdmin]
