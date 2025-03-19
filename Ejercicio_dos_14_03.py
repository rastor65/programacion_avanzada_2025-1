def GenerarTabla(numero, formato):
    if formato == "vertical":
        for i in range(1, 13):
            print(f"{numero} x {i} = {numero * i}")
    elif formato == "horizontal":
        print(" | ".join([f"{numero} x {i} = {numero * i}" for i in range(1, 13)]))
    else:
        print("Formato no válido. solo hay horizontal o vertical.")
numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))
formato = input("Elige el formato de impresión (horizontal/vertical): ").strip().lower()
GenerarTabla(numero, formato)

