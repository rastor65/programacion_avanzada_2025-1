Cod = input("Ingrese el codigo del producto que desea verificar")
Cod = Cod.upper()
if Cod.startswith("PRO"):
    print("El codigo ingresado es valido")
else:
    print("El codigo ingresado no es valido")
