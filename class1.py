nombre = input("Ingrese su nombre: ")
if len(nombre) < 3 or len(nombre) > 8:
    print("Nombre no valido. Debe tener entre 3-8 caracteres.")
else: 
    print(f"Hola, {nombre.upper()}.")
