#Pagina 30
comentario_=(input("Ingrese el comentario del cliente: "))
minus_= comentario_.lower()
contar_= comentario_.count("excelente")
espacio_= comentario_.strip()

if minus_ == comentario_ :
    print("El texto se encuentra en minusculas")
else:
    print("El texto en minusculas es: ",minus_)

print("El numero de veces que se repite 'excelente' es: ",contar_)