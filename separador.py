
comentarios = str(input("ingrese los comentarios: "))
contador_excelente = 0
for comentario in comentarios:
    comentario = comentario.strip()
    comentario = comentario.lower() 
    contador_excelente += comentario.count("excelente") 
    print(comentario)
print(f"Número total de menciones de 'excelente': {contador_excelente}")