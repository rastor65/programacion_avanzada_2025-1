def pares(n):
    return [i for i in range(2, 2 * n + 1, 2)]
def suma(lista):
    return sum(lista)
numeros_pares = pares(20)
suma_pares = suma(numeros_pares)
print("los primeros 20 números pares son:", numeros_pares)
print("el resultado de la Suma de los números pares es:", suma_pares)

