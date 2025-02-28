precio_licencia = 60000  
presupuesto_escuela = 100000 
licencias_compradas = 20 


dinero_gastado = licencias_compradas * precio_licencia

dinero_disponible = presupuesto_escuela - dinero_gastado

licencias_adicionales_posibles = int(dinero_disponible / precio_licencia) 

print(f"Precio por licencia: ${precio_licencia}")
print(f"Presupuesto total de la escuela: ${presupuesto_escuela}")
print(f"Licencias ya compradas: {licencias_compradas}")
print(f"Dinero ya gastado: ${dinero_gastado}")
print(f"Dinero disponible: ${dinero_disponible}")

if licencias_adicionales_posibles > 0:
    print(f"La escuela puede comprar {licencias_adicionales_posibles} licencias adicionales.")
    print(f"Esto costaría ${licencias_adicionales_posibles * precio_licencia}")
    print(f"Quedaría un saldo de ${dinero_disponible - (licencias_adicionales_posibles * precio_licencia)}")
else:
    print("La escuela no puede comprar licencias adicionales con el presupuesto actual.")