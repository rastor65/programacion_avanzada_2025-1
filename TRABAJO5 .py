# Solicitar al usuario que ingrese una lista de calificaciones separadas por comas
calificaciones_input = input("Ingrese una lista de calificaciones separadas por comas: ")

# Convertir la entrada en una lista de números flotantes
calificaciones = [float(cal) for cal in calificaciones_input.split(",")]

# Calcular el promedio de calificaciones
promedio = sum(calificaciones) / len(calificaciones)

# Encontrar la calificación más alta y la más baja
calificacion_max = max(calificaciones)
calificacion_min = min(calificaciones)

# Contar cuántos estudiantes aprobaron (nota mínima de 3.0)
estudiantes_aprobados = sum(1 for cal in calificaciones if cal >= 3.0)

# Mostrar los resultados
print(f"Promedio de calificaciones: {promedio:.2f}")
print(f"Calificación más alta: {calificacion_max}")
print(f"Calificación más baja: {calificacion_min}")
print(f"Cantidad de estudiantes aprobados: {estudiantes_aprobados}")