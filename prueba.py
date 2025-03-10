
presupuesto = float(input("Ingrese su presupuesto: "))
gastos = float(input("Ingrese el precio de los vegetales: "))
gastos = float(input("Ingrese el precio de la carne: "))
gastos = float(input("Ingrese el precio de las especias: "))
if gastos < presupuesto:
    gastos = float(input("Ingrese el precio de las frutas: "))
    if gastos == presupuesto:
        print("No le queda dinero despues de la compra.")
    elif gastos < presupuesto:
        restante = presupuesto - gastos
        print(f"La cantidas que le queda es de ${restante}.")
    else:
        print("La compra supera su presupuesto.")
elif gastos == presupuesto:
    print("No le queda dinero para comprar frutas.")
else:
    print("La compra supera su presupuesto.")
