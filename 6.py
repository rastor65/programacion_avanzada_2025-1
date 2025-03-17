import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.sample(caracteres, longitud))

longitud = int(input("Ingrese la longitud de la contraseña: "))
print("Contraseña segura:", generar_contraseña(longitud))
