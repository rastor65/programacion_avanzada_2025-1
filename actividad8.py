articulo = input("Ingrese el artículo: ")
articulo_modificado = articulo.replace("tecnología antigua", "tecnología de punta")
oraciones = articulo_modificado.split(". ")
print("\nArtículo corregido:")
for oracion in oraciones:
    print(f"- {oracion.strip()}.")