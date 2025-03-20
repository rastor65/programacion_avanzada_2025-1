def notas():
    lista= input("Ingresa una lista de calificaciones: ")
    calificaciones = [float(nota) for nota in lista.split(",")]

    promedio = sum(calificaciones) / len(calificaciones)
    nota_max = max(calificaciones)
    nota_min = min(calificaciones)
    aprobar = sum(1 for nota in calificaciones if nota >= 3.0)

    print("El promedio de las notas es: ",promedio)
    print("Los estudiantes aprobados con nota 3.0 fueron : ",aprobar)
    print("La nota más alta fue: ",nota_max )
    print("La nota más baja fue: ",nota_min)
notas()