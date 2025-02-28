nombre = str(input("diga su nombre "))
if len(nombre) < 3 or len(nombre) > 8:
    print("el nombre no es valido")
else: 
    print(f"hola, {nombre.upper()}")

