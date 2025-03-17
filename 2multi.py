#Pide al usuario un número y genera su tabla de multiplicar del 1 al 12.
##Permite al usuario decidir si la tabla se imprime en formato horizontal o
#vertical.

def tablas():
    numero=int(input("digite un numero: (1 al 12):"))

    formato=input("ingrese si desea la tabla VERTICAL 'v' O horizontal 'h': ").strip().lower()

    if formato=="h":
        for i in range(1,13):
            print(f"{numero} x {i} = {numero*i} ",end=" | ")

    elif formato=="v":
        for i in range(1,13):
            print(f"{numero} x {i} = {numero*i}")

    else:
            print("formato no valido: ")

tablas()




    

