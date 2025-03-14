def calcular_edad (edad):
    if edad < 0:
        return print("Edad no disponible.")
    if edad <= 12:
        return print("Eres un niño. Juega y diviertete.")
    elif edad <= 17:
        return print("Eres un adolecente. Enfocate en tus estudios.")
    elif edad <= 64:
        return print("Eres un adulto. Ordena tu vida.")
    else:
        return print("Eres un adulto mayor. Disfruta de tu hogar.")
        
edad = int(input("Ingrese su edad: "))
calcular_edad(edad)