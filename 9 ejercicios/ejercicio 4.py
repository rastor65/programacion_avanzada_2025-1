estudiantes=int(input("Ingrese el numero total de estudiantes"))
numero_lapices =32

lapices_sobrantes = numero_lapices % estudiantes

if estudiantes > numero_lapices:
    lapices_faltantes = estudiantes - numero_lapices
    print(f"Faltan {lapices_faltantes} lápices.")
else:
    # Calcular cuántos lápices sobran
    lapices_sobrantes = numero_lapices % estudiantes
    print(f"Al profesor le sobran {lapices_sobrantes} lápices")