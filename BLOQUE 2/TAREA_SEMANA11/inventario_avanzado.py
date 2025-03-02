from colorama import Fore, init  # Importa las clases Fore y init del módulo colorama para colorear la salida en consola.
import os  # Importa el módulo os para interactuar con el sistema operativo, como manejar archivos.
import json  # Importa el módulo json para manejar la serialización y deserialización de datos.

# Inicializa colorama para resaltar los mensajes en consola
init(autoreset=True)  # Inicializa colorama y configura autoreset para que los colores no se propaguen a otras líneas.

# Nombre del archivo donde se guardará el inventario
ARCHIVO_INVENTARIO = "inventario.json"  # Define el nombre del archivo que almacenará el inventario en formato JSON.

# ==============================
# Clase Producto
# ==============================
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        # Constructor de la clase Producto. Inicializa los atributos del producto.
        self._id = id  # Asigna el ID del producto.
        self._nombre = nombre  # Asigna el nombre del producto.
        self._cantidad = cantidad  # Asigna la cantidad del producto.
        self._precio = precio  # Asigna el precio del producto.

    @property
    def id(self):
        # Getter para el atributo id.
        return self._id

    @property
    def nombre(self):
        # Getter para el atributo nombre.
        return self._nombre

    @property
    def cantidad(self):
        # Getter para el atributo cantidad.
        return self._cantidad

    @property
    def precio(self):
        # Getter para el atributo precio.
        return self._precio

    @nombre.setter
    def nombre(self, nuevo_nombre):
        # Setter para el atributo nombre. Valida que el nuevo nombre sea una cadena no vacía.
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre.strip()
        else:
            print(Fore.RED + "Error: El nombre no puede estar vacío.")

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        # Setter para el atributo cantidad. Valida que la nueva cantidad sea un entero no negativo.
        if isinstance(nueva_cantidad, int) and nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            print(Fore.RED + "Error: La cantidad debe ser un número entero no negativo.")

    @precio.setter
    def precio(self, nuevo_precio):
        # Setter para el atributo precio. Valida que el nuevo precio sea un número no negativo.
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print(Fore.RED + "Error: El precio debe ser un número no negativo.")

    def __str__(self):
        # Método para representar el producto como una cadena en formato CSV.
        return f"{self._id},{self._nombre},{self._cantidad},{self._precio:.2f}"

    def to_dict(self):
        # Método para convertir el producto a un diccionario.
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

# ==============================
# Clase Inventario
# ==============================
class Inventario:
    def __init__(self):
        # Constructor de la clase Inventario. Inicializa un diccionario para almacenar productos.
        self._productos = {}
        self.cargar_desde_archivo()  # Carga los productos desde el archivo al iniciar.

    def cargar_desde_archivo(self):
        """Carga los productos desde un archivo JSON al iniciar el programa."""
        if not os.path.exists(ARCHIVO_INVENTARIO):
            return  # Si el archivo no existe, no hay nada que cargar.

        try:
            with open(ARCHIVO_INVENTARIO, "r") as archivo:
                # Abre el archivo en modo lectura.
                datos = json.load(archivo)  # Carga los datos desde el archivo JSON.
                for producto_data in datos:
                    # Crea un objeto Producto a partir de los datos cargados.
                    producto = Producto(
                        producto_data["id"],
                        producto_data["nombre"],
                        producto_data["cantidad"],
                        producto_data["precio"]
                    )
                    self._productos[producto.id] = producto
            print(Fore.GREEN + "Inventario cargado correctamente desde archivo.")
        except FileNotFoundError:
            print(Fore.RED + "Error: Archivo de inventario no encontrado.")
        except PermissionError:
            print(Fore.RED + "Error: No se tiene permiso para leer el archivo de inventario.")
        except Exception as e:
            print(Fore.RED + f"Error inesperado al cargar inventario: {e}")

    def guardar_en_archivo(self):
        """Guarda los productos en el archivo JSON después de cualquier modificación."""
        try:
            with open(ARCHIVO_INVENTARIO, "w") as archivo:
                # Abre el archivo en modo escritura.
                datos = [producto.to_dict() for producto in self._productos.values()]
                json.dump(datos, archivo, indent=4)  # Escribe los datos en el archivo JSON.
            print(Fore.GREEN + "Inventario guardado correctamente en archivo.")
        except PermissionError:
            print(Fore.RED + "Error: No se tiene permiso para escribir en el archivo de inventario.")
        except Exception as e:
            print(Fore.RED + f"Error inesperado al guardar inventario: {e}")

    def agregar_producto(self, producto):
        # Método para agregar un producto al inventario.
        if producto.id in self._productos:
            print(Fore.RED + "Error: Ya existe un producto con ese ID. No se puede agregar.")
        else:
            self._productos[producto.id] = producto
            self.guardar_en_archivo()  # Guarda los cambios en el archivo.
            print(Fore.GREEN + f"Producto '{producto.nombre}' agregado con éxito.")

    def eliminar_producto(self, id):
        # Método para eliminar un producto del inventario.
        if id in self._productos:
            producto_eliminado = self._productos.pop(id)
            self.guardar_en_archivo()  # Guarda los cambios en el archivo.
            print(Fore.GREEN + f"Producto '{producto_eliminado.nombre}' eliminado con éxito.")
        else:
            print(Fore.RED + "Error: No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, nombre=None, cantidad=None, precio=None):
        # Método para actualizar un producto en el inventario.
        if id in self._productos:
            producto = self._productos[id]

            if nombre:
                producto.nombre = nombre
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio

            self.guardar_en_archivo()  # Guarda los cambios en el archivo.
            print(Fore.GREEN + f"Producto '{producto.nombre}' actualizado con éxito.")
        else:
            print(Fore.RED + "Error: No se encontró un producto con ese ID.")

    def buscar_por_nombre(self, nombre):
        # Método para buscar productos por nombre.
        resultados = [producto for producto in self._productos.values() if nombre.lower() in producto.nombre.lower()]
        if resultados:
            print(Fore.YELLOW + "\n--- Resultados de la búsqueda ---")
            for producto in resultados:
                print(f"{Fore.MAGENTA}Id: {Fore.WHITE}{producto.id} - {Fore.MAGENTA}"
                      f"Nombre: {Fore.WHITE}{producto.nombre} - {Fore.MAGENTA}"
                      f"Cantidad: {Fore.WHITE}{producto.cantidad} - {Fore.MAGENTA}"
                      f"Precio: {Fore.WHITE}${producto.precio:.2f}")
        else:
            print(Fore.RED + "No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        # Método para mostrar todos los productos en el inventario.
        if not self._productos:
            print(Fore.RED + "El inventario está vacío.")
        else:
            print(Fore.YELLOW + "\n--- Inventario ---")
            for producto in self._productos.values():
                # Muestra cada producto con colores específicos para cada campo.
                print(f"{Fore.MAGENTA}Id: {Fore.WHITE}{producto.id} - {Fore.MAGENTA}"
                      f"Nombre: {Fore.WHITE}{producto.nombre} - {Fore.MAGENTA}"
                      f"Cantidad: {Fore.WHITE}{producto.cantidad} - {Fore.MAGENTA}"
                      f"Precio: {Fore.WHITE}${producto.precio:.2f}")


# ==============================
# Función Principal: Menú de Usuario
# ==============================
def menu():
    inventario = Inventario()  # Crea una instancia de Inventario.

    while True:
        # Muestra el menú principal en un bucle infinito.
        print(Fore.CYAN + "\n--- Sistema de Gestión de Inventarios ---")
        print(Fore.WHITE + "1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Mostrar inventario")
        print("5. Buscar producto por nombre")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")  # Solicita al usuario que seleccione una opción.

        if opcion == "1":
            try:
                # Opción para agregar un nuevo producto.
                id = int(input("Ingrese el ID del producto (Utiliza solo numeros enteros): "))
                if id in inventario._productos:
                    print(Fore.RED + "Error: Ya existe un producto con ese ID. No se puede agregar.")
                else:
                    nombre = input("Ingrese el nombre del producto: ").strip()
                    cantidad = int(input("Ingrese la cantidad: "))
                    precio = float(input("Ingrese el precio: "))

                    producto = Producto(id, nombre, cantidad, precio)
                    inventario.agregar_producto(producto)
            except ValueError:
                print(Fore.RED + "Error: Entrada no válida. Asegúrese de ingresar números en los campos correspondientes.")

        elif opcion == "2":
            try:
                # Opción para eliminar un producto.
                id = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print(Fore.RED + "Error: El ID debe ser un número entero.")

        elif opcion == "3":
            try:
                # Opción para actualizar un producto.
                id = int(input("Ingrese el ID del producto a actualizar: "))
                nombre = input("Nuevo nombre (deje en blanco para no cambiar): ").strip() or None
                cantidad = input("Nueva cantidad (deje en blanco para no cambiar): ")
                cantidad = int(cantidad) if cantidad else None
                precio = input("Nuevo precio (deje en blanco para no cambiar): ")
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id, nombre, cantidad, precio)
            except ValueError:
                print(Fore.RED + "Error: Entrada no válida.")

        elif opcion == "4":
            # Opción para mostrar el inventario.
            inventario.mostrar_inventario()

        elif opcion == "5":
            # Opción para buscar productos por nombre.
            nombre = input("Ingrese el nombre del producto a buscar: ").strip()
            inventario.buscar_por_nombre(nombre)

        elif opcion == "6":
            # Opción para salir del programa.
            print(Fore.GREEN + "Saliendo del sistema...")
            break

        else:
            # Opción por defecto si la entrada no es válida.
            print(Fore.RED + "Opción no válida. Intente de nuevo.")


# Ejecución del programa
if __name__ == "__main__":
    menu()  # Llama a la función menu() si el script es ejecutado directamente.