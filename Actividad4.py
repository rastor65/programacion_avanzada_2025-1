cantidad_lapices = int (input("ingrese la cantidad de lapices que tiene: "))
estudiantes = int (input("ingrese la cantidad de estudiantes que hay: ")) 
lapices_sobrantes =  cantidad_lapices % estudiantes 
print(f"sobran {lapices_sobrantes} lapices")
