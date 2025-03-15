def generar_tabla_multiplicar(numero, formato):
    if formato == 'horizontal':
        for i in range(1, 13):
            print(f'{numero} x {i} = {numero * i}', end='  ')
        print()
    elif formato == 'vertical':
        for i in range(1, 13):
            print(f'{numero} x {i} = {numero * i}')
    else:
        print("Formato no válido. Por favor, elija 'horizontal' o 'vertical'.")

def main():
    try:
        numero = int(input("Introduce un número para generar su tabla de multiplicar: "))
        formato = input("Introduce el formato (horizontal/vertical): ").strip().lower()
        generar_tabla_multiplicar(numero, formato)
    except ValueError:
        print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()