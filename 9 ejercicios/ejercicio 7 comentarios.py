def analizar_comentario():
    comentario = input("Ingresa su comentario: ").lower().strip() 
    contar_excelente = comentario.count("excelente") 
    
    print(f'La palabra "excelente" aparece {contar_excelente} veces.')

analizar_comentario()
