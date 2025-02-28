# Solicitar nombre de usuario
nombre = input("Ingresa el nombre: ")
if 3 < len(nombre) < 8:
    print("Hola " + nombre.upper())
else:
    print("El nombre debe tener entre 4 y 7 caracteres.")