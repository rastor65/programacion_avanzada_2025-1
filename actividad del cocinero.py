presupuesto_total = float(input("Ingrese el presupuesto para las compras que va realizar  "))
gasto_en_vegetales = float(input("Ingrese cuanto dinero se va gastar en comprar los vegetales "))
gasto_en_carnes = float(input("Ingrese cuanto dinero se va gastar en comprar las carnes "))
gasto_en_especias = float(input("Ingrese cuanto dinero se gastara en las especias "))
gasto_total = gasto_en_carnes + gasto_en_vegetales + gasto_en_especias
if gasto_total == presupuesto_total or gasto_total > presupuesto_total:
    print("Usted no puede comprar nada más, regrese la próxima")
elif gasto_total < presupuesto_total:
    print("Usted puede comprar frutas")
exit()