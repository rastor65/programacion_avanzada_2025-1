while True:
    try:
        numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

while True:
    formato = input("¿Cómo deseas ver la tabla? (H para horizontal, V para vertical): ").upper()
    if formato in ["H", "V"]:
        break
    else:
        print("Por favor, ingresa 'H' para horizontal o 'V' para vertical.")

print(f"\nTabla de multiplicar del {numero}:")

if formato == "H":
    resultado = []
    for i in range(1, 13):
        resultado.append(f"{numero} x {i} = {numero * i}")
    print("  ".join(resultado))
else:
    for i in range(1, 13):
        print(f"{numero} x {i} = {numero * i}")