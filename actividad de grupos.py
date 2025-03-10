total_estudiantes = int(input("Ingrese el número de estudiantes que hay en el curso "))
integrantes_por_grupo = int(input("Ingrese el número de integrantes que tiene que tener cada grupo"))
total_grupos = total_estudiantes // integrantes_por_grupo
print("El número de grupos completos que pueden haber son: ", total_grupos)
