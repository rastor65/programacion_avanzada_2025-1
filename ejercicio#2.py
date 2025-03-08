#Una empresa de tecnología vende un paquete de software por
#licencia. Y tiene una escuela como cliente, esta escuela planea
#comprar cierta cantidad de licencias, dependiendo de su
#presupuesto.

#Calcula y muestra cuántas licencias adicionales pueden comprar y en
#casodequenopuedan comprarmásadicionales, indícaselos.

presupuesto=float(input("Ingrese su presupuesto para comprar\n las licencias?:"))
cantidad=int(input("Cuantas licencias desea comprar?:"))
licencias=10000
x=presupuesto/licencias#cuantas puedo comprar
total=licencias*cantidad#total de plata
r=x-cantidad
if x<=cantidad:
  round(x)
  round(total)
  print(f"Ustedes solo pueden comprar en licencias: {x} y el total es de $:{total}")
  print(f"Sobre paso su presupusto pot:{r}")
elif x>cantidad:
  round(x)
  round(total)
  print(f"Las licencias que pueden comprar son:{x} y el total es de $:{total} ")
  print(f"Le falta por comprar:{r}")

