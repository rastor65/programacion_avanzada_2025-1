#!/usr/bin/env python
"""
Script para eliminar bytes nulos de archivos Python que causan problemas en las migraciones.
Ejecutar con: python fix_null_bytes.py
"""

import os
import sys

def fix_null_bytes_in_directory(directory='.'):
    """Elimina bytes nulos de todos los archivos Python en el directorio especificado y sus subdirectorios"""
    print(f"Buscando archivos Python con bytes nulos en: {directory}")
    fixed_files = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    # Leer el archivo en modo binario
                    with open(file_path, 'rb') as f:
                        content = f.read()
                    
                    # Verificar si contiene bytes nulos
                    if b'\x00' in content:
                        # Eliminar bytes nulos
                        cleaned_content = content.replace(b'\x00', b'')
                        
                        # Escribir el contenido limpio
                        with open(file_path, 'wb') as f:
                            f.write(cleaned_content)
                        
                        print(f"Corregido: {file_path}")
                        fixed_files += 1
                except Exception as e:
                    print(f"Error al procesar {file_path}: {e}")
    
    return fixed_files

if __name__ == "__main__":
    # Obtener directorio desde argumentos o usar el directorio actual
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    # Corregir archivos
    fixed_files = fix_null_bytes_in_directory(directory)
    
    if fixed_files > 0:
        print(f"\nSe corrigieron {fixed_files} archivos con bytes nulos.")
    else:
        print("\nNo se encontraron archivos con bytes nulos.")
    
    print("\nPara corregir un directorio específico, ejecute:")
    print("python fix_null_bytes.py ruta/al/directorio") 