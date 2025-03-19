import random
import string
def generar_contraseña(longitud):
    if longitud < 8:
        return 
    mayus = string.ascii_uppercase  
    minus = string.ascii_lowercase  
    numeros = string.digits             
    simbolos = string.punctuation        
    contraseña = [
        random.choice(mayus),
        random.choice(minus),
        random.choice(numeros),
        random.choice(simbolos)
    ]
    todos = mayus + minus + numeros + simbolos
    contraseña += random.choices(todos, k=longitud - 4)
    random.shuffle(contraseña)
    return "".join(contraseña)
longitud = int(input("Ingrese la longitud de la contraseña: "))
print("Contraseña generada:", generar_contraseña(longitud))
