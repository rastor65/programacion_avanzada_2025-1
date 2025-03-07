def calcular_equipos_completos():
    # Ingresar número total de estudiantes
    total_estudiantes = int(input("Ingrese el número total de estudiantes: "))

    # Ingresar número de estudiantes por equipo
    estudiantes_por_equipo = int(input("Ingrese el número de estudiantes por equipo: "))

    # Calcular número de equipos completos
    equipos_completos = total_estudiantes // estudiantes_por_equipo

    # Mostrar resultado
    print(f"Se pueden formar {equipos_completos} equipos completos.")

calcular_equipos_completos()