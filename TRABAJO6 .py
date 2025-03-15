import random
import string

def generar_contraseña_segura(longitud):
    if longitud < 4:
        raise ValueError("La longitud debe ser al menos 4 para incluir todos los tipos de caracteres.")

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    contraseña += random.choices(caracteres, k=longitud - 4)
    random.shuffle(contraseña)

    return ''.join(contraseña)

# Ejemplo de uso
longitud = 12
print(generar_contraseña_segura(longitud))