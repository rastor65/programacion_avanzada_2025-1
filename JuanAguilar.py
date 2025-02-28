presupuesto = 100000

vegetales = 50000
carne = 70000
especias = 20000

gastos = vegetales+carne+especias-presupuesto

if gastos < presupuesto:
    frutas = 50000
    gastos += frutas
    print ("El chef puede comprar frutas")

else:
    print ("El chef no puede comprar frutas")


total = presupuesto - gastos


print(f"\nPresupuesto Inicial: ${presupuesto}")
print(f"\nPresupuesto restante: ${total}")