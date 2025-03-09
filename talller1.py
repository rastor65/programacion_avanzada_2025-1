presupuesto = float(input ("ingrese su presupuesto chef :   "))
vegetales = float (input(" cuanto vas a gastar en vegetales :  "))
carnes = float(input("cuantos vas a gastar en carnes :  "))
espesias = float (input("cuantos vas a gastar en especias :  "))
presupuesto -= (vegetales + carnes + espesias)
if presupuesto > 0:
    frutas = float(input("Ingrese el costo de las frutas : "))
    if frutas <= presupuesto:
        presupuesto -= frutas
    else:
        print("No hay suficiente presupuesto para comprar frutas.")

print(f"Dinero restante después de todas las compras: ${presupuesto:.2f}")
