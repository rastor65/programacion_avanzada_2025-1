from rest_framework import generics, permissions
from .models import Pedido
from .serializers import PedidoSerializer
from autenticacion.permissions import IsAdminRole, IsUsuarioRole

class CrearPedidoView(generics.CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user.perfil)

class ListaPedidosAdminView(generics.ListAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAdminRole]

class MisPedidosView(generics.ListAPIView):
    serializer_class = PedidoSerializer
    permission_classes = [IsUsuarioRole]

    def get_queryset(self):
        return Pedido.objects.filter(usuario=self.request.user.perfil)
