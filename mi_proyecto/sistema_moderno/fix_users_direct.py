#!/usr/bin/env python
"""
Script ejecutable directamente para corregir usuarios sin perfil.
Ejecutar con: python fix_users_direct.py
"""

import os
import sys
import django

# Configuración inicial de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_moderno.settings')
django.setup()

from django.contrib.auth.models import User
from autenticacion.models import Usuario

def fix_user_profiles():
    """Crear perfiles para usuarios que no tienen uno, especialmente superusers"""
    total_fixed = 0
    
    # Obtener todos los usuarios sin perfil
    for user in User.objects.all():
        try:
            # Intentar acceder al perfil
            profile = user.perfil
            print(f"Usuario {user.username} ya tiene perfil: {profile}")
        except:
            # Si no tiene perfil, crear uno
            if user.is_superuser or user.is_staff:
                rol = 'admin'
            else:
                rol = 'estudiante'
                
            Usuario.objects.create(
                user=user,
                rol=rol,
                nombres=user.first_name or user.username,
                apellidos=user.last_name or '',
                email=user.email
            )
            total_fixed += 1
            print(f"Perfil creado para {user.username} con rol {rol}")
    
    return total_fixed

if __name__ == "__main__":
    print("Iniciando reparación de perfiles de usuario...")
    fixed = fix_user_profiles()
    print(f"Proceso completado. {fixed} perfiles de usuario creados.") 