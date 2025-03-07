def procesar_nombre_usuario():
    # Ingresar nombre de usuario
    nombre_usuario = input("Ingrese su nombre de usuario: ")

    # Verificar longitud del nombre de usuario
    if len(nombre_usuario) < 4 or len(nombre_usuario) > 7:
        print("El nombre de usuario debe tener entre 4 y 7 caracteres.")
    else:
        # Convertir nombre de usuario a mayúsculas
        nombre_usuario_mayusculas = nombre_usuario.upper()

        # Enviar saludo con nombre de usuario en mayúsculas
        print(f"Hola, {nombre_usuario_mayusculas}!")

procesar_nombre_usuario()