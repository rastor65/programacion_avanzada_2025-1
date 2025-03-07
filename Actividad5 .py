def calcular_area_terreno():
    # Ingresar longitud del lado conocido
    lado_conocido = float(input("Ingrese la longitud del lado conocido: "))

    # Calcular área del terreno (suponiendo que el terreno es un cuadrado)
    area_terreno = lado_conocido ** 2

    # Mostrar resultado
    print(f"El área del terreno es: {area_terreno} unidades cuadradas")

calcular_area_terreno()