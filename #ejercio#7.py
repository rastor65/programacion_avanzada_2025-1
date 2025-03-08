#Estás analizando comentarios de clientes para un producto. Necesitas
#contar cuántas veces se menciona la palabra "excelente"
##, eliminar
#espaciosinnecesarios ymostrarelcomentarioenminúsculas.
def analizar():
    comentario = input("Ingresa el comentario del cliente: ")
  
    comentario_limpio = comentario.strip()
    comentario_minusculas = comentario_limpio.lower()
    veces_excelente = comentario_minusculas.count("excelente")
    print(f"\nComentario procesado: {comentario_minusculas}")
    print(f"La palabra 'excelente' aparece {veces_excelente} veces.")

analizar()
