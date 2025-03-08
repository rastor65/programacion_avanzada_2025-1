#Un profesor quiere dividir 32 lápices entre todos los estudiantes de su
#grupoyquieresabercuántoslápiceslesobran.

#¿Cuántos lápices lesobranalprofesor?
grupo=int(input("Ingrese el numero de estudiantes: "))
lapices=32
R=grupo%lapices
N=lapices-R
if R<=lapices:
 
 print(f"La cantidad de lapices son: {N}")
 print(f"sobran: {R}")
elif R>=lapices:
   print(f"No sobraron lapices y faltan: {R}")
   print(f"faltan: {N}")
