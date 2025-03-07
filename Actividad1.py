valor_licencia = float(input("ingrese el valor de la licencia: "))
pres_escuela = float (input("ingrese su presupuesto: "))
lic_a_comprar = float(input ("ingrese la cantidad de licencia que desea comprar: "))
total = valor_licencia * lic_a_comprar
pres_rest =pres_escuela - total
if total == pres_escuela or total>pres_escuela:
    print ("no tiene presupuesto para comprar mas licencias")
elif total<pres_escuela:
    pres_restante = pres_escuela - total
    lic_adicional = pres_restante // valor_licencia
    print(f"tiene presupuesto para comprar  {int(lic_adicional)} licencias adicional")