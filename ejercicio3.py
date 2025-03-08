estudiantes = int(input("Cuantos estudiantes hay en tu curso?: "))
cantidad_estudiantes_por_grupo= int(input("¡Escoge a tus amigos! cuantos estudiantes por grupo?: "))

grupos = estudiantes // cantidad_estudiantes_por_grupo

print(f"Salen {grupos} completos.") 