lado1= float(input("Ingrese el valor numerico de el lado, por favor: "))

if lado1 > 0:
    lado2=lado1**2

    area = lado1* lado2

    print(f"El area es: {area}")
else:
    print("Con estos datos esta dificil hacer el calculo, ingresa otra vez, por favor...")