#pagina 32
codigo_ = input("Ingrese el codigo del producto: ")
code = "PRO"
mayus = codigo_.upper()
valido = mayus.startswith(code)

if valido:
    print("El codigo es valido")
    print(f"Nota: Se ha convertido el código a '{mayus}'.")

else:
    print("El codigo no es valido. Intente nuevamente")
