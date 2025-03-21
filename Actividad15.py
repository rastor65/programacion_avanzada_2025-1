import random
import string

def contraseña(longitud):
    if longitud < 4:
       print("la longitud minima es de 4 caracteres")
       return
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation
    contraseña = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]
    todos_los_caracteres = mayusculas + minusculas + numeros + simbolos
    contraseña += random.sample(todos_los_caracteres, k=longitud - 4)
    random.shuffle(contraseña)
    return ''.join(contraseña)
longitud = int(input("Ingresa la longitud que desea para su contraseña: "))
contraseña_segura = contraseña(longitud)
print("Su Contraseña segura es:", contraseña_segura)