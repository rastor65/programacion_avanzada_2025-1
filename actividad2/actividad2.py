def tabla_multilicar():
    num = int(input("Ingrese el número de la tabla de multiplicar: "))
    formato = input("¿Quieres el formato de la tabla de multiplicar en horizontal o vertical? (h/v): ").strip().lower()
    
    if formato == "h":
        resultados = [f"| {num} x {i} = {num * i} |" for i in range(1, 13)]
        print("  ".join(resultados))
    elif formato == "v":
        for i in range(1, 13):
            print(f"{num} x {i} = {num * i}")
    else:
        print("Formato no válido")

tabla_multilicar()