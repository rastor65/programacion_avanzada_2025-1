#TALLER

#1.

"""presupuesto = float(input("ingrese cuanto dinero tiene "))
vegetales = float(input("ingrese cuanto costo vegetales "))
carne = float(input("Ingrese cuanto costo la carne "))
especias = float(input("Ingrese cuanto costo las especias "))

gasto_total = vegetales + carne + especias
if gasto_total < presupuesto:
    frutas = float(input("Ingrese cuanto cuesta la fruta "))
    gasto_total = gasto_total + frutas
else:
    print("falta dinero, somos pobres :(")


loqquedo = presupuesto - gasto_total


print(f"lo que quedo de dinero: {loqquedo}")"""

#2.

"""presupuesto = float(input("Ingrese el presupuesto que tiene  "))
licencia = float(input("Ingrese cual es el precio de la licencia "))
licencias_compra = int(input("Ingrese la cantidad de licencias q desea comprar "))
precio_total =licencia* licencias_compra 
presupuesto = presupuesto - precio_total

licencias_adicionales = presupuesto // licencia  

if licencias_adicionales > 0:
    print(f" puede comprar {int(licencias_adicionales)} licencias adicionales.")
else:
    print("No tiene mas dinero para comprar mas licencias")"""

#3. 

"""total_estudiantes = int(input("Ingrese cuantos estudiantes hay"))
cuanto = int(input("Ingrese de cuanto debe ser el equipo"))
equipos = total_estudiantes // cuanto  
print(f"Se pueden formar {equipos} equipos")"""

#4.

"""lapices = 32
estudiantes = int(input("cuantos estudiantes hay"))
sobrante = lapices % estudiantes
print(f" sobran {sobrante} lápices.")"""

#5.

"""lado = float( input("Ingrese la medida de un lado : "))
area = lado ** 2
print(f"El área  es {area}.")"""

#6.

"""nombre = input("Ingrese un nombre de usuario")

if 3 < len(nombre) < 8:
    
    print(f"¡Hola, {nombre.upper()}!")
else:
    print("El nombre debe tener entre 4 y 7 caracteres.")"""

#7.

"""comentario = input("Ingrese el comentario ")

comentario = comentario.strip()

comentario_minusculas = comentario.lower()

cantidad_excelente = comentario_minusculas.count("excelente")

print(f"{comentario_minusculas}")
print(f'La palabra "excelente" aparece {cantidad_excelente} veces.')"""

#8.

"""articulo = input("Ingrese el artículo: ")

articulo_corregido = articulo.replace("tecnología antigua", "tecnología de punta")

oraciones = articulo_corregido.split(".")

print("\nArtículo  nuevo:")
print(articulo_corregido)"""

#9. 


"""codigo = input("Ingrese el código : ")
codigo = codigo.upper()

if codigo.startswith("PRO"):
    print("Código válido")
else:
    print("Código inválido")"""


