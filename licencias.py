presupuesto = float(input("Cuánto presupuesto tienes: "))
precioL = float(input("cuanto cuestan las licencias : "))
cantL = int(input("Cuál es la cantidad? "))
total = precioL * cantL
add = presupuesto - total
if total > presupuesto:
    print("No puedes comprar, no tienes suficiente presupuesto.")
else:
    print(f"El valor a pagar es de: {total}")
    print(f"Te quedan {add} para comprar.")
    licencias_adicionales = int(add // precioL)
    if licencias_adicionales > 0:
        print(f"Puedes comprar {licencias_adicionales} licencias adicionales.")
    else:
        print("No puedes comprar más licencias adicionales.")