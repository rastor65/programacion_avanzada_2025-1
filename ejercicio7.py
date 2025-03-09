comentario1 = input("Ingrese su comentario: ").strip()
conteo2 = comentario1.lower().count("excelente")

print("Comentario procesado:", comentario1.lower())
print("La palabra 'excelente' aparece", conteo2, "veces.")