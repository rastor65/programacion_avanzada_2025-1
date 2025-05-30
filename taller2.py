
presupuesto = float(input("Ingrese el presupuesto inicial del chef: "))
vegetales = float(input("Ingrese el costo de los vegetales: "))
carne = float(input("Ingrese el costo de la carne: "))
especias = float(input("Ingrese el costo de las especias: "))
frutas = float(input("Ingrese el costo de las frutas (si el presupuesto lo permite): "))
total_gastos = vegetales + carne + especias
if total_gastos + frutas <= presupuesto:
    total_gastos += frutas
    print("El chef puede comprar frutas.")
else:
    print("El chef no puede comprar frutas.")
dinero_restante = presupuesto - total_gastos
print(f"Dinero restante después de las compras: ${dinero_restante:.2f}")