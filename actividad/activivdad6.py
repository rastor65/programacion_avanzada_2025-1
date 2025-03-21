nUsuario = input("Ingrese su nombre de usuario: ")
longitud = len(nUsuario)

if longitud > 3 and longitud < 8:
    mayusculas = nUsuario.upper()
    print(f"¡Hola {mayusculas}! Tu nombre de usuario ha sido aceptado!.")
else:
    print("El nombre de usuario debe tener más de 3 caracteres y menos de 8.")
    print(f"Tu nombre tiene {longitud} caracteres.")



