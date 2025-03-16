presupuestos = float(input("cuanto es su presupuesto"))
verduras = float(input("ingrse cuanto costo las vegetales "))
carnes = float(input("ingrse cuanto costo las carnes "))
especias = float(input("ingrse cuanto costo las especias "))
presupuesto_total = verduras + carnes + especias
ress = presupuestos - presupuesto_total

if presupuesto_total <= presupuestos:
    print("usted puede comprar todo eso")
    print(f"la  cuenta fue de {presupuesto_total}")
    print(f"a usted le quedan {ress} para comprar mas cosas")
    frutas = float(input("ingrse cuanto costo las frutas "))
    ress2 = ress - frutas
    ress3 = presupuesto_total + frutas
    if ress2 >= 0:
        print(f"su cuenta con las las futas es de {ress3} y le sobran {ress2}")
    else:
        print("usted no puede comprar las frutas")
else:
    print("usted es pobre no puede comprar todo eso")