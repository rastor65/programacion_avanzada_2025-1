def clasificar_edad():
    edad = int(input("Ingrese su edad: "))

    if edad < 0:
        print("La edad no puede ser negativa.")
    elif edad <= 12:
        print("Usted es un niño.")
        print("No te rindas, sigue aprendiendo y explorando el mundo.")
    elif edad <= 17:
        print("Usted es un adolescente.")
        print("La vida es un desafío emocionante, ¡disfrútala!")
    elif edad <= 64:
        print("Usted es un adulto.")
        print("No dejes de soñar y trabajar hacia tus objetivos.")
    else:
        print("Usted es un adulto mayor.")
        print("Disfruta de la vida, comparte tus experiencias y sabiduría con los demás.")

clasificar_edad()