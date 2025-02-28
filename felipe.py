
presupuesto = float(input("Ingrese el presupuesto inicial del chef: "))
costo_vegetales = float(input("Ingrese el costo de los vegetales: "))
costo_carne = float(input("Ingrese el costo de la carne: "))
costo_especias = float(input("Ingrese el costo de las especias: "))

total_gastos = costo_vegetales + costo_carne + costo_especias

dinero_restante = presupuesto - total_gastos

if dinero_restante > 0:
    costo_frutas = float(input("Ingrese el costo de las frutas: "))
    if costo_frutas <= dinero_restante:
        dinero_restante -= costo_frutas
    else:
        print("No hay suficiente dinero para comprar frutas.")

print(f"Dinero restante después de todas las compras: {dinero_restante:.2f}")