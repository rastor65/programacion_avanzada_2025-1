notas = (input("Hola profe, ingresa las notas de tus estudiantes: "))

notas_separadas = list(map(float, notas.split(', ')))

cantidadDeNotas=len(notas_separadas)
Suma=sum(notas_separadas)

promedio = Suma/cantidadDeNotas

notaAlta=max(notas_separadas)
notaBaja=min(notas_separadas)

aprobados=sum(1 for notas in notas_separadas if notas >= 3.0)
    
print(f"El promedio es: {promedio}")
print(f"La calificacion mas alta es: {notaAlta}")
print(f"La calificacion mas baja es: {notaBaja}")
print(f"Los aprobados son: {aprobados}")