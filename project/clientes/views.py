from rest_framework import viewsets
from .serializer.serializers import clienteSerializer
from .models import clientes
from rest_framework.permissions import IsAuthenticated
from autenticacion.permissions import IsSupervisorOrAdmin

class clienteViewSet(viewsets.ModelViewSet):
    queryset = clientes.objects.all()
    serializer_class = clienteSerializer
    permission_classes = [IsAuthenticated, IsSupervisorOrAdmin]

