presupuestoI = float(input("Presupuesto: "))
costo_licencias = float(input("Costo licencia: "))
cantidad = int(input("Licencias que quieren comprar: "))

otros_mas = int(presupuestoI // costo_licencias)
total = cantidad + otros_mas

print("le alcanza", total, "licencias en total y pueden comprar", otros_mas, "más.")
