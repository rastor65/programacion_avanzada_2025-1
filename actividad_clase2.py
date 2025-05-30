import sys
import math
def calcular_edad (edad):
    if edad < 0:
        return print("Edad no disponible.")
    if edad <= 12:
        return print("Eres un niño. Juega y diviertete.")
    elif edad <= 17:
        return print("Eres un adolecente. Enfocate en tus estudios.")
    elif edad <= 64:
        return print("Eres un adulto. Ordena tu  vida.")
    else:
        return print("Eres un adulto mayor. Disfruta de tu hogar.")
        
#edad = int(input("Ingrese su edad: "))
#calcular_edad(edad)

def tablaDeMultiplicar (n, o):
    if o == 1:
        for i in range(1, 12):
            print(f"{n} X {i} = {n*(i)}")
    else:
        lista = ""
        for i in range(1, 12):
            lista += f"{n} X {i} = {n*(i)}\t"
        print(lista)
""""        
numero = int(input("Ingresa un numero: "))
if numero < 1:
    print("Ingresa solo numeros enteros positivos.")
    sys.exit(0)
orientacion = int(input("Orientacion: \n1. Vertical. \n2. Horizontal.\n"))
if orientacion != 1 and orientacion != 2:
    print("Opcion no disponible (1 o 2).")
else:   
    tablaDeMultiplicar(numero, orientacion)
"""

def es_primo (numero):
    if numero <= 1:
        return False
    for i in range (2, int(math.sqrt(numero) +1)):
        if numero % i == 0:
            return False
    return True

def imprimir_numeros_primos (limite):
    for i in range (2, limite + 1):
        if es_primo(i):
            print(i)

numero = int(input("Ingresa el numero: "))
imprimir_numeros_primos(numero)