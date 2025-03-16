def año():
    while True:
        op = input("¿Quieres seguir? (s/n): ")
        if op == "n":
            print("Saliendo del programa...")
            break
        elif op != "s":
            
            continue
        
        edad = int(input("Ingrese su edad: "))
        if edad < 0:
            print("Por favor, ingrese una edad válida.")
        elif edad <= 12:
            print("Usted es un niño todavía.")
            print("Eres bastante joven, aprovecha.")
        elif edad <= 17:
            print("Usted es adolescente.")
            print("Estás empezando a vivir la vida, disfrútala.")
        elif edad <= 64:
            print("Usted es un adulto.")
            print("Ya eres una persona con experiencia.")
        elif edad >= 65:
            print("Usted es un adulto mayor.")
            print("Ya usted es un veterano de la vida.")

año()