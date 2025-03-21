import random
import string

def generar_contraseña(longitud=12):
    """
    Genera una contraseña segura de la longitud especificada.
    
    Args:
        longitud: Longitud de la contraseña (por defecto 12)
        
    Returns:
        str: Contraseña generada que incluye mayúsculas, minúsculas,
             números y símbolos especiales
    """
    # Definir los conjuntos de caracteres
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation
    
    # Asegurarnos de que la contraseña tenga al menos un carácter de cada tipo
    contraseña = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]
    
    # Completar el resto de la contraseña
    caracteres_restantes = longitud - 4
    todos_caracteres = mayusculas + minusculas + numeros + simbolos
    
    for _ in range(caracteres_restantes):
        contraseña.append(random.choice(todos_caracteres))
    
    # Mezclar la contraseña para que no tenga un patrón predecible
    random.shuffle(contraseña)
    
    # Convertir la lista a string y retornar
    return ''.join(contraseña)

# Ejemplo de uso
if __name__ == "__main__":
    longitud_deseada = int(input("Ingresa la longitud deseada para la contraseña: "))
    nueva_contraseña = generar_contraseña(longitud_deseada)
    print(f"Tu nueva contraseña segura es: {nueva_contraseña}")