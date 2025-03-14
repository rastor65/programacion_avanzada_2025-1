total_Estudiantes = int(input("Ingrese la cantidad de estudiantes que hay en el salon: "))
total_Lapiz = 32
if total_Estudiantes == total_Lapiz or total_Estudiantes < total_Lapiz:
    print("Todos los estudiantes han obtenido un lapiz ")
elif total_Estudiantes > total_Lapiz:
    totalT = total_Estudiantes - total_Lapiz
    print(f"Haz entregado todos los lapices pero faltaron {totalT}  Estudiantes por lapices ")
lapices_sobrantes = total_Lapiz - total_Estudiantes
if lapices_sobrantes >= 0:
    print(f"sobran {lapices_sobrantes} lapices ")