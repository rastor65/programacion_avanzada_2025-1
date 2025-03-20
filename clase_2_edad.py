def año():
    edad = int(input("Ingrese su edad: "))

    if edad <= 12:
        print("Usted es un niño")
        print("Te falta mucho por crecer")
    elif edad <= 19:
        print("Estas en la pubertad")
        print("Estas entrando en la vida adulta :)")
    elif edad < 65:
        print("Eres mayor de edad. Animo, la vida es dura")
    else:
        print ("Eres de la 3era edad, estás viejo :( ")
año()
