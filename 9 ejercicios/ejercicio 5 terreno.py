medida_conocida = float(input("Ingrese la medida de un lado del terreno (en metros): "))

respuesta = input("¿Conoce alguna relación entre los lados? (si/no): ").strip().lower()

if respuesta == "si":
    relacion = float(input("Ingrese el valor por el cual multiplicar el lado conocido para obtener el otro lado: "))
    otro_lado = medida_conocida * relacion
    area = medida_conocida * otro_lado
    print(f"El área del terreno es {area:.2f} metros cuadrados.")
else:
    print("No se puede calcular el área sin conocer el otro lado del terreno.")
