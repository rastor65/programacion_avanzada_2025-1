numero_estudiantes=int (input("Ingrese el numero total de estudiantes"))
equipo= int(input("Cuantos estudiantes debe haber por equipo?"))

equipos_totales= numero_estudiantes //equipo

sin_equipo= numero_estudiantes % equipo

print(f"El numero total de es {equipos_totales} equipos_totales.  ")

print(f"Los estudiantes que quedan sin equipo son: {sin_equipo} ")