
codigo = input("Ingrese el código del producto: ")


codigo_mayusculas = codigo.upper()


if codigo_mayusculas.startswith("PRO"):
    print("Código válido")
else:
    print("Código inválido")
