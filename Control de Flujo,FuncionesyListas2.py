def generar_tabla(numero, orientacion):
    if orientacion == "horizontal":
        print(" | ".join([f"{numero} x {i} = {numero * i}" for i in range(1, 13)]))
    else:
        for i in range(1, 13):
            print(f"{numero} x {i} = {numero * i}")

def main():
    numero = int(input("Ingresa un número: "))
    orientacion = input("¿Formato horizontal o vertical?: ").strip().lower()
    generar_tabla(numero, orientacion)

main()
