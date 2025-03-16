import secrets
import string
def generar_contraseñas(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(caracteres)for _ in range(longitud))
    return contraseña
longitud_contraseña = 12
contraseña_segura = generar_contraseñas(longitud_contraseña)
print(f"contraseña_generada: {contraseña_segura}")