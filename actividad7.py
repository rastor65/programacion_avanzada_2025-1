
comentario = input("Ingrese el comentario del cliente: ")
comentarioLimpio = comentario.strip()

minusculas = comentarioLimpio.lower()

cantidad_excelente = minusculas.count("excelente")

print(f"Comentario en minúsculas: {minusculas}")
print(f"Número de veces que se menciona 'excelente': {cantidad_excelente}")

if cantidad_excelente > 0:
    print("¡Parece que el cliente está satisfecho con el producto!")
else:
    print("El cliente no mencionó la palabra 'excelente' en su comentario.")