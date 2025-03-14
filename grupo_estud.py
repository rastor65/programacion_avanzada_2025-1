num_estudiantes = int(input("INgrese el numero de estudiantes que hay en el curso "))
integ_x_grupo =int(input("Ingrese el numero de integrantes que tiene que tener cada grupo"))
num_grups = num_estudiantes // integ_x_grupo
estudiantes_sobrantes = num_estudiantes % integ_x_grupo
print(f"El número de grupos completos que pueden haber es: {num_grups}")
if estudiantes_sobrantes > 0:
    print(f"Quedan {estudiantes_sobrantes} estudiante(s) sin asignar a un grupo.")
else:
    print

