def analizar_calificaciones(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)  
    nota_max = max(calificaciones)  
    nota_min = min(calificaciones)  
    aprobados = sum(1 for nota in calificaciones if nota >= 3.0) 
    return promedio, nota_max, nota_min, aprobados
entrada = input("Ingrese las calificaciones separadas por comas: ")
calificaciones = [float(nota) for nota in entrada.split(",")] 
promedio, nota_max, nota_min, aprobados = analizar_calificaciones(calificaciones)
print(f"Promedio de calificaciones: {promedio:.2f}")
print(f"Calificación más alta: {nota_max}")
print(f"Calificación más baja: {nota_min}")
print(f"Número de estudiantes aprobados: {aprobados}")
