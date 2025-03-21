def tabla_de_multiplicar():
   num = int(input("Ingrese un numero del 1 al 12 para su tabla de multiplicar: "))
   format = input("ingrese en que formato desea imprimir su tabla de multiplicar, horizontal (h) o vertical (v): ").strip().lower()
   if format == 'h':
    tabla_horizontal(num)
   elif format == 'v':
    tabla_vertical(num)
def tabla_horizontal(num):
    print(f"Tabla de multiplicar del {num} horizontal:")
    for i in range(1, 11):
      print(f"{num} x {i} = {num * i}", end="\t")
def tabla_vertical(num):
    print(f"Tabla de multiplicar del {num} vertical:")
    for i in range(1, 11):
      print(f"{num} x {i} = {num * i}")
tabla_de_multiplicar()
