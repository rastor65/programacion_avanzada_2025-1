nombre = input("ingrese su nombre ")
if len(nombre) < 3 or len(nombre) > 8:
    print("nombre no valido. debe tener entre 3 a 8 caracteres. ")
else:
    print(f"hola, {nombre.upper()}.")