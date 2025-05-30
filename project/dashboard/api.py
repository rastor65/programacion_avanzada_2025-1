from .models import *
from rest_framework import viewsets, permissions
from .serializer.serializers import *

class clientsViwSet(viewsets.ModelViewSet):
    queryset = clients.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = clientsSerializer

class suppliersViwSet(viewsets.ModelViewSet):
    queryset = suppliers.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = suppliersSerializer

class productsViwSet(viewsets.ModelViewSet):
    queryset = products.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = productsSerializer