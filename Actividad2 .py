def calcular_licencias_adicionales():
    # Ingresar presupuesto disponible
    presupuesto_disponible = float(input("Ingrese el presupuesto disponible: "))

    # Ingresar costo de cada licencia
    costo_licencia = float(input("Ingrese el costo de cada licencia: "))

    # Ingresar número de licencias ya compradas
    licencias_compradas = int(input("Ingrese el número de licencias ya compradas: "))

    # Calcular número de licencias adicionales que se pueden comprar
    if presupuesto_disponible >= costo_licencia:
        licencias_adicionales = int(presupuesto_disponible / costo_licencia)
        print(f"La escuela puede comprar {licencias_adicionales} licencias adicionales.")
    else:
        print("La escuela no puede comprar licencias adicionales.")

calcular_licencias_adicionales()