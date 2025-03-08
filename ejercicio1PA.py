presupuesto = float(input("Hola chef, ingrese su presupuesto: "))
vergetales = float(input("Sabe cuanto cuestan los vegetales ¿verdad?, ingrese el precio: "))
carne= float(input("Tambien el de las carnes, por favor: "))
especias = float(input("¡Las especias son importantes! ingrese su valor: "))

total1= vergetales + carne + especias
print(f"Su gasto es: ${total1}")

if total1 <= presupuesto :
    print("Usted puede comprar frutas tambien...") 
    presupuesto2 = presupuesto - total1
    print(f"Te quedan: {presupuesto2}")
    frutas= float(input("Precio de las frutas, por favor: "))
if frutas <= presupuesto2:
        total2= total1+frutas
        dineroRestante=presupuesto2-total2
        print(f"Le quedo esto, chef: {dineroRestante}")
else:
    print("Prepare otra cosa chef, lo siento")
    