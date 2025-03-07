def calcular_lapices_sobrantes():
    # Ingresar número total de lápices
    total_lapices = int(input("Ingrese el número total de lápices: "))

    # Ingresar número de estudiantes
    numero_estudiantes = int(input("Ingrese el número de estudiantes: "))

    # Calcular lápices sobrantes
    lapices_sobrantes = total_lapices % numero_estudiantes

    # Mostrar resultado
    print(f"Le sobran {lapices_sobrantes} lápices.")

calcular_lapices_sobrantes()