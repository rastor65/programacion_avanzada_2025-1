print("Cliente 1: ")
reseña1= str(input("Cuentenos su experiencia con el producto: "))
print("Cliente 2: ")
reseña2= str(input("Cuentenos su experiencia con el producto: "))
print("Cliente 3: ")
reseña3= str(input("Cuentenos su experiencia con el producto: "))

reseñaModificada1=reseña1.lower().strip()
reseñaModificada2=reseña2.lower().strip()
reseñaModificada3=reseña3.lower().strip()

mencion1=reseñaModificada1.count("excelente")
mencion2=reseñaModificada2.count("excelente")
mencion3=reseñaModificada3.count("excelente")

cantidadMenciones=mencion1 + mencion2 + mencion3
cantidadCliente= reseña1 + reseña2 + reseña3


print(f"excelente se menciona {cantidadMenciones} veces en {cantidadCliente} reseñas...")