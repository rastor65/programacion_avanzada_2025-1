    lista_calificaciones = []
    lista = cadena.split(",")
    for i in range(0, len(lista)):
        lista_calificaciones.append(float(lista[i].strip()))
    return lista_calificaciones
def main(lista):
    print(f"El promedio de la clase es: {calcular_promedio(lista)}\nLa nota más alta: {nota_mas_alta(lista)}\nLa nota mas baja: {nota_mas_baja(lista)}")
    print(f"Cantidad de estudiantes que aprobaron: {estudiantes_aprobados(lista)}")
calificaciones = input("Ingrese las calificaciones separadas por comas: ").strip()
main(convertir_str_a_lista(calificaciones))
"""

"""
#6.

import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena
longitud = int(input("Ingresa la longitud de la contraseña: "))
if longitud < 4:
    print("Ingresa una longitud minimo de 4 caracteres.")
else:
    print(f"Contraseña generada: {generar_contrasena(longitud)}")  
""
