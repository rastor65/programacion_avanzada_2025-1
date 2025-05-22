import math

numero = int(input("Hola, ingrese un numero por favor: "))

def primo(numero):
    if numero < 2:
        return False
    if numero ==2 or numero==3:
        return True
    if numero % 2 ==0 or numero % 3 ==0: 
        return False
    
    limite = int(math.sqrt(numero))
    for i in range(5, limite + 1, 2):
        if numero % i == 0:
            return False
    return True

if primo(numero):
    print(f"{numero}")
    print("Este numero es primo ")
else:
    print(f"{numero}")
    print("Este numero  NO es primo")