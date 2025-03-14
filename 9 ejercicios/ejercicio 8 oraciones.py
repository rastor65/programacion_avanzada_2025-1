import re

def corregir_articulo():

    print("Bienvenido, Sr Editor")

    articulo = """Hace décadas, la tecnología antigua sentó las bases de la innovación actual.
    Los primeros teléfonos eran grandes y solo permitían hacer llamadas básicas.
    Las computadoras ocupaban habitaciones enteras y tenían una capacidad muy limitada.
    Antes de los discos duros, la información se almacenaba en cintas magnéticas.
    Aunque hoy parecen obsoletos, estos avances fueron revolucionarios en su tiempo."""
    
    articulo = articulo.replace("tecnología antigua", "tecnología de punta")
    
    oraciones = re.split(r'(?<=\.)\s+', articulo)

    print("\nOraciones corregidas:")
    for oracion in oraciones:
        print(oracion)

corregir_articulo()
