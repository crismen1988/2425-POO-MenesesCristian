class Biblioteca:
    def __init__(self, nombre):
        """
        Constructor: Inicializa la biblioteca con un nombre y una lista vacía de libros.
        """
        self.nombre = nombre
        self.libros = []
        print(f"Biblioteca '{self.nombre}' creada con éxito.\n")

    def agregar_libro(self, titulo):
        """
        Agrega un libro a la lista de libros.
        """
        self.libros.append(titulo)
        print(f"Libro '{titulo}' agregado a la biblioteca '{self.nombre}'.")

    def mostrar_libros(self):
        """
        Muestra todos los libros disponibles en la biblioteca.
        """
        if self.libros:
            print(f"\n*** Libros en la biblioteca'{self.nombre}' ***")
            for libro in self.libros:
                print(f" - {libro}")
        else:
            print(f"La biblioteca '{self.nombre}' no tiene libros.")

    def __del__(self):
        """
        Destructor: Muestra un mensaje al cerrar la biblioteca.
        """
        print(f"\nLa biblioteca '{self.nombre}' está siendo cerrada.")
        print("**** Limpieza completa. ****")


# Crear una biblioteca
mi_biblioteca = Biblioteca("Biblioteca Central")

# Agregar libros
mi_biblioteca.agregar_libro("Cien años de soledad")
mi_biblioteca.agregar_libro("Don Quijote de la Mancha")
mi_biblioteca.agregar_libro("Viaje al Centro de la Tierra")

# Mostrar libros
mi_biblioteca.mostrar_libros()

# Eliminar la biblioteca
del mi_biblioteca
