def class_edad(edad):
    if 0 <= edad <= 12:
        return "Niño", "¡Nunca dejes de soñar y jugar! El mundo es tuyo para descubrir."
    elif 13 <= edad <= 17:
        return "Adolescente", "¡Sigue aprendiendo y explorando! El futuro tiene muchas oportunidades para ti."
    elif 18 <= edad <= 64:
        return "Adulto", "¡El esfuerzo y la perseverancia te llevarán lejos! Sigue adelante con tus metas."
    elif edad >= 65:
        return "Adulto mayor", "¡Tu experiencia y sabiduría son invaluables! Disfruta cada momento."
    else:
        return "Edad no válida", "Por favor, ingresa una edad válida."
edad_usuario = int(input("Ingresa tu edad: "))
categoria, mensaje = class_edad(edad_usuario)
print(f"Categoría: {categoria}")
print(mensaje) 