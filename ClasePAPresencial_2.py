nombre = str(input("Ingrese su nombre, por favor: "))
nombre.upper()

if len(nombre) > 3 and len(nombre) < 8 :
    print (f"Su nombre es: {nombre.upper()}")
    print(f"{len(nombre)}")
else : 
    print("Su nombre no ha sido admitido, lo lamento")
    