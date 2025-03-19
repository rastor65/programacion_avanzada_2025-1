edad = int(input("Hola!, ingrese su edad por favor: "))
if edad >0 and  edad<=12:
    print("Usted es un niño")
    print("De los niños es el reino de los cielos!")
    if edad >=13 and edad <= 17 :
        print("Usted es un adolescente")
        print("Ninguno tenga en poco tu juventud, sino sé ejemlo...")
        if edad >=18 and edad <=64:
            print("Usted es un adulto")
            print("Teme a Dios y guarda sus mandamientos; porque esto es el todo del hombre")
            if edad >=65 and edad <=120:
                    print("Usted es un adulto mayor")
                    print("vuetros ancianos soñaran sueños,")
else:
    print("Información no valida...")
    print("Verifique su edad...")
