presupuestos = float(input("cuanto es su presupuesto"))
verduras = float(input("ingrse cuanto costo las futas "))
carnes = float(input("ingrse cuanto costo las futas "))
especias = float(input("ingrse cuanto costo las futas "))
presupuesto_total = verduras + carnes + especias
if presupuesto_total <= presupuestos:
    print("usted puede comprar todo eso")
else:
    print("usted es pobre no puede comprar todo eso")