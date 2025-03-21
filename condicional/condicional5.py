def obtener_calificaciones():
    entrada = input("Ingresa las calificaciones de los estudiantes separadas por comas (Ej: 3.5,4.2,2.8): ")
    # Convertir entrada en una lista de números flotantes
    try:
        calificaciones = [float(calif.strip()) for calif in entrada.split(',')]
        return calificaciones
    except ValueError:
        print("Error: Asegúrate de ingresar solo números separados por comas.")
        return obtener_calificaciones()  # Recursión para volver a intentarlo

def calcular_estadisticas(calificaciones):
    # Promedio
    promedio = sum(calificaciones) / len(calificaciones)
    
    # Calificación más alta y más baja
    calificacion_maxima = max(calificaciones)
    calificacion_minima = min(calificaciones)
    
    # Conteo de aprobados (nota mínima de 3.0)
    aprobados = sum(1 for calif in calificaciones if calif >= 3.0)
    
    return promedio, calificacion_maxima, calificacion_minima, aprobados

# Programa principal
print("Análisis de Calificaciones de Estudiantes")
print("-----------------------------------------")

# Obtener las calificaciones
calificaciones = obtener_calificaciones()

# Calcular estadísticas
if calificaciones:
    promedio, maxima, minima, aprobados = calcular_estadisticas(calificaciones)
    
    # Mostrar resultados
    print(f"\nResultados del análisis:")
    print(f"- Número total de estudiantes: {len(calificaciones)}")
    print(f"- Promedio de calificaciones: {promedio:.2f}")
    print(f"- Calificación más alta: {maxima:.2f}")
    print(f"- Calificación más baja: {minima:.2f}")
    print(f"- Estudiantes aprobados: {aprobados} ({(aprobados/len(calificaciones)*100):.1f}%)")