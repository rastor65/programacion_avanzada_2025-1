presupuestoI= float(input("Presupuesto: "))
gasto1= sum(float(input(c)) for c in ["Vegetales: ", "Carne: ", "Especias: "])
gasto1 += float(input("Frutas: ")) if gasto1 <= presupuestoI else 0
print(f"Dinero restante: {presupuestoI - gasto1:.2f}")
