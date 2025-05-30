import random
import string 


peticion= int(input("Ingrese la cantidad de caracteres que quiere que tenga la contraseña: "))

def contraseña(peticion):
        if peticion <=7:
            print("La contrasea debe tener minimo 8 caracteres...")
        else:
    
            caracteres = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper()
            contra = ''.join(random.choice(caracteres) for _ in range(peticion))
    
            return contra


print(f"La contraseña que se genero es: {contraseña(peticion)}" )