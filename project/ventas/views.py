from rest_framework import viewsets
from ventas.models import ventas
from ventas.serializer.serializers import VentaSerializer
from rest_framework.permissions import IsAuthenticated
from autenticacion.permissions import IsVendedorOrSupervisorReadOnlyOrAdmin

class VentaCreateView(viewsets.ModelViewSet):
    queryset = ventas.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [IsAuthenticated, IsVendedorOrSupervisorReadOnlyOrAdmin]

    def perform_create(self, serializer):
        perfil = self.request.user.perfil  # Este es el objeto Usuario personalizado
        serializer.save(registered_by=perfil)



