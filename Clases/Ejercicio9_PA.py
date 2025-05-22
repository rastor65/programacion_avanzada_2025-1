codigo = str(input("Ingrese su codigo de producto, por favor: "))
codigo.upper()

print(f"{codigo.upper()}")

if codigo.startswith(codigo) :
    print("Codigo Valido")
else:
    print("Codigo Invalido")
