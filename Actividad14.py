def calificaciones():
    calificaciones = input("Ingrese las calificaciones de los estudiantes separadas por comas: ")
    calificaciones = [float(calificacion) for calificacion in calificaciones.split(',')]
    promedio = sum(calificaciones) / len(calificaciones)
    calificacion_maxima = max(calificaciones)
    calificacion_minima = min(calificaciones)
    estudiantes_aprobados = sum(1 for x in calificaciones if x >= 3.0)
    print(f"Promedio de calificaciones: {promedio:.2f}")
    print(f"Calificación más alta: {calificacion_maxima}")
    print(f"Calificación más baja: {calificacion_minima}")
    print(f"Número de estudiantes aprobados: {estudiantes_aprobados}")
calificaciones()