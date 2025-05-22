print("¡Hola profe!")
estudiantes = int(input("Cuantos estudiantes tiene usted?: "))

lapices= 32 

cantidad_lapices_por_estudiante = lapices // estudiantes 
lapices_para_el_profe= lapices % estudiantes

print(f"Son {cantidad_lapices_por_estudiante} por estudiante")
print(f"Al profe le quedan: {lapices_para_el_profe}")

if lapices_para_el_profe == 0:
    print("Lo siento profe, ya ha quedado sin lapices")
else:
    print("¡Profe!, deme otro lapices :D")