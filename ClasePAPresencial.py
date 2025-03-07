print("Hola, estamos vendiendo licencias...")

presupuesto = float(input("Ingrese su presupuesto: "))
cantidadLicencia = int(input("Cuantas licencias deseas comprar: "))

precioLicencia = 10
print(f"El precio de las licencias es: ${precioLicencia}")


Licencias1 = precioLicencia * cantidadLicencia
dineroRestante = Licencias1 - presupuesto 
CompraFutura = dineroRestante // precioLicencia 

if (presupuesto >= Licencias1 ) :
    print(f"Usted puede comprar: {Licencias1}")
    print(f"Usted puede comprar: {CompraFutura} más")
else:
   print("Usted no puede seguir comprando")



