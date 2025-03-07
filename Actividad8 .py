def editar_articulo():
    # Ingresar artículo
    articulo = input("Ingrese el artículo: ")

    # Reemplazar "tecnología antigua" por "tecnología de punta"
    articulo_corregido = articulo.replace("tecnología antigua", "tecnología de punta")

    # Dividir artículo en oraciones
    oraciones = articulo_corregido.split(". ")

    # Mostrar resultado
    print("Artículo corregido y dividido en oraciones:")
    for i, oracion in enumerate(oraciones):
        print(f"{i+1}. {oracion}")

editar_articulo()