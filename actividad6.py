nombre = input("Ingrese su nombre de usuario: ")

if 3 < len(nombre) < 8:
    print(f"¡Hola, {nombre.upper()}!")
else:
    print("El nombre de usuario debe tener entre 4 y 7 caracteres.")