#Actividad en clase
Presupuesto = float(input("Ingrese el presupuesto para las compras que va realizar  "))
gasto_en_vegetales = float(input("Ingrese cuanto dinero se va gastar en comprar los vegetales "))
gasto_en_carne = float(input("Ingres cuanto dinero se va gastar en comprar las carnes "))
gasto_en_especia = float(input("Ingrese cuanto dinero se gastara en las especias "))
total_de_Gasto = gasto_en_carne + gasto_en_vegetales + gasto_en_especia
if total_de_Gasto == Presupuesto or total_de_Gasto>Presupuesto:
    print("Usted no puede comprar nada más, regrese la proxima")
elif total_de_Gasto<Presupuesto:
    print("Usted puede comprar frutas")
exit()