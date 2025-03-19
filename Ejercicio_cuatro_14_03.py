def gen_pares(n):
    pares = [i * 2 for i in range(1, n + 1)] 
    suma_total = sum(pares)  
    return pares, suma_total
numeros_pares, suma = gen_pares(20)
print("Lista de los primeros 20 números pares:", numeros_pares)
print("Suma total de los números pares:", suma)
