from django.shortcuts import render
from .models import Pedido, DetallePedido
from productos.models import Perfume
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def hacer_pedido(request):
    if request.method == 'POST':
        perfume = Perfume.objects.first()  # solo como ejemplo
        pedido = Pedido.objects.create(cliente=request.user, fecha=timezone.now())
        DetallePedido.objects.create(
            pedido=pedido,
            perfume=perfume,
            cantidad=1,
            subtotal=perfume.precio
        )
        return render(request, 'pedidos/pedido_realizado.html', {'pedido': pedido})
    return render(request, 'pedidos/hacer_pedido.html')

# Create your views here.
