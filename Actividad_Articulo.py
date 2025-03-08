Artc = input("Ingrese el articulo de noticias: ")
Artc_Correg = Artc.replace("tecnología antigua", "tecnología de punta")
Oracions = Artc_Correg.split(",")
print("Articulo Corregido: ",Artc_Correg)
for i, Oracions in enumerate(Oracions,1):
    print(f"{i}. {Oracions.strip()}")