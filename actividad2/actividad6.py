import random
import string

def generar_contraseña(longitud):
    if longitud < 1:
        return "La longitud debe ser mayor a 0."

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = "".join(random.choices(caracteres, k=longitud))
    return contraseña

try:
    longitud = int(input("Longitud de la contraseña: "))
    print("Contraseña segura:", generar_contraseña(longitud))
except ValueError:
    print("Por favor, ingresa un número entero válido.")
