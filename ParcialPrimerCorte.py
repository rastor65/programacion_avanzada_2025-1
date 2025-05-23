import random
import os
def Generar_NumeroRandom():
    return random.randint(1,100)
nums = Generar_NumeroRandom()
inten = 0
while True:
    num =int(input("ingrese un numero del 1 al 100:y "))
    inten += 1
    if num == nums:
        print(f"El nuemro ingresado {num} es el numero correcto")
        os.system("pause")
        break
    elif num < nums:
        print(f"El nuemro ingresado {num} es menor que el numero que esta buscando vuelva intertarlo")
        os.system("pause")
        os.system("cls")
    else :
        print(f"El numero ingresado {num} es mayor que el el nuemro que esta buscando vuelva intentarlo")
        os.system("pause")
        os.system("cls")
print(f"El numero de intentos totales que intento fue la siguiente {inten}")
    
    
    