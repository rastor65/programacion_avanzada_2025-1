def analizar_calificaciones(calificaciones):
    print(f"Promedio: {sum(calificaciones) / len(calificaciones):.2f}")
    print(f"Máxima: {max(calificaciones)} - Mínima: {min(calificaciones)}")
    print(f"Aprobados: {sum(cal >= 3.0 for cal in calificaciones)}")

calificaciones = list(map(float, input("Ingrese calificaciones separadas por comas: ").split(',')))
analizar_calificaciones(calificaciones)
