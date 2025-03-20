def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Ingrese un número: "))
if primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

