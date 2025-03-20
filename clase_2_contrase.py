import random
import string

def contraseña(longi):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longi))

print(contraseña(5))
