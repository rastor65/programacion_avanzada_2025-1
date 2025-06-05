from rest_framework import viewsets
from .serializer.serializers import proveedorSerializer
from .models import proveedores
from rest_framework.permissions import IsAuthenticated
from autenticacion.permissions import IsSupervisorOrAdmin

class proveedorViewSet(viewsets.ModelViewSet):
    queryset = proveedores.objects.all()
    serializer_class = proveedorSerializer
    permission_classes = [IsAuthenticated, IsSupervisorOrAdmin]
