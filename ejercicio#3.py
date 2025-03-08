#Un grupo de estudiantes necesita dividirse en equipos. Pídele al usuario
#que ingrese el número total de estudiantes y cuántos estudiantes debe
#haberporequipo.

#Calculaymuestracuántosequipos completos sepueden formar.
estudiantes=int(input("Ingrese el numero de estudiantes: "))
equipo=float(input("Cuantos estudiantes deberia haber por equipo"))
R=estudiantes//equipo
N=round(R)
print(f"El numero de estudiantes por equipo es: {N}")
