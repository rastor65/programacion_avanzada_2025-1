import math

def es_primo(numero):
    """
    Determina si un número es primo.
    
    Args:
        numero: El número a evaluar
        
    Returns:
        bool: True si el número es primo, False en caso contrario
    """
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    
    limite = int(math.sqrt(numero)) + 1
    
    for i in range(5, limite, 6):
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
    
    return True

if __name__ == "__main__":
    num = int(input("Ingresa un número para verificar si es primo: "))
    if es_primo(num):
        print(f"{num} es un número primo")
    else:
        print(f"{num} no es un número primo")