nombre= input("ingresa un nombre: ")
if len(nombre) < 3 or len(nombre) > 8:
    print("Digite otro nombre, este no es valido")
else:
    print(f"hola,{nombre.upper()}.")



