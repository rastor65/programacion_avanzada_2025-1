presupuesto = float(input("Ingrese su presupuesto: "))
precio = float(input("Ingrese el precio de las licencias, por favor: "))

licencias1 = presupuesto // precio
dineroRestante = presupuesto - precio

if licencias1 > 0 :

    print(f"Puedes comprar {licencias1}")

if dineroRestante < presupuesto :
    print("Usted puede seguir comprando más licencias... ")
    print(f"A usted le queda:   {dineroRestante}")
    op=-1 
    while op not in [0, 1] :   
        print("Desea comprar más?: ")
        op=int(input("[1] SI - [0] NO: "))
        if op==1 :    
            precio2 = float(input("Ingrese el valor de la licencias: "))   
        presupuesto2=dineroRestante
        licencias2=presupuesto2 // precio2
    else :
        print("Saliendo...") 
    print(f"Usted volvio a comprar:   {licencias2}")
else:
    print("Es todo lo que tiene, lo lamento...")
    