import json  # Importar la librería json para manejar archivos JSON
from colorama import Fore, Style, init

# Inicializar colorama (necesario para Windows)
init()

# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos una tupla para almacenar el autor y el título, ya que son inmutables
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        # Método para imprimir la información del libro de manera legible
        return f"{Fore.LIGHTYELLOW_EX}Título: {Fore.LIGHTWHITE_EX}{self.titulo_autor[0]}  {Fore.LIGHTYELLOW_EX}Autor: {Fore.LIGHTWHITE_EX}{self.titulo_autor[1]}  {Fore.LIGHTYELLOW_EX}Categoría: {Fore.LIGHTWHITE_EX}{self.categoria}  {Fore.LIGHTYELLOW_EX}ISBN: {Fore.LIGHTWHITE_EX}{self.isbn}"

    def to_dict(self):
        # Método para convertir el objeto Libro a un diccionario (útil para JSON)
        return {
            "titulo": self.titulo_autor[0],
            "autor": self.titulo_autor[1],
            "categoria": self.categoria,
            "isbn": self.isbn
        }

    @classmethod
    def from_dict(cls, data):
        # Método para crear un objeto Libro desde un diccionario
        return cls(data["titulo"], data["autor"], data["categoria"], data["isbn"])

# Definición de la clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para almacenar los libros prestados al usuario
        self.libros_prestados = []

    def __str__(self):
        # Método para imprimir la información del usuario y los libros prestados
        libros_prestados_str = ", ".join([libro.titulo_autor[0] for libro in self.libros_prestados])
        return f"{Fore.LIGHTYELLOW_EX}Usuario: {Fore.LIGHTWHITE_EX}{self.nombre}, {Fore.LIGHTYELLOW_EX}ID: {Fore.LIGHTWHITE_EX}{self.id_usuario}, {Fore.LIGHTYELLOW_EX}Libros Prestados: {Fore.LIGHTWHITE_EX}{libros_prestados_str}"

# Definición de la clase Biblioteca
class Biblioteca:
    def __init__(self, archivo_libros="libros.json", archivo_usuarios="usuarios.json"):
        self.archivo_libros = archivo_libros
        self.archivo_usuarios = archivo_usuarios
        # Diccionarios para almacenar libros por diferentes claves
        self.libros_por_isbn = {}  # Libros indexados por ISBN
        self.libros_por_titulo = {}  # Libros indexados por título
        self.libros_por_autor = {}  # Libros indexados por autor
        self.libros_por_categoria = {}  # Libros indexados por categoría
        # Cargar libros y usuarios desde los archivos JSON al iniciar
        self.cargar_libros()
        self.usuarios_registrados = self.cargar_usuarios()

    def cargar_libros(self):
        # Cargar libros desde un archivo JSON
        try:
            with open(self.archivo_libros, "r") as archivo:
                libros_data = json.load(archivo)
                # Convertir los diccionarios a objetos Libro y almacenarlos en los diccionarios
                for libro_data in libros_data:
                    libro = Libro.from_dict(libro_data)
                    self.libros_por_isbn[libro.isbn] = libro
                    self.libros_por_titulo[libro.titulo_autor[0]] = libro
                    self.libros_por_autor[libro.titulo_autor[1]] = libro
                    self.libros_por_categoria[libro.categoria] = libro
        except FileNotFoundError:
            # Si el archivo no existe, inicializar los diccionarios vacíos
            self.libros_por_isbn = {}
            self.libros_por_titulo = {}
            self.libros_por_autor = {}
            self.libros_por_categoria = {}

    def cargar_usuarios(self):
        # Cargar usuarios desde un archivo JSON
        try:
            with open(self.archivo_usuarios, "r") as archivo:
                usuarios_data = json.load(archivo)
                # Convertir los diccionarios a objetos Usuario
                return {usuario["id_usuario"]: Usuario(usuario["nombre"], usuario["id_usuario"]) for usuario in usuarios_data}
        except FileNotFoundError:
            # Si el archivo no existe, retornar un diccionario vacío
            return {}

    def guardar_libros(self):
        # Guardar libros en un archivo JSON
        libros_data = [libro.to_dict() for libro in self.libros_por_isbn.values()]
        with open(self.archivo_libros, "w") as archivo:
            json.dump(libros_data, archivo, indent=4)
        print(Fore.GREEN + "*** Biblioteca Actualizada Correctamente ***" + Style.RESET_ALL)

    def guardar_usuarios(self):
        # Guardar usuarios en un archivo JSON
        usuarios_data = [{"nombre": usuario.nombre, "id_usuario": usuario.id_usuario} for usuario in self.usuarios_registrados.values()]
        with open(self.archivo_usuarios, "w") as archivo:
            json.dump(usuarios_data, archivo, indent=4)

    def añadir_libro(self):
        # Solicitar datos del libro al bibliotecario
        titulo = input(Fore.LIGHTYELLOW_EX + f"Ingrese el título del libro: {Fore.LIGHTWHITE_EX}")
        autor = input(Fore.LIGHTYELLOW_EX + f"Ingrese el autor del libro: {Fore.LIGHTWHITE_EX}")
        categoria = input(Fore.LIGHTYELLOW_EX + f"Ingrese la categoría del libro: {Fore.LIGHTWHITE_EX}")
        isbn = input(Fore.LIGHTYELLOW_EX + f"Ingrese el ISBN del libro: {Fore.LIGHTWHITE_EX}" + Style.RESET_ALL)

        # Crear el objeto Libro
        libro = Libro(titulo, autor, categoria, isbn)
        # Almacenar el libro en los diccionarios
        self.libros_por_isbn[libro.isbn] = libro
        self.libros_por_titulo[libro.titulo_autor[0]] = libro
        self.libros_por_autor[libro.titulo_autor[1]] = libro
        self.libros_por_categoria[libro.categoria] = libro
        print(f"Libro '{libro.titulo_autor[0]}' añadido a la biblioteca.")
        # Guardar los libros en el archivo JSON después de añadir
        self.guardar_libros()

    def quitar_libro(self):
        # Solicitar ISBN del libro a quitar
        isbn = input(Fore.LIGHTYELLOW_EX + "Ingrese el ISBN del libro a quitar: " + Style.RESET_ALL)
        if isbn in self.libros_por_isbn:
            libro = self.libros_por_isbn.pop(isbn)
            # Eliminar el libro de los otros diccionarios
            del self.libros_por_titulo[libro.titulo_autor[0]]
            del self.libros_por_autor[libro.titulo_autor[1]]
            del self.libros_por_categoria[libro.categoria]
            print(Fore.LIGHTRED_EX + f"Libro '{Fore.LIGHTWHITE_EX + libro.titulo_autor[0]  + Style.RESET_ALL}' quitado de la biblioteca." + Style.RESET_ALL)
            # Guardar los libros en el archivo JSON después de quitar
            self.guardar_libros()
        else:
            # Mensaje de error en rojo
            print(Fore.RED + f"Libro con ISBN {isbn} no encontrado." + Style.RESET_ALL)

    def registrar_usuario(self):
        # Solicitar datos del usuario al bibliotecario
        nombre = input(Fore.LIGHTYELLOW_EX + "Ingrese el nombre del usuario: " + Style.RESET_ALL)
        id_usuario = input(Fore.LIGHTYELLOW_EX + "Ingrese el ID del usuario: " + Style.RESET_ALL)

        # Verificar si el ID ya está en uso
        if id_usuario not in self.usuarios_registrados:
            usuario = Usuario(nombre, id_usuario)
            self.usuarios_registrados[id_usuario] = usuario
            print(Fore.LIGHTMAGENTA_EX + f"Usuario '{usuario.nombre}' registrado con éxito." + Style.RESET_ALL)
            # Guardar los usuarios en el archivo JSON después de registrar
            self.guardar_usuarios()
        else:
            # Mensaje de error
            print(Fore.RED + f"ID de usuario {id_usuario} ya está en uso." + Style.RESET_ALL)

    def dar_de_baja_usuario(self):
        # Solicitar ID del usuario a dar de baja
        id_usuario = input(Fore.LIGHTYELLOW_EX + "Ingrese el ID del usuario a dar de baja: " + Style.RESET_ALL)
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados.pop(id_usuario)
            print(Fore.LIGHTCYAN_EX + f"Usuario '{usuario.nombre}' dado de baja." + Style.RESET_ALL)
            # Guardar los usuarios en el archivo JSON después de dar de baja
            self.guardar_usuarios()
        else:
            # Mensaje de error
            print(Fore.RED + f"Usuario con ID {id_usuario} no encontrado." + Style.RESET_ALL)

    def prestar_libro(self):
        # Solicitar ID del usuario y ISBN del libro
        id_usuario = input(Fore.LIGHTYELLOW_EX + "Ingrese el ID del usuario: " + Style.RESET_ALL)
        isbn = input(Fore.LIGHTYELLOW_EX + "Ingrese el ISBN del libro a prestar: " + Style.RESET_ALL)

        if id_usuario in self.usuarios_registrados and isbn in self.libros_por_isbn:
            usuario = self.usuarios_registrados[id_usuario]
            libro = self.libros_por_isbn[isbn]
            usuario.libros_prestados.append(libro)
            # Eliminar el libro de los diccionarios de libros disponibles
            del self.libros_por_isbn[isbn]
            del self.libros_por_titulo[libro.titulo_autor[0]]
            del self.libros_por_autor[libro.titulo_autor[1]]
            del self.libros_por_categoria[libro.categoria]
            print(Fore.CYAN + f"Libro '{libro.titulo_autor[0]}' prestado a '{usuario.nombre}'." + Style.RESET_ALL)
            # Guardar los libros en el archivo JSON después de prestar
            self.guardar_libros()
        else:
            # Mensaje de error
            print(Fore.RED + "No se pudo prestar el libro. Verifique el ID de usuario y el ISBN." + Style.RESET_ALL)

    def devolver_libro(self):
        # Solicitar ID del usuario y ISBN del libro
        id_usuario = input(Fore.LIGHTYELLOW_EX + "Ingrese el ID del usuario: " + Style.RESET_ALL)
        isbn = input(Fore.LIGHTYELLOW_EX + "Ingrese el ISBN del libro a devolver: " + Style.RESET_ALL)

        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    # Agregar el libro de nuevo a los diccionarios de libros disponibles
                    self.libros_por_isbn[libro.isbn] = libro
                    self.libros_por_titulo[libro.titulo_autor[0]] = libro
                    self.libros_por_autor[libro.titulo_autor[1]] = libro
                    self.libros_por_categoria[libro.categoria] = libro
                    print(f"Libro '{libro.titulo_autor[0]}' devuelto por '{usuario.nombre}'.")
                    # Guardar los libros en el archivo JSON después de devolver
                    self.guardar_libros()
                    return
            # Mensaje de error
            print(Fore.RED + f"Libro con ISBN {isbn} no encontrado en los préstamos de '{usuario.nombre}'." + Style.RESET_ALL)
        else:
            # Mensaje de error
            print(Fore.RED + f"Usuario con ID {id_usuario} no encontrado." + Style.RESET_ALL)

    def buscar_libro_por_titulo(self):
        # Solicitar título del libro a buscar
        titulo = input(Fore.LIGHTYELLOW_EX + "Ingrese el título del libro a buscar: " + Style.RESET_ALL)
        if titulo in self.libros_por_titulo:
            libro = self.libros_por_titulo[titulo]
            print(Fore.LIGHTCYAN_EX + f"Resultado de búsqueda por título '{titulo}':" + Style.RESET_ALL)
            print(libro)
        else:
            # Mensaje de error
            print(Fore.RED + f"No se encontraron libros con el título '{titulo}'." + Style.RESET_ALL)

    def buscar_libro_por_autor(self):
        # Solicitar autor del libro a buscar
        autor = input(Fore.LIGHTYELLOW_EX + "Ingrese el autor del libro a buscar: " + Style.RESET_ALL)
        if autor in self.libros_por_autor:
            libro = self.libros_por_autor[autor]
            print(Fore.LIGHTCYAN_EX + f"Resultado de búsqueda por autor '{autor}':" + Style.RESET_ALL)
            print(libro)
        else:
            # Mensaje de error
            print(Fore.RED + f"No se encontraron libros del autor '{autor}'." + Style.RESET_ALL)

    def buscar_libro_por_categoria(self):
        # Solicitar categoría del libro a buscar
        categoria = input(Fore.LIGHTYELLOW_EX + "Ingrese la categoría del libro a buscar: " + Style.RESET_ALL)
        if categoria in self.libros_por_categoria:
            libro = self.libros_por_categoria[categoria]
            print(Fore.LIGHTCYAN_EX + f"Resultado de búsqueda por categoría '{categoria}':" + Style.RESET_ALL)
            print(libro)
        else:
            # Mensaje de error
            print(Fore.RED + f"No se encontraron libros en la categoría '{categoria}'." + Style.RESET_ALL)

    def listar_libros_prestados(self):
        # Solicitar ID del usuario
        id_usuario = input(Fore.LIGHTYELLOW_EX + "Ingrese el ID del usuario: " + Style.RESET_ALL)
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            if usuario.libros_prestados:
                print(Fore.LIGHTCYAN_EX + f"Libros prestados a '{usuario.nombre}':" + Style.RESET_ALL)
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                # Mensaje de error
                print(Fore.RED + f"'{usuario.nombre}' no tiene libros prestados." + Style.RESET_ALL)
        else:
            # Mensaje de error
            print(Fore.RED + f"Usuario con ID {id_usuario} no encontrado." + Style.RESET_ALL)

    def mostrar_todos_los_libros(self):
        # Mostrar todos los libros disponibles en la biblioteca
        if self.libros_por_isbn:
            print(Fore.LIGHTYELLOW_EX + "\n--- Todos los libros disponibles ---" + Style.RESET_ALL)
            for libro in self.libros_por_isbn.values():
                print(libro)
        else:
            # Mensaje de error
            print(Fore.RED + "No hay libros disponibles en la biblioteca." + Style.RESET_ALL)

# Menú principal
def menu():
    biblioteca = Biblioteca()
    # Menu Principal
    while True:
        print(Fore.LIGHTYELLOW_EX + "\n--- Sistema de Gestión de Biblioteca Digital ---" + Style.RESET_ALL)
        print(Fore.LIGHTGREEN_EX + f"1. {Fore.CYAN}Añadir libro")
        print(Fore.LIGHTGREEN_EX + f"2. {Fore.CYAN}Quitar libro")
        print(Fore.LIGHTGREEN_EX + f"3. {Fore.CYAN}Registrar usuario")
        print(Fore.LIGHTGREEN_EX + f"4. {Fore.CYAN}Dar de baja usuario")
        print(Fore.LIGHTGREEN_EX + f"5. {Fore.CYAN}Prestar libro")
        print(Fore.LIGHTGREEN_EX + f"6. {Fore.CYAN}Devolver libro")
        print(Fore.LIGHTGREEN_EX + f"7. {Fore.CYAN}Buscar libro por título")
        print(Fore.LIGHTGREEN_EX + f"8. {Fore.CYAN}Buscar libro por autor")
        print(Fore.LIGHTGREEN_EX + f"9. {Fore.CYAN}Buscar libro por categoría")
        print(Fore.LIGHTGREEN_EX + f"10. {Fore.CYAN}Listar libros prestados a un usuario")
        print(Fore.LIGHTGREEN_EX + f"11. {Fore.CYAN}Mostrar todos los libros")
        print(Fore.LIGHTGREEN_EX + f"12. {Fore.CYAN}Salir" + Style.RESET_ALL)

        opcion = input(Fore.LIGHTMAGENTA_EX + "Seleccione una opción: " + Style.RESET_ALL)

        if opcion == "1":
            biblioteca.añadir_libro()
        elif opcion == "2":
            biblioteca.quitar_libro()
        elif opcion == "3":
            biblioteca.registrar_usuario()
        elif opcion == "4":
            biblioteca.dar_de_baja_usuario()
        elif opcion == "5":
            biblioteca.prestar_libro()
        elif opcion == "6":
            biblioteca.devolver_libro()
        elif opcion == "7":
            biblioteca.buscar_libro_por_titulo()
        elif opcion == "8":
            biblioteca.buscar_libro_por_autor()
        elif opcion == "9":
            biblioteca.buscar_libro_por_categoria()
        elif opcion == "10":
            biblioteca.listar_libros_prestados()
        elif opcion == "11":
            biblioteca.mostrar_todos_los_libros()
        elif opcion == "12":
            print(Fore.LIGHTBLUE_EX + "Saliendo del sistema..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo." + Style.RESET_ALL)

# Ejecutar el menú principal
if __name__ == "__main__":
    menu()