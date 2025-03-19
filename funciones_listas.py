"""
1.Clasificación por edad con mensajes personalizados

Escribe un programa que solicite la edad del usuario e indique si es niño
(0-12 años), adolescente (13-17 años), adulto (18-64 años) o adulto
mayor (65+ años). Además, imprime un mensaje motivacional acorde a
laedad.

def imprimir_edad (edad):
    if edad < 0:
        return print("Edad no disponible.")
    if edad <= 12:
        return print("Eres un niño. Juega y diviertete.")
    elif edad <= 17:
        return print("Eres un adolecente. Enfocate en tus estudios.")
    elif edad <= 64:
        return print("Eres un adulto. Ordena tu  vida.")
    else:
        return print("Eres un adulto mayor. Disfruta de tu hogar.")
        
edad = int(input("Ingrese su edad: "))
imprimir_edad(edad)
"""

"""
2. Generador de tablas de multiplicar personalizadas

Pide al usuario un número y genera su tabla de multiplicar del 1 al 12.
Permite al usuario decidir si la tabla se imprime en formato horizontal o
vertical.

def imprimir_tabla_de_multiplicar(numero, orientacion):
    if orientacion == 1:
        for i in range(1, 13):
            print(f"{numero} X {i} = {numero*i}")
    else:
        tabla = []
        for i in range(1, 13):
            tabla.append(f"{numero} X {i} = {numero*i}")
        print("  ".join(tabla))    
numero = int(input("Ingresa un numero: "))
if numero > 0:
    orientacion = int(input("1. Vertical.\n2. Horizontal.\n"))
    if orientacion == 1 or orientacion == 2:
        imprimir_tabla_de_multiplicar(numero, orientacion)
    else:
        print("Opcion incorrecta.")
else:
    print("Numero no valido.")
"""

"""
3. Verificació de números primos con optimización

Crea una función que reciba un número y determine si es primo.
Optimiza el código para que no tenga que comprobar todos los
números hasta n,sino solo hasta su raíz cuadrada.

import math
def es_primo(numero):
    if numero <= 1:
        return print(f"{numero} no es primo.")
    for i in range(2, int(math.sqrt(numero))+1):
        if numero%i == 0:
            return print(f"{numero} no es primo.")
    return print(f"{numero} es primo.")
numero = int(input("Ingresa un numero: "))
es_primo(numero)
"""

"""
4. Lista de los primeros 20 números pares con suma total

Genera una lista con los primeros 20 números pares y luego muestra la
lista junto con la suma de todos sus elementos.

def imprimir_numeros_pares(limite):
    numeros_pares = []
    for i in range(1,limite + 1):
        numeros_pares.append(i*2)
    print(numeros_pares)
    sumar(numeros_pares)

def sumar(lista):
    return print(f"Sumatoria: {sum(lista)}")

imprimir_numeros_pares(6)
"""

"""
5. Análisis de una lista de calificaciones

Pide al usuario ingresar una lista de calificaciones de estudiantes
(separadas por comas) y luego calcula:
El promedio de calificaciones.
La calificación más alta y la más baja.
Cuántos estudiantes aprobaron(nota mínima de 3.0).


def calcular_promedio(lista):
    return sum(lista)/len(lista)
def nota_mas_alta(lista):
    return max(lista)
def nota_mas_baja(lista):
    return min(lista)
def estudiantes_aprobados(lista):
    aprobados = 0
    for i in range(0, len(lista)):
        if lista[i] >= 3.0:
            aprobados += 1
    return aprobados
def convertir_str_a_lista(cadena):
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
Diseña una función que genere contraseñas seguras de una longitud
dada. La ontraseña debe incluir letras mayúsculas, minúsculas, números
y símbolos especiales.

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
"""