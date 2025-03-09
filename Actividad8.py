articulo = input("ingrese su articulo: ")
corregido_articulo = articulo.replace("tecnologia antigua","tecnologia de punta")
oracion = corregido_articulo.split(".")
print("su articulo ya corregido es: ",corregido_articulo)
for a, oracion in enumerate(oracion,1):
    print(f"oracion # {a}: {oracion.strip()}")
