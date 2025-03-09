articulo_noticia = input("Ingrese el artículo: ")
corregido = articulo_noticia.replace("tecnología antigua", "tecnología de punta")
oraciones = corregido.split(". ")

print("Artículo corregido:", corregido)
print("Oraciones:", oraciones)