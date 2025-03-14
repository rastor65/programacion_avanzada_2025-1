print("Buenas tardes, Sr Cliente")
presupuesto= int(input("Cual es su presupuesto para comprar licencias?"))
licencias_actuales= int (input("Con cuantas licencias actuales cuentan?"))
costo_licencia=200

licencias_posibles= presupuesto / costo_licencia

if licencias_posibles > 0:
    print(f"La escuela puede comprar {int(licencias_posibles)} licencias adicionales.")


