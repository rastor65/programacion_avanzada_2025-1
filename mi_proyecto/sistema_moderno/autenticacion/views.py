from rest_framework import generics
from serializer.serializers import *

class RolListCreateView(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializers_class = RolSerializer

class RolRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializers_class = RolSerializer


# Create your views here.
