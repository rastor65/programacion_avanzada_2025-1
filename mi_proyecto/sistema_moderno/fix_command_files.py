#!/usr/bin/env python
"""
Script para arreglar archivos con bytes nulos que causan problemas en las migraciones.
Ejecutar con: python fix_command_files.py
"""

import os
import sys

def fix_null_bytes():
    # Rutas a revisar
    paths_to_check = [
        'autenticacion/management/commands',
        'autenticacion/management',
        'autenticacion/migrations'
    ]
    
    fixed_files = 0
    
    for base_path in paths_to_check:
        if not os.path.exists(base_path):
            print(f"La ruta {base_path} no existe, saltando...")
            continue
            
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    
                    try:
                        # Intentar abrir el archivo en modo binario
                        with open(file_path, 'rb') as f:
                            content = f.read()
                        
                        # Verificar si hay bytes nulos
                        if b'\x00' in content:
                            print(f"Encontrados bytes nulos en {file_path}, corrigiendo...")
                            
                            # Eliminar bytes nulos
                            content = content.replace(b'\x00', b'')
                            
                            # Guardar el archivo corregido
                            with open(file_path, 'wb') as f:
                                f.write(content)
                                
                            fixed_files += 1
                            print(f"✅ Archivo corregido: {file_path}")
                    except Exception as e:
                        print(f"❌ Error al procesar {file_path}: {str(e)}")
    
    print(f"\nTotal de archivos corregidos: {fixed_files}")
    return fixed_files

if __name__ == "__main__":
    print("Buscando y corrigiendo archivos con bytes nulos...")
    fixed = fix_null_bytes()
    if fixed > 0:
        print("Se recomienda ejecutar 'python manage.py migrate' nuevamente.")
    else:
        print("No se encontraron archivos con problemas de bytes nulos.") 