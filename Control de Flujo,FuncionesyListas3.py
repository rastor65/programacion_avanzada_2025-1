import math

def es_primo(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limite = int(math.sqrt(n)) + 1
    for i in range(5, limite, 2):
        if n % i == 0:
            return False
    return True

num = int(input("Ingrese un número: "))
print("Es primo" if es_primo(num) else "No es primo")
