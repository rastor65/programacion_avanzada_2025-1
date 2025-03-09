#pagina 26
estudiantes= (int(input("¿Cuantos estudiantes hay? ")))
equipos= (int(input("¿Cuantos estudiantes tienen que haber por equipo? ")))

if equipos > 0 and estudiantes > 0:
    div= int(estudiantes/equipos)
    print("Se pueden formar equipos de ",div)
else:
    print("No se puede dividir entre 0, ingrese otro valor")