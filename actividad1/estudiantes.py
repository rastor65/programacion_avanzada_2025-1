estu = int(input("cuantos estudiantes hay ? "))
grupos = int(input("de cuantos gupos son ? "))
grupos_estu = estu // grupos
restos = estu % grupos
if restos == 0:
    print(f"se forman {grupos_estu} grupos de {grupos} estudiantes")
else:
    print(f"se forman {grupos_estu} grupos de {grupos} estudiantes y un grupo de {restos} estudiantes")