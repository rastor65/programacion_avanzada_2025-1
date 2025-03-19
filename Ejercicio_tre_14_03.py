import math
def primos(n):
    if n < 2:
        return False  
    if n in (2, 3):
        return True  
    if n % 2 == 0 or n % 3 == 0:
        return False  
    limite = int(math.sqrt(n))
    for i in range(5, limite + 1, 2): 
        if n % i == 0:
            return False
    return True
numero = int(input("Ingresa un número para verificar si es primo: "))
if primos(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
