numero = int(input("Ingrese un número: "))
formato = input("¿Cómo quiere la tabla? (H para horizontal, V para vertical): ")

if formato == "H" or formato == "h":
    for i in range(1, 13):
        print(numero * i, "", end="")
elif formato == "V" or formato == "v":
    for i in range(1, 13):
        print(numero, "x", i, "=", numero * i)
else:
    print("Opción no válida.")