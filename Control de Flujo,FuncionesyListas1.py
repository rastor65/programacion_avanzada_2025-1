def clasificar_edad(edad):
    if edad <= 12:
        return "Niño", "¡Disfruta tu infancia!"
    elif edad <= 17:
        return "Adolescente", "¡Sigue aprendiendo y creciendo!"
    elif edad <= 64:
        return "Adulto", "¡Sigue trabajando por tus sueños!"
    else:
        return "Adulto mayor", "¡Tu experiencia es valiosa!"

def obtener_edad():
    return int(input("Ingresa tu edad: "))

def main():
    edad = obtener_edad()
    categoria, mensaje = clasificar_edad(edad)
    print(f"Eres {categoria}. {mensaje}")

main()
