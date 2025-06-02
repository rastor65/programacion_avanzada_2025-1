#Escribir un prgrama en python que
#genere un numero aleatorio entre 1 y 100
#pida al usuario que adivine el numero
#indiduque si el numero ingresado es mayor o menor que el numero generado
#el usuario debe serguir intentando hasta adivinarlo
#al final mostrar cuantos intentos le tomó

import random
num=random.randint(1,100)

intentos=0

while True:
    num_usuario=int(input("Ingresa un numero: "))
    intentos+=1
    if num_usuario<num:
        print("El numero es mayor")
    elif num_usuario>num:
        print("El numero es menor")
    else:
        print("Adivinaste el numero")
        print(f"Te tomó {intentos} intentos")
        break
