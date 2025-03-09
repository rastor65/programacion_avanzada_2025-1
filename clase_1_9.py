#clase 25
presupuesto = float(input("¿De cuánto es su presupuesto? "))
precio = float(input("¿Cuánto cuesta la licencia? "))
cantidad = int(input("¿Cuántas licencias quiere comprar? "))

total =precio * cantidad
sobrante= presupuesto - total
adicional= int(sobrante / precio)

if total <= presupuesto:
    print("Compra realizada")
    if sobrante == total:
        print(f"Le alcanza para {adicional} licencias más")
    else:
        print("Ha usado todo el presupuesto")
else:
    print("No le alcanza su presupuesto")