total_Estuden = int(input("Ingrese la cantidad de estudiantes que hay en el salon: "))
total_Lapiz = 32
if total_Estuden == total_Lapiz or total_Estuden < total_Lapiz:
    print("Todos los estudiantes han obtenido un lapiz :) ")
elif total_Estuden > total_Lapiz:
    totalT = total_Estuden-total_Lapiz
    print(f"Haz entregado todos los lapices pero faltaron {totalT}  Estudiantes por lapices :( ")