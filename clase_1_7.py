#pagina 24
presupuesto= float(input("¿Cuánto es su presupuesto? "))
vegetales= float(input("¿Cuánto quiere comprar en vegetales? "))
carne_especies= float(input("¿Cuánto quiere comprar en carne y especias? "))

total_ = vegetales + carne_especies
sobrante = presupuesto-total_

if total_ < presupuesto:
    print(f"Van {total_} de dinero, le sobran {sobrante}")
    frutas_= float(input("Le alcanza para comprar frutas también ¿Cuánto comprará? "))
    
    if frutas_ > sobrante:
        print("La compra de frutas supera al sobrante")
    else:
        sobrante_nuevo = sobrante - frutas_
        print(f"Listo, el nuevo sobrante es {sobrante_nuevo}")

else:
    print("No le alcanza para comprar frutas")

total_nuevo= total_+ frutas_
print("El total fue de ", total_nuevo)
print("Gracias por su compra")

