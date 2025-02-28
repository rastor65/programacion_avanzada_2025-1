print("Bienvenido al Bienestar")
nombre_usu = str(input("Porfavor ingrese su nombre de usuario"))
if len(nombre_usu) > 3 and len(nombre_usu) < 8:
    print(f"¡Hola, {nombre_usu.upper()}!")
else:
    print("El nombre debe tener entre 4 y 7 caracteres como maximo")
