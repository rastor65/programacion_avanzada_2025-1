presupuesto = float (input("ingrese su presupuesto:"))
vegetales = float (input("ingrese la cantidad de dinero destinado para vegetales: "))
carne = float (input("ingrese la cantidad de dinero destinado para carnes: "))
especias = float (input("ingrese la cantidad de dinero destinada para las especias: "))
total_gasto = vegetales + carne + especias
if total_gasto < presupuesto: 
  print("puede comprar frutas")
elif total_gasto > presupuesto:
  print("no tiene dinero suficiente para comprar las frutas.")


   


