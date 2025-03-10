presupuesto = float(input("Ingrese el presupuesto inicial del chef: "))
vegetales = float(input("Ingrese el costo de los vegetales: "))
carne = float(input("Ingrese el costo de la carne: "))
especias = float(input("Ingrese el costo de las especias: "))
gasto_total = vegetales + carne + especias

if gasto_total <= presupuesto:
    frutas = float(input("Ingrese el costo de las frutas: "))
    gasto_total += frutas

dinero_restante = presupuesto - gasto_total

print(f"Dinero restante del chef: ${dinero_restante:.2f}")