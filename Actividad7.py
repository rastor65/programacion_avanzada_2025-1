comentario = input("estimado cliente por favor ingrese su comentario aqui:")
comentario = comentario.strip() 
comentario = comentario.lower()
cont = comentario.count("excelente")
print (f"la palabra 'excelente' fue repetida {cont} veces.")
print (f"su comentario sin espacios innecesarios es: ",comentario)