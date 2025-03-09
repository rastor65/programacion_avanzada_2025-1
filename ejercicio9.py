codigo = input("Ingrese el código del producto: ").upper()

if codigo.startswith("PROMO"):
    print("Código válido")
else:
    print("Código inválido")