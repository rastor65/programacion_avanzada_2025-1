
comentario = input("Ingresa el comentario : ")


comentario_limpio = comentario.strip()


comentario_minusculas = comentario_limpio.lower()

cantidad_excelente = comentario_minusculas.count("excelente")


print("\nComentario analisado :", comentario_minusculas)
print(f"La palabra 'excelente' aparece {cantidad_excelente} veces ")
