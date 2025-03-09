estudiante = int(input("cuantos estudiantes hay ? "))
lapices = 32
lapices_estudiante = lapices // estudiante
restos = lapices % estudiante
if restos == 0:
    print(f"se daran {lapices_estudiante} lapices por estudiante")
else:
    print(f"se daran {lapices_estudiante} lapices por estudiante y el profe se queda con {restos} ")