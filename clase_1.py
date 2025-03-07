def calcular_licencias_adicionales(precio_licencia, presupuesto, licencias_compradas):
    costo_total = licencias_compradas * precio_licencia
    presupuesto_restante = presupuesto - costo_total
    
    if presupuesto_restante >= precio_licencia:
        licencias_adicionales = presupuesto_restante // precio_licencia
        return f"Con el presupuesto restante, la escuela puede comprar {licencias_adicionales} licencias adicionales."
    else:
        return "La escuela no tiene suficiente presupuesto para comprar licencias adicionales."

presupuesto = float(input("Introduce el presupuesto total de la escuela: "))
precio_licencia = float(input("Introduce el costo de una licencia: "))
licencias_compradas = int(input("Introduce la cantidad de licencias que la escuela planea comprar: "))

resultado = calcular_licencias_adicionales(precio_licencia, presupuesto, licencias_compradas)
print(resultado)
