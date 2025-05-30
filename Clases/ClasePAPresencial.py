print("Hola, estamos vendiendo licencias...")

presupuesto = float(input("Ingrese su presupuesto?: $"))
cantidadLicencia = int(input("Cuantas licencias deseas comprar?: "))
precioLicencia = float(input("Cuanto cuesta la licencia?: $"))

Licencias1 = precioLicencia * cantidadLicencia
dineroRestante = presupuesto - Licencias1 
CompraFutura = dineroRestante // precioLicencia

if (presupuesto >= Licencias1 ):
    print(f"¡Felicidades, usted compro: {cantidadLicencia}!")
    print(f"A usted le quedan ${dineroRestante}")
    print(f"Usted puede comprar: {CompraFutura} más")
else:
    print("Usted no puede comprar, lo lamento...")



