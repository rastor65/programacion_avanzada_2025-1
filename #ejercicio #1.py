#ejercicio #1
#Un chef tiene un presupuesto inicial. Y para su receta necesita comprar
#vegetales, carne y especias. Finalmente, si los gastos no superan el
#presupuesto,puedeagregarfrutas.
#Calcula y muestra cuánto dinero le queda al chef después de todas las
#compras.

presupuesto=float(input("Por favor digite su presupuesto:"))
print(f"Su presupuesto para las compras es : {presupuesto}")

vegetales=float(input("Digite el precio de lo que compro en vegetales :"))
carne=float(input("Digite el precio de lo que compro en carne :"))
especias=float(input("Digite el precio de lo que compro en especias :"))

total=vegetales+carne+especias
restante=presupuesto-total
if total<=presupuesto:
    print("usted puede comprar frutas")
    frutas=float(input("Cuanto se gasto en frutas?:"))
    total1=vegetales+carne+especias+frutas
    r=total1-presupuesto
    print(f"Su compra en total fueron: {total1}")
    print(f"Le quedaron restando: {r}")
elif total>presupuesto:
    print(f"Su compra en total Fue:{total}")

    








    





