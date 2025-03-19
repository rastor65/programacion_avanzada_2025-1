numero=int(input("Ingrese un numero, por favor: "))
def tabla(numero):
    print("La tabla del numero ingresado es: ")
    for i in range(1,13):
        resultado=numero * i
        print(f"El {numero} x {i} = {resultado}")
        
if numero <=0:
    print("Esta tabla no es posible...")
else:
    tabla(numero)