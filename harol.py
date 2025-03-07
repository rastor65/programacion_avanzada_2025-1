presupuesto = float(input("cuanto presupuesto tienes: "))
precioL = float(input("diga el costo de las licencias: "))
cantL = float(input("cual es la cantidad ? "))
total = precioL * cantL
add = presupuesto - total
if total >= presupuesto:
    print(f"no puedes comprar, no tienes plata ")
elif (total <= presupuesto) :
    print(f"el valor a pagar es de: {total}")
    print(f"te quedan {add} para comprar")
elif add < precioL:
    print(f"no puedes comprar porque te quedan {add}")    