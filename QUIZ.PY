class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.__disponible = True

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            print(f'\nEl libro "{self.titulo}" ha sido prestado.')
        else:
            print(f'\nEl libro "{self.titulo}" ya está prestado.')

    def devolver(self):
        self.__disponible = True
        print(f'\nEl libro "{self.titulo}" ha sido devuelto.')

    def estado(self):
        if self.__disponible:
            return "DISPONIBLE"
        else:
            return "PRESTADO"

    def __str__(self):
        return f'Libro: "{self.titulo}" - Autor: {self.autor} - Estado: {self.estado()}'


def buscar_libro(lista, titulo):
    for libro in lista:
        if libro.titulo.lower() == titulo.lower():
            return libro
    return None


if __name__ == "__main__":
    biblioteca = []

    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar un libro")
        print("2. Retirar un libro")
        print("3. Ver estado de un libro")
        print("4. Prestar un libro")
        print("5. Devolver un libro")
        print("6. Mostrar todos los libros")
        print("7. Salir")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            biblioteca.append(Libro(titulo, autor))
            print(f'Libro "{titulo}" agregado con éxito.')

        elif opcion == "2":
            titulo = input("Ingrese el título del libro a retirar: ")
            libro = buscar_libro(biblioteca, titulo)
            if libro:
                biblioteca.remove(libro)
                print(f'Libro "{titulo}" retirado de la biblioteca.')
            else:
                print("Libro no encontrado.")

        elif opcion == "3":
            titulo = input("Ingrese el título del libro: ")
            libro = buscar_libro(biblioteca, titulo)
            if libro:
                print(libro)
            else:
                print("Libro no encontrado.")

        elif opcion == "4":
            titulo = input("Ingrese el título del libro a prestar: ")
            libro = buscar_libro(biblioteca, titulo)
            if libro:
                libro.prestar()
            else:
                print("Libro no encontrado.")

        elif opcion == "5":
            titulo = input("Ingrese el título del libro a devolver: ")
            libro = buscar_libro(biblioteca, titulo)
            if libro:
                libro.devolver()
            else:
                print("Libro no encontrado.")

        elif opcion == "6":
            if biblioteca:
                print("\nLibros en la biblioteca:")
                for libro in biblioteca:
                    print(libro)
            else:
                print("La biblioteca está vacía.")

        elif opcion == "7":
            print("Gracias por usar el sistema.")
            break

        else:
            print("Opción inválida.")
