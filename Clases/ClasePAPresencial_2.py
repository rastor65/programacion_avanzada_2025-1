nombre = str(input("Ingrese su nombre, por favor: "))
nombre.upper()

if len(nombre) > 3 and len(nombre) < 8 :
    print (f"¡Mucho gusto, {nombre.upper()}!")
    print(f"Su nombre tiene {len(nombre)} letras")
else : 
    print("Su nombre no ha sido admitido, lo lamento")
    