def determinar_categoria(edad):
    """Determina la categoría de edad y devuelve un string."""
    if 0 <= edad <= 12:
        return "niño"
    elif 13 <= edad <= 17:
        return "adolescente"
    elif 18 <= edad <= 64:
        return "adulto"
    else:  # edad >= 65
        return "adulto mayor"

def obtener_mensaje_motivacional(categoria):
    """Devuelve un mensaje motivacional según la categoría de edad."""
    mensajes = {
        "niño": "¡El mundo es tuyo para explorarlo! Disfruta cada día con curiosidad y alegría.",
        "adolescente": "Estás en una etapa de descubrimiento. Confía en ti mismo y persigue tus sueños con pasión.",
        "adulto": "Tienes la experiencia y energía para lograr grandes cosas. ¡Nunca dejes de aprender y crecer!",
        "adulto mayor": "Tu sabiduría es un tesoro invaluable. Sigue compartiendo tus experiencias y disfrutando cada momento."
    }
    return mensajes[categoria]


print("Bienvenido al Clasificador de Edades")

# Solicitar y validar la edad
while True:
    try:
        edad = int(input("Por favor, ingresa tu edad: "))
        if edad < 0:
            print("La edad no puede ser negativa. Intenta de nuevo.")
            continue
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

categoria = determinar_categoria(edad)
mensaje = obtener_mensaje_motivacional(categoria)

print(f"\nCon {edad} años, eres un {categoria}.")
print(f"Mensaje para ti: {mensaje}")