#Actividad en clase
def solicitar_monto(mensaje):
    while True:
        try:
            monto = float(input(mensaje))
            entrada = input(mensaje).replace(".", "")
            if monto <= 0:
                print("Por favor, ingrese un monto valido.")
            else:
                return monto
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

Presupuesto = solicitar_monto(input("Iintroduzca el presupuesto para las compras que va realizar  "))
gasto_en_vegetales = float(input("Ingrese cuanto dinero se va gastar en vegetales "))
gasto_en_carne = float(input("Ingres cuanto dinero se va gastar en carne "))
gasto_en_especia = float(input("Ingrese cuanto dinero se gastara en especias "))

Gasto_total = gasto_en_carne + gasto_en_vegetales + gasto_en_especia

if Gasto_total > Presupuesto:
    print(f"Usted ha excedido su presupuesto en ${Gasto_total - Presupuesto:.2f}. Revise sus gastos.")
elif Gasto_total == Presupuesto:
    print("Ha utilizado exactamente su presupuesto. No puede comprar nada más.")
else:
    presupuesto_restante = Presupuesto - Gasto_total
    print(f"Usted puede seguir comprando. Le quedan ${presupuesto_restante:.2f} disponibles.")
    
exit()