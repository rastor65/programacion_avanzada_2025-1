def generar_pares(n):
    return [i * 2 for i in range(n)]

def suma_lista(lista):
    return sum(lista)

def main():
    numeros_pares = generar_pares(20)
    suma_total = suma_lista(numeros_pares)

    print("Lista de los primeros 20 números pares:", numeros_pares)
    print("Suma total:", suma_total)

main()
