articulo = input("Ingrese el artículo a corregir: ")
articulo_corregido = articulo.replace("tecnología antigua", "tecnología de punta")

oraciones = articulo_corregido.split(". ")

print("\nArtículo corregido:")
print(articulo_corregido)

print("\nOraciones del artículo:")
for i, oracion in enumerate(oraciones, 1):
   if oracion and not oracion.endswith("."):
       oracion += "."
   print(f"Oración {i}: {oracion}")