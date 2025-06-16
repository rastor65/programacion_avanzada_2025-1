#!/usr/bin/env python
"""
Script para verificar los roles existentes en la base de datos.
Ejecutar con: python check_roles.py
"""

import os
import django

# Configuración inicial de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_moderno.settings')
django.setup()

from autenticacion.models import Rol

def check_roles():
    """Verificar los roles existentes en la base de datos"""
    print("Verificando roles en la base de datos...")
    
    # Obtener todos los roles
    roles = Rol.objects.all()
    
    print(f"Total de roles: {roles.count()}")
    
    # Mostrar información detallada de cada rol
    for rol in roles:
        print(f"ID: {rol.id}, Nombre: '{rol.nombre}', Descripción: '{rol.descripcion}'")
    
    return roles.count()

if __name__ == "__main__":
    total_roles = check_roles()
    print(f"\nTotal de roles en el sistema: {total_roles}") 