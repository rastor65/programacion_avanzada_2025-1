edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad <= 12:
    print("Eres niñp todavia. ¡Disfruta tu niñez y juega màs!")
elif edad >= 13 and edad <= 17:
    print("Eres un adolescente. ¡Piensa bien antes de tomar una desiciòn!")
elif edad >= 18 and edad <= 64:
    print("Eres un adulto. ¡Sigue adelante con tus sueños!")
elif edad >= 65:
    print("Eres un adulto mayor. ¡avanzaste mucho en la vida!")
else:
    print("Edad no válida.")
