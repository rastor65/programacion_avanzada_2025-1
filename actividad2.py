#1.
"""edad = int(input("Ingrese tu edad: "))

if edad <= 12:
    categoria = "Niño"
    mensaje = "Disfruta tu infancia"
elif edad <= 17:
    categoria = "Adolescente"
    mensaje = "persigas tus sueños"
elif edad <= 64:
    categoria = "Adulto"
    mensaje = "seas responsable"
else:
    categoria = "Adulto mayor"
    mensaje = "Los recuerdos son lo mas hermoso "

print(f"hola, Eres un {categoria}.quiero decirte que {mensaje}")"""


#2.
 
"""num = int(input("Ingrese un número: "))
forma = input("Elija el formato H o V ( H horizontal o V vertical): ")

for i in range(1, 13):
    if forma.upper() == "H":
        print(f"{num} x {i} = {num * i}", end=" | ")
    else:
        print(f"{num} x {i} = {num * i}")"""

#3.
""""
def primo(numero):
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return numero > 1

numero = int(input("Ingrese un número: "))
print("Es primo" if primo(numero) else "No es primo")"""

#4.
"""pares = []
suma = 0

for i in range(1, 21):
    pares.append(i * 2)
    suma += i * 2

print(pares)
print("Suma:", suma)"""

#5.

"""calificaciones = input("Ingresa las calificaciones pero separadas por comas: ").split(",")
calificaciones = [float(nota) for nota in calificaciones]

suma = 0
maxima = calificaciones[0]
minima = calificaciones[0]
aprobados = 0

for nota in calificaciones:
    suma += nota
    if nota > maxima:
        maxima = nota
    if nota < minima:
        minima = nota
    if nota >= 3.0:
        aprobados += 1


print("estas son las calificaciones:", calificaciones)
print("Promedio:", suma / len(calificaciones))
print("Máxima:", maxima)
print("Mínima:", minima)
print("Aprobados:", aprobados)"""

#6.

"""import random

def g_contrasena(longitud):
    caracteres = "abcABC123!@#"
    contrasena = ""
    for _ in range(longitud):
        contrasena += random.choice(caracteres)
    return contrasena

longitud = int(input("Ingresa la longitud de la contraseña: "))
print("Contraseña :", g_contrasena(longitud))"""