import sys
"""
Ejercicio 1.
Un chef tiene un presupuesto inicial. Y para su receta necesita comprar
vegetales, carne y especias. Finalmente, si los gastos no superan el
presupuesto, puede agregar frutas.

Calcula y muestra cuánto dinero le queda al chef después de todas las
compras.

presupuesto = 0
gastos = 0

presupuesto = float(input("Ingrese su presupuesto: "))
gastos += float(input("Ingrese el valor de los vegetales: "))
gastos += float(input("Ingrese el valor de la carne: "))
gastos += float(input("Ingrese el valor de las especias: "))

if gastos == presupuesto:  
    print("Compra exitosa, dinero restante $0.")
    
elif gastos > presupuesto:
    print(f"No puede realizar la compra, le hacen falta ${gastos-presupuesto}.")
else:
    gastos += float(input("Ingrese el valor de las frutas: "))
    if gastos > presupuesto:
        print(f"No puede realizar la compra, le hacen falta ${gastos-presupuesto}.")
    elif gastos == presupuesto:  
        print("Compra exitosa, dinero restante $0.")
    else:
        print(f"Compra exitosa, dinero restante ${presupuesto-gastos}.")
"""

"""
Ejercicio 2.
Una empresa de tecnología vende un paquete de software por
licencia. Y tiene una escuela como cliente, esta escuela planea
comprar cierta cantidad de licencias, dependiendo de su
presupuesto.

Calcula y muestra cuántas licencias adicionales pueden comprar y en
caso de que no puedan comprar má sadicionales, indícaselos.

precio_licencia = 0
total_licencias = 0
presupuesto = 0

while presupuesto <= 0:
    presupuesto = int(input("Ingrese su presupuesto: "))
    if presupuesto <= 0:
        print("Cantidad invalida.")
while precio_licencia <= 0:
    precio_licencia = int(input("Ingrese el costo de la licencia: "))
    if precio_licencia <= 0:
        print("Cantidad invalida.")
while total_licencias <= 0:       
    total_licencias = int(input("Ingrese el numero de licencias que quiere comprar: "))
    if total_licencias <= 0:
        print("Cantidad invalida.")
costo_total = precio_licencia*total_licencias
if costo_total > presupuesto:
    print(f"No puede efectuar la compra.\nPresupuesto: {presupuesto}\nCosto total: {costo_total}")
elif costo_total == presupuesto:
    print(f"Compra exitosa.\nLicencias extra: 0")
else:
    restante = presupuesto-costo_total
    licencias_extras = restante//precio_licencia
    print(f"Compra exitosa.\nDinero restante: {restante}\nLicencias extras: {licencias_extras}")
"""

"""
Ejercicio 3.
Un grupo de estudiantes necesita dividirse en equipos. Pídele al usuario
que ingrese el número total de estudiantes y cuántos estudiantes debe
haber por equipo.

Calcula y muestra cuántos equipos completos se pueden formar.

total_estudiantes = int(input("Ingresa el número total de estudiantes: "))
integrantes_por_equipo = int(input("¿Cuantos integrantes debe tener cada grupo?\n-"))
if total_estudiantes <= 0 or integrantes_por_equipo <= 0:
    print("Datos invalidos.")
    sys.exit(0)
grupos_completos = total_estudiantes // integrantes_por_equipo
if total_estudiantes % integrantes_por_equipo == 0:
    print(f"Se pueden formar {grupos_completos} grupos de {integrantes_por_equipo} estudiantes.")
else:
    estudiantes_extras = total_estudiantes-(grupos_completos*integrantes_por_equipo)
    print(f"Se pueden formar {grupos_completos} grupos de {integrantes_por_equipo} estudiantes\nEstudiantes que sobran: {estudiantes_extras}")
"""

"""
Ejercicio 4.
Un profesor quiere dividir 32 lápices entre todos los estudiantes de su
grupo y quiere saber cuántos lápices le sobran.

¿Cuántos lápices le sobran al profesor?

lapices = 32
total_estudiantes = int(input("Ingresa el número de estudiantes: "))
if total_estudiantes <= 0:
    print("Datos invalidos.")
    sys.exit(0)
if total_estudiantes > lapices:
    print("Hay más estudiantes que lapices.")
    sys.exit(0)
lapices_restantes = int(lapices % total_estudiantes)
print(f"Lapices por estudiante: {lapices//total_estudiantes}")
print(f"Lapices que sobran: {lapices_restantes}")
"""

"""
Ejercicio 5.
Cuál es el área de un terreno rectangular para el cual el usuario
solamente conoce la medida de uno de sus lados.

# Asumiendo que se referia al area de un cuadrado sería asi.
lado = float(input("Ingrese el valor del lado: "))
print(f"Area = {lado**2}")
"""

"""
Ejercicio 6.
Estás desarrollando un sistema de registro para una plataforma en
línea. Necesitas procesar los nombres de usuario ingresados por los
usuarios, dichos nombres deben ser mayores a 3 caracteres y menores
que 8. Si cumple con eso, envía un saludo con su nombre en
mayúsculas.

nombre = input("Ingrese su nombre: ")
if len(nombre) < 3 or len(nombre) > 8:
    print("Nombre no valido. Debe tener entre 3-8 caracteres.")
else: 
    print(f"Hola, {nombre.upper()}.")
"""

"""
Ejercicio 7.
Estás analizando comentarios de clientes para un producto. Necesitas
contar cuántas veces se menciona la palabra "excelente", eliminar espacios 
innecesarios y mostrar el comentario en minúsculas.

comentario = input("Ingrese el comentario: ").lower()
repeticiones = comentario.count("excelente")
print(f"COMENTARIO LUEGO DE LOS CAMBIOS\n-{comentario.strip()}\n Veces que se usó la palabra \"Excelente\": {repeticiones}.")
"""

"""
Ejercicio 8.
Enunciado: Eres un editor de noticias y necesitas corregir un artículo.
Debes reemplazar todas las menciones de "tecnología antigua" por
"tecnología de punta" y dividir el artículo en oraciones.

articulo = input("Ingrese el articulo: ").strip()
articulo = articulo.lower().replace("tegnologia antigua", "tegnologia de punta")
print(articulo.split("."))
"""

"""
Ejercicio 9.
Enunciado: Estás trabajando en un sistema de inventario. Necesitas
verificar si un código de producto ingresado por el usuario es válido. Un
código válido debe comenzar con las letras "PRO" (en mayúsculas). Si el
código es válido, muestra un mensaje de "Código válido". De lo
contrario, muestra "Código inválido".

while True: # El ciclo while solo es para probar varios codigos sin detener la ejecución.
    codigo = input("Ingrese su codigo: ").strip().upper()
    if codigo.startswith("PRO"):
        print("Código válido")
    else:
        print("Código inválido")
"""