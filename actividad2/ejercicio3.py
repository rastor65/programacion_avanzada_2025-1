import math

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Ingrese un número: "))

if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")