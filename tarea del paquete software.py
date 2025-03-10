valor_licencia = float(input("Ingrese el valor de las licencias de software"))
presupuesto = float(input("Ingrese el presupuesto que tiene para las licencias"))
cantidad_licencias = float(input("Ingrese la cantidad de licencias que desea comprar"))
total_compra = valor_licencia * cantidad_licencias
if total_compra == presupuesto or total_compra > presupuesto:
    print("No puede comprar licencias adicionales")
elif total_compra < presupuesto:
    presupuesto_restante = presupuesto - total_compra
    licencias_adicionales = presupuesto_restante // valor_licencia
    print(f"Se pueden comprar {int(licencias_adicionales)} licencias adicionales")
exit()