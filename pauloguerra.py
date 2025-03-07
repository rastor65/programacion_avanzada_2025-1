

presupuesto = float(input("ingrese el presupuesto: "))
licencias = int(input("ingrese la cantidad de licencias: "))

preciolicencia = 100


licenciasadquiridas = presupuesto // licencias

if (presupuesto >=licencias) :
  print(f"cada licencia te sale en  : {preciolicencia} ")
else:
  print("no cuenta con el presupuesto para adquirir esa cantidad de licencias")