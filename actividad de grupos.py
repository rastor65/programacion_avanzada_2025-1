
num_estudiantes = int(input("Cual es la cantidad de estudiantes que hay en el salon: "))
num_lapices = 32
if num_estudiantes > num_lapices:
    print("No habrá lápices sobrantes, ya que la cantidad de estudiantes excede la cantidad de lápices disponibles.")
else:
    lapices_sobrantes = num_lapices % num_estudiantes
    print(f"Al profesor le sobran {lapices_sobrantes} lápices después de entregar.")