import secrets
import string
from passlib.hash import bcrypt

# 1. Generar una contraseña segura
def sugerir_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(caracteres) for _ in range(longitud))

# 2. Hashear (guardar) una contraseña
def guardar_contraseña(plain_password):
    return bcrypt.hash(plain_password)

# 3. Verificar una contraseña contra su hash
def verificar_contraseña(plain_password, hashed_password):
    return bcrypt.verify(plain_password, hashed_password)

# 4. Cambiar contraseña (genera un nuevo hash)
def cambiar_contraseña(nueva_contraseña):
    return guardar_contraseña(nueva_contraseña)

# ------------- DEMOSTRACIÓN --------------

# Generar sugerencia
sugerida = sugerir_contraseña()
print("🔐 Contraseña sugerida:", sugerida)

# Guardar (hash)
hash_sugerida = guardar_contraseña(sugerida)
print("🔒 Hash almacenado:", hash_sugerida)

# Verificar contraseña (correcta)
resultado = verificar_contraseña(sugerida, hash_sugerida)
print("✅ Verificación (correcta):", resultado)

# Intento con contraseña incorrecta
resultado_incorrecto = verificar_contraseña("claveIncorrecta123", hash_sugerida)
print("❌ Verificación (incorrecta):", resultado_incorrecto)

# Cambiar contraseña
nueva = "NuevaClaveSegura456@"
nuevo_hash = cambiar_contraseña(nueva)
print("🔄 Nuevo hash después del cambio:", nuevo_hash)

# Verificar nueva contraseña
print("✅ Verificación nueva:", verificar_contraseña(nueva, nuevo_hash))
