Coments = input("Ingrese el comentario que desea dejar: ")
if len(Coments) == 0:
    return Coments
    print("El comentario no puede estar vacío. Por favor, intente de nuevo.")
else:
    Coments = input("Ingrese el comentario que desea dejar: ")
Coments = Coments.strip()
Cont_Exelente = Coments.count("excelente")
print("El comentario que dejo es el siguiente: ",Coments)
print(f"Repitio la palabra Excelente {Cont_Exelente} veces")
