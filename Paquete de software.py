#Paquete de software
valor_licen = float(input("INgrese el valor de las licensia de software"))
presupuesto_escuela = float(input("Ingrese el prespuesto que tiene para las licencias"))
licencia_comprada =float(input("Ingrese la cantidad de licencias que desea comprar"))
total_de_compra = valor_licen * licencia_comprada
if total_de_compra == presupuesto_escuela or total_de_compra>presupuesto_escuela:
    print("No puede comprar licencias adicionales")
elif total_de_compra<presupuesto_escuela:
    presupuesto_restante = presupuesto_escuela - total_de_compra
    licencias_adicionales = presupuesto_restante // valor_licen
    print(f"Se puede comprar",{int(licencias_adicionales)} ,"licencias adicionales")