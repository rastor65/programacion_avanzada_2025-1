def generar_numeros_pares(cantidad):
    return [2 * i for i in range(1, cantidad + 1)]

def calcular_suma(lista):
    return sum(lista)

def mostrar_resultados(lista, suma):
    print("Lista de los primeros 20 números pares:")
    print(lista)
    print(f"\nLa suma de todos los números pares es: {suma}")

def main():
    numeros_pares = generar_numeros_pares(20)
    
    suma_total = calcular_suma(numeros_pares)
    
    mostrar_resultados(numeros_pares, suma_total)

if __name__ == "__main__":
    main()