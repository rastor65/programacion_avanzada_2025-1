num_estuden = int(input("INgrese el numero de estudiantes que hay en el curso "))
integ_x_grupo =int(input("Ingrese el numero de integrantes que tiene que tener cada grupo"))
num_grups = num_estuden // integ_x_grupo
print("El numero de grupos completos que pueden haber son: ",num_grups)
#por si el quedan estudiantes por fuera de los grupos completos se usa num_studen % num_grups para mostrar cuantos quedan por fuera