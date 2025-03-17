#Escribe un programa que solicite la edad del usuario e indique si es niño
#(0-12 años), adolescente (13-17 años), adulto (18-64 años) o adulto
#mayor (65+ años). Además, imprime un mensaje motivacional acorde a
#laedad.

while True:
    edad=int(input("Ingrese su edad:"))
    #terminar=input("digite fin para terminar o enter para continuar:")
    #if terminar.lower()=='fin':
     #   break
    
    

    

    if edad>=0 and edad <=12:
        print(f"NIÑO:{edad}\n 'tiene una vida por delante' ")

    elif edad>=13 and edad <=17:
        print(f"ADOLECENTE:{edad}\n 'enfocarse en que quiere en la vida' ")

    elif edad >=18 and edad <=64:
        print(f"adulto:{edad}\n 'Espero haya logrado sus metas' ")

    elif edad >=65:
        print(f"adulto mayor:{edad}\n 'usted es un ejemplo a seguir' ")

    

    else:
        print("opcion no valida: ")

    terminar=input("digite fin para terminar o enter para continuar:")
    if terminar.lower()=='fin':
        break


