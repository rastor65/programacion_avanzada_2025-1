#!/usr/bin/env python
"""
Script para verificar y crear roles si no existen.
Ejecutar con: python create_roles.py
"""

import os
import django

# Configuración inicial de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_moderno.settings')
django.setup()

from autenticacion.models import Rol

def create_roles():
    """Verificar y crear roles si no existen"""
    print("Verificando y creando roles necesarios...")
    
    # Lista de roles predefinidos
    roles_predefinidos = [
        {'nombre': 'estudiante', 'descripcion': 'Estudiante del colegio'},
        {'nombre': 'profesor', 'descripcion': 'Profesor del colegio'},
        {'nombre': 'admin', 'descripcion': 'Administrador del sistema'}
    ]
    
    # Verificar y crear cada rol
    roles_creados = []
    for rol_data in roles_predefinidos:
        rol, created = Rol.objects.get_or_create(
            nombre=rol_data['nombre'],
            defaults={'descripcion': rol_data['descripcion']}
        )
        
        if created:
            print(f"✅ Rol creado: {rol.nombre} (ID: {rol.id})")
            roles_creados.append(rol)
        else:
            print(f"ℹ️ Rol ya existe: {rol.nombre} (ID: {rol.id})")
    
    # Mostrar todos los roles existentes
    print("\nRoles en el sistema:")
    for rol in Rol.objects.all():
        print(f"ID: {rol.id}, Nombre: '{rol.nombre}', Descripción: '{rol.descripcion}'")
    
    return roles_creados

if __name__ == "__main__":
    roles = create_roles()
    print(f"\nTotal de roles creados: {len(roles)}")
    print(f"Total de roles en el sistema: {Rol.objects.count()}") 