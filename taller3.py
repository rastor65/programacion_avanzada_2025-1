
costo_licencia = float(input("Ingrese el costo de cada licencia: "))
presupuesto = float(input("Ingrese el presupuesto total de la escuela: "))
licencias_base = int(input("Ingrese la cantidad base de licencias que desea comprar la escuela: "))
costo_base = licencias_base * costo_licencia
if costo_base > presupuesto:
    print("El presupuesto no alcanza para comprar la cantidad base de licencias.")
else:
    sobrante = presupuesto - costo_base
    licencias_adicionales = int(sobrante // costo_licencia)
    
    if licencias_adicionales > 0:
        print(f"La escuela puede comprar {licencias_adicionales} licencias adicionales.")
    else:
        print("La escuela no puede comprar licencias adicionales.")