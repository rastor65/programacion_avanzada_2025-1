total_estudiantes = int(input("Ingrese el número total de estudiantes: "))
estudiantes_por_equipo = int(input("Ingrese la cantidad de estudiantes por equipo: "))
equipos_completos = total_estudiantes // estudiantes_por_equipo
print(f"Se pueden formar {equipos_completos} equipos completos.")               