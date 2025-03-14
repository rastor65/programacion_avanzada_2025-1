#-*- coding: utf-8 -*-

print("Ingrese su nombre")
nombre = input()
print("Buenos dias Chef, " + nombre)
presupuesto = float(input("Ingrese el presupuesto inicial del chef: "))

costo_vegetales = float(input("Ingrese el costo de los vegetales: "))
costo_carne = float(input("Ingrese el costo de la carne: "))
costo_especias = float(input("Ingrese el costo de las especias: "))


gasto_total = costo_vegetales + costo_carne + costo_especias

if gasto_total >presupuesto:
    print("Se exedio en el presupuesto")

if gasto_total < presupuesto:
    costo_frutas = float(input("Ingrese el costo de las frutas: "))
    gasto_total += costo_frutas if gasto_total + costo_frutas <= presupuesto else 0

dinero_restante = presupuesto - gasto_total

print(f"Dinero restante después de las compras: ${dinero_restante:.2f}")

