# def clasificar_edad():
#     edad = int(input("Ingresa tu edad: "))
    
#     if edad <= 12:
#         print("Eres un niño. ¡Sigue explorando y aprendiendo cosas nuevas!")
#     elif edad <= 17:
#         print("Eres un adolescente. ¡Es un gran momento para descubrir tus pasiones!")
#     elif edad <= 64:
#         print("Eres un adulto. ¡Sigue creciendo y alcanzando tus metas!")
#     else:
#         print("Eres un adulto mayor. ¡Disfruta de la sabiduría y la tranquilidad!")

# clasificar_edad()

# def tabla_multiplicar():
#     numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
#     formato = input("¿Quieres la tabla en formato horizontal (H) o vertical (V)? ").strip().upper()

#     if formato == "H":
#         print(" - ".join([f" | {numero} x {i} = {numero * i} |" for i in range(1, 13)]))
#     else:
#         for i in range(1, 13):
#             print(f"{numero} x {i} = {numero * i}")

# tabla_multiplicar()

import math

def es_primo (numero):
    if numero <= 1:
        return False
    for i in range (2, int(math.sqrt(numero) +1)):
        if numero % i == 0:
            return False
    return True

def imprimir_numeros_primos (limite):
    for i in range (2, limite + 1):
        if es_primo(i):
            print(i)

numero = int(input("Ingresa el numero: "))
imprimir_numeros_primos(numero)


# def es_primo(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

# numero = int(input("Ingresa un número para verificar si es primo: "))
# print(f"El número {numero} {'es primo' if es_primo(numero) else 'no es primo'}.")


# pares = [i for i in range(2, 41, 2)]
# suma_pares = sum(pares)

# print("Lista de los primeros 20 números pares:", pares)
# print("Suma total de los números pares:", suma_pares)


# def analizar_calificaciones():
#     calificaciones = list(map(float, input("Ingresa las calificaciones separadas por comas: ").split(",")))

#     promedio = sum(calificaciones) / len(calificaciones)
#     nota_max = max(calificaciones)
#     nota_min = min(calificaciones)
#     aprobados = sum(1 for nota in calificaciones if nota >= 3.0)

#     print(f"Promedio: {promedio:.2f}")
#     print(f"Nota más alta: {nota_max}")
#     print(f"Nota más baja: {nota_min}")
#     print(f"Cantidad de estudiantes aprobados: {aprobados}")

# analizar_calificaciones()


# import random
# import string

# def generar_contraseña(longitud=12):
#     caracteres = string.ascii_letters + string.digits + string.punctuation
#     contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
#     return contraseña

# longitud = int(input("Ingresa la longitud de la contraseña: "))
# print("Tu contraseña segura es:", generar_contraseña(longitud))

