#!/usr/bin/env python
"""
Script para corregir archivos con caracteres nulos en la carpeta management/commands
"""

import os
import glob

def fix_null_bytes():
    # Rutas a revisar
    paths = [
        'autenticacion/management/__init__.py',
        'autenticacion/management/commands/__init__.py',
        'autenticacion/management/commands/check_auth.py',
    ]
    
    for path in paths:
        if os.path.exists(path):
            print(f"Corrigiendo archivo: {path}")
            try:
                # Leer el archivo y eliminar caracteres nulos
                with open(path, 'rb') as f:
                    content = f.read()
                
                # Eliminar caracteres nulos
                content = content.replace(b'\x00', b'')
                
                # Escribir el contenido corregido
                with open(path, 'wb') as f:
                    f.write(content)
                
                print(f"  ✓ Archivo corregido")
            except Exception as e:
                print(f"  ✗ Error al corregir el archivo: {e}")
        else:
            print(f"El archivo {path} no existe")
    
    # Crear archivos vacíos si no existen
    for path in paths:
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            print(f"Creado directorio: {directory}")
        
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write("# Archivo generado automáticamente\n")
            print(f"Creado archivo vacío: {path}")

if __name__ == "__main__":
    print("Iniciando corrección de archivos con caracteres nulos...")
    fix_null_bytes()
    print("Proceso completado.") 