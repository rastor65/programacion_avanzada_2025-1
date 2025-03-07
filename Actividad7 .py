def analizar_comentario():
    # Ingresar comentario de cliente
    comentario = input("Ingrese el comentario de cliente: ")

    # Eliminar espacios innecesarios
    comentario_sin_espacios = comentario.strip()

    # Convertir comentario a minúsculas
    comentario_minusculas = comentario_sin_espacios.lower()

    # Contar cantidad de veces que se menciona la palabra "excelente"
    cantidad_excelente = comentario_minusculas.count("excelente")

    # Mostrar resultado
    print(f"Comentario en minúsculas: {comentario_minusculas}")
    print(f"Cantidad de veces que se menciona 'excelente': {cantidad_excelente}")

analizar_comentario()