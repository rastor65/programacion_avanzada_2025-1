usuario = input("Ingresa tu nombre de usuario: ")

if 3 < len(usuario) < 8:
    print("¡Holiss,", usuario.upper() + "!")
else:
    print("El nombre debe tener entre 4 y 7 caracteres.")