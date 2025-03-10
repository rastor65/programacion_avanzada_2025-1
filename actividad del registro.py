print("Bienvenido al Bienestar")
usuario = str(input("Por favor ingrese su nombre de usuario"))
if len(usuario) > 3 and len(usuario) < 8:
    print(f"¡Hola, {usuario.upper()}!")
else:
    print("El nombre debe tener entre 4 y 7 caracteres como máximo")
exit()