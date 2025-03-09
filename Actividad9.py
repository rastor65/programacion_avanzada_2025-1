codigo = input("por favor Ingrese el código de producto: ")
codigo = codigo.upper()
if codigo.startswith("PRO"):
    print("El Código que ha ingresado es válido")
else:
    print("El Código que ha ingresado NO es válido")