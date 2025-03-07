precio_licencia = 0
total_licencias = 0
presupuesto = 0

while presupuesto <= 0:
    presupuesto = int(input("Ingrese su presupuesto: "))
    if presupuesto <= 0:
        print("Cantidad invalida.")
        presupuesto = 0
while precio_licencia <= 0:
    precio_licencia = int(input("Ingrese el costo de la licencia: "))
    if precio_licencia <= 0:
        print("Cantidad invalida.")
        precio_licencia = 0
while total_licencias <= 0:       
    total_licencias = int(input("Ingrese el numero de licencias que quiere comprar: "))
    if total_licencias <= 0:
        print("Cantidad invalida.")
        precio_licencia = 0
costo_total = precio_licencia*total_licencias
if costo_total > presupuesto:
    print(f"No puede efectuar la compra.\nPresupuesto: {presupuesto}\nCosto total: {costo_total}")
elif costo_total == presupuesto:
    print(f"Compra exitosa.\nLicencias extra: 0")
else:
    restante = presupuesto-costo_total
    licencias_extras = restante//precio_licencia
    print(f"Compra exitosa.\nDinero restante: {restante}\nLicencias extras: {licencias_extras}")

