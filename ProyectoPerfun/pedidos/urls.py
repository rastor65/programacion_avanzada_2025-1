from django.urls import path
from .views import CrearPedidoView, ListaPedidosAdminView, MisPedidosView

urlpatterns = [
    path('crear/', CrearPedidoView.as_view(), name='crear_pedido'),
    path('admin/', ListaPedidosAdminView.as_view(), name='lista_pedidos_admin'),
    path('mios/', MisPedidosView.as_view(), name='mis_pedidos'),
]
