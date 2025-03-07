def calcular_presupuesto():
    # Ingresar presupuesto inicial
    presupuesto_inicial = float(input("Ingrese el presupuesto inicial: "))

    # Ingresar gastos en vegetales, carne y especias
    gasto_vegetales = float(input("Ingrese el gasto en vegetales: "))
    gasto_carne = float(input("Ingrese el gasto en carne: "))
    gasto_especias = float(input("Ingrese el gasto en especias: "))

    # Calcular gasto total
    gasto_total = gasto_vegetales + gasto_carne + gasto_especias

    # Verificar si se puede agregar frutas
    if gasto_total <= presupuesto_inicial:
        gasto_frutas = float(input("Ingrese el gasto en frutas: "))
        gasto_total += gasto_frutas

    # Calcular dinero restante
    dinero_restante = presupuesto_inicial - gasto_total

    # Mostrar resultado
    print(f"Dinero restante: ${dinero_restante:.2f}")

calcular_presupuesto()