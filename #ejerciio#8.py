def corregir_articulo(articulo):
    articulo_corregido = articulo.replace("tecnología antigua", "tecnología de punta")
    oraciones = articulo_corregido.split(".")
    
    for oracion in oraciones:
        if oracion.strip():
            print(f"- {oracion.strip()}.")

texto = "La tecnología antigua ya no es eficiente. La tecnología antigua limita el progreso. Debemos adoptar la tecnología antigua con mejoras."
corregir_articulo(texto)
