import math
def primo(n):
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
num = int(input("Ingrese un número para saber si es primo o no: "))
if primo(num):
    print(f"El numero {num} es un número primo.")
else:
    print(f"El numero {num} no es un número primo.")
   