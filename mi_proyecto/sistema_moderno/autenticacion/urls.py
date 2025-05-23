from django.urls import path
from .views import *

urlpatterns = [
    path('roles/', RolListCreateView.as_view(), name='rol_list_create'),
    path('roles/<int:pk>/', RolRetrieveUpdateDestroyView.as_view(), name='rol_detail'),

]