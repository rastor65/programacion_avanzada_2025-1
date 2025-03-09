estudiantes = int(input("Ingresa el número total de estudiantes:  "))
estudiantes_por_equipo = int(input("Ingresa la cantidad de estudiantes por equipo:   "))

equipos_completos = estudiantes // estudiantes_por_equipo


print(f"Se pueden formar {equipos_completos} equipos completos ")