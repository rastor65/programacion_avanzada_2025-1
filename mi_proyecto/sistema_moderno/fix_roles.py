#!/usr/bin/env python
"""
Script para arreglar problemas con los roles en la base de datos.
Ejecutar con: python fix_roles.py
"""

import os
import django
import sys

# Configuración inicial de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_moderno.settings')
django.setup()

from django.db import connection
from autenticacion.models import Rol

def fix_roles():
    """Arreglar problemas con los roles en la base de datos"""
    print("Arreglando problemas con los roles...")
    
    # 1. Verificar si hay roles con nombres duplicados (ignorando mayúsculas/minúsculas)
    print("Verificando nombres duplicados...")
    
    # Obtener todos los roles
    roles = Rol.objects.all()
    nombres_lower = {}
    duplicados = []
    
    for rol in roles:
        nombre_lower = rol.nombre.lower()
        if nombre_lower in nombres_lower:
            duplicados.append((rol, nombres_lower[nombre_lower]))
        else:
            nombres_lower[nombre_lower] = rol
    
    if duplicados:
        print(f"Se encontraron {len(duplicados)} roles con nombres duplicados.")
        for rol_dup, rol_orig in duplicados:
            print(f"  - Duplicado: ID {rol_dup.id}, Nombre '{rol_dup.nombre}'")
            print(f"    Original: ID {rol_orig.id}, Nombre '{rol_orig.nombre}'")
            
            # Eliminar el duplicado
            print(f"    Eliminando rol duplicado (ID: {rol_dup.id})...")
            rol_dup.delete()
    else:
        print("No se encontraron roles con nombres duplicados.")
    
    # 2. Normalizar nombres de roles (convertir a minúsculas)
    print("\nNormalizando nombres de roles...")
    for rol in Rol.objects.all():
        nombre_original = rol.nombre
        nombre_normalizado = nombre_original.lower()
        
        if nombre_original != nombre_normalizado:
            rol.nombre = nombre_normalizado
            rol.save()
            print(f"  - Rol ID {rol.id}: '{nombre_original}' → '{nombre_normalizado}'")
    
    # 3. Eliminar restricción UNIQUE si está causando problemas
    print("\nVerificando restricción UNIQUE en la tabla de roles...")
    try:
        with connection.cursor() as cursor:
            # En SQLite, podemos verificar las restricciones
            cursor.execute("PRAGMA index_list('autenticacion_rol');")
            indices = cursor.fetchall()
            
            for indice in indices:
                if 'unique' in indice[1].lower() or 'nombre' in indice[1].lower():
                    print(f"  - Encontrado índice: {indice[1]}")
                    
                    # Si queremos eliminar la restricción, tendríamos que recrear la tabla
                    # Esto es complejo y arriesgado, así que solo lo mostramos como información
                    print("    Para eliminar la restricción UNIQUE, sería necesario modificar la migración y recrear la tabla.")
    except Exception as e:
        print(f"  Error al verificar restricciones: {e}")
    
    # 4. Asegurar que existan los roles básicos
    print("\nAsegurando que existan los roles básicos...")
    roles_basicos = ['estudiante', 'profesor', 'admin']
    
    for nombre in roles_basicos:
        rol, created = Rol.objects.get_or_create(
            nombre=nombre,
            defaults={'descripcion': f'Rol de {nombre}'}
        )
        
        if created:
            print(f"  - Creado rol: '{rol.nombre}' (ID: {rol.id})")
        else:
            print(f"  - Rol ya existe: '{rol.nombre}' (ID: {rol.id})")
    
    # Mostrar todos los roles después de las correcciones
    print("\nRoles después de las correcciones:")
    for rol in Rol.objects.all():
        print(f"ID: {rol.id}, Nombre: '{rol.nombre}', Descripción: '{rol.descripcion}'")
    
    return True

if __name__ == "__main__":
    success = fix_roles()
    if success:
        print("\n✅ Corrección de roles completada con éxito.")
        sys.exit(0)
    else:
        print("\n❌ Error al corregir roles.")
        sys.exit(1) 