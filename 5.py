notas = list(map(float, input("Ingrese las calificaciones separadas por comas: ").split(",")))

print("Promedio:", sum(notas) / len(notas))
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))
print("Aprobados:", sum(1 for n in notas if n >= 3.0))
