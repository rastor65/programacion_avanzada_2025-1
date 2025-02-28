presupuesto = float(input("Ingrese el presupuesto total de la escuela: "))
licencia = float(input("Ingrese el precio de una licencia: "))
licencias_compra = int(input("¿Cuántas licencias han sido compradas?: "))

costo = licencias_compra*licencia
sobrante = presupuesto - costo
adicional = sobrante/licencia
