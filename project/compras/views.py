from rest_framework import viewsets
from compras.serializer.serializers import compraSerializer
from .models import compras
from rest_framework.permissions import IsAuthenticated
from autenticacion.permissions import IsCompradorOrSupervisorReadOnlyOrAdmin

class CompraCreateView(viewsets.ModelViewSet):
    queryset = compras.objects.all()
    serializer_class = compraSerializer
    permission_classes = [IsAuthenticated, IsCompradorOrSupervisorReadOnlyOrAdmin]

    def perform_create(self, serializer):
        perfil = self.request.user.perfil
        serializer.save(registered_by=perfil)

