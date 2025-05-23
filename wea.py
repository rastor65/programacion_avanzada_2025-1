# Definición de la clase base Empleado
class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado el empleado {self.nombre} de {self.edad} años.")

    def trabajar(self):
        print(f"{self.nombre} está trabajando.")

    def __del__(self):
        print(f"Se ha eliminado el empleado {self.nombre}.")

# Definición de la clase hija Gerente
class Gerente(Empleado):
    def __init__(self, nombre, edad, departamento):
        super().__init__(nombre, edad)
        self.departamento = departamento

    def trabajar(self):
        print(f"{self.nombre} está gestionando el departamento de {self.departamento}.")

# Definición de la clase hija Programador
class Programador(Empleado):
    def __init__(self, nombre, edad, lenguaje):
        super().__init__(nombre, edad)
        self.lenguaje = lenguaje

    def trabajar(self):
        print(f"{self.nombre} está programando en {self.lenguaje}.")

# Programa principal
if __name__ == "__main__":
    # Crear objetos
    gerente = Gerente("Ana", 40, "Recursos Humanos")
    programador = Programador("Luis", 25, "Python")

    # Llamar al método trabajar
    gerente.trabajar()
    programador.trabajar()
