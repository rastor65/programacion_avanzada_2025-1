print("Bienvenido al Bienestar")  

nombre_usu = input("Por favor, ingrese su nombre de usuario: ").strip() 

if 4 <= len(nombre_usu) <= 7:
    print(f"¡Hola, {nombre_usu.upper()}!")
else:
    print("El nombre debe tener entre 4 y 7 caracteres como máximo. Por favor, intente de nuevo.")
return nombre_usu
