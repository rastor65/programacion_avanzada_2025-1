product_code = input("Ingrese el codigo del producto que desea verificar")
product_code = product_code.upper()
if product_code.startswith("PRO"):
    print("El codigo ingresado es valido")
else:
    print("El codigo ingresado no es valido")