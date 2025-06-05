from django.urls import path, include
from rest_framework import routers
from compras import views

router = routers.DefaultRouter()

router.register(r'compras', views.CompraCreateView)

urlpatterns = [
    path('', include(router.urls))
]