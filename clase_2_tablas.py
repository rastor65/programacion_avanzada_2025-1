def tablita():
    numero = int(input("Introduce la tabla que quieras del 1 al 12: "))
    formato = input("¿Deseas la tabla en formato horizontal o vertical? (horiz/vert): ")

    if formato.lower() == 'horiz':
        print("Tabla de multiplicar del", numero)
        for i in range(1, 13):
            print(f"{numero} * {i} = {numero * i}", end="  ")
    else:
        print("Tabla de multiplicar del", numero)
        for i in range(1, 13):
            print(f"{numero} * {i} = {numero * i}")
tablita()   