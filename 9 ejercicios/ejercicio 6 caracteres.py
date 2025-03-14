def procesar_usuario(nombre):
    if 3 < len(nombre) < 8:
        print(f" Feliz dia, {nombre.upper()}!")
    else:
        print("El nombre debe tener entre 4 y 7 caracteres.")

nombre_usuario = input("Ingresa su nombre de usuario: ")
procesar_usuario(nombre_usuario)
