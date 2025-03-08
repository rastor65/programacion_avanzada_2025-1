#Estás desarrollando un sistema de registro para una plataforma en
#línea. Necesitas procesar los nombres de usuario ingresados por los
#usuarios, dichos nombres deben ser mayores a 3 caracteres y menores
#que 8. Si cumple con eso, envía un saludo con su nombre en
#mayúsculas.

nombre=input("Ingrese su nombre:")
if 3< len(nombre) <8:
    print(f"Bienvenido:, {nombre.upper()} !")
else:
    print("Error: El nombre de usuario debe tener entre 4 y 7 caracteres.")
   