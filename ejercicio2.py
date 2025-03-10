presupuesto = float(input("Ingrese el presupuesto de la escuela: "))
costo_licencia = float(input("Ingrese el costo de una licencia: "))
licencias_compradas = presupuesto // costo_licencia  
dinero_restante = presupuesto % costo_licencia  
print(f"La escuela puede comprar {int(licencias_compradas)} licencias.")
if dinero_restante < costo_licencia:
    print("No pueden comprar más licencias adicionales.")