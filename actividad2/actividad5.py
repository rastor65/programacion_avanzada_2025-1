nota_general = []
nota_minima = 3.0

while True:
    notas = input("Ingrese las notas de sus estudiantes, separadas por comas: ")
    notas = [float(nota.strip()) for nota in notas.split(",")]
    nota_general.extend(notas)
    
    for nota in notas:
        if nota < nota_minima:
            print(f"Nota {nota}: Perdiste la materia")
        else:
            print(f"Nota {nota}: Ganaste la materia")

    promedio = sum(nota_general) / len(nota_general)
    print(f"El promedio de nota es de: {promedio:.2f}")
    print(f"La nota más alta es de: {max(nota_general)}")
    
    aprobados = sum(1 for n in nota_general if n >= nota_minima)
    print(f"La cantidad de aprobados es de: {aprobados}")
    
    op = input("¿Quieres seguir? (si/no): ").strip().lower()
    if op == "no":
        print("Saliendo del programa....")
        break