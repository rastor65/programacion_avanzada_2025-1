from django.urls import path
from . import views

urlpatterns = [
    path('nuevo/', views.hacer_pedido, name='hacer_pedido'),
]
