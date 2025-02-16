from colorama import Fore, init

# Inicializa colorama para que funcione en todos los sistemas operativos
init(autoreset=True)

# ==============================
# Clase Producto
# ==============================
# Esta clase representa un producto en el inventario.
# Definimos la clase Producto para manejar información de productos
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        # Atributos privados para encapsulamiento
        self._id = id   # ID único del producto (inmutable)
        self._nombre = nombre  # Nombre del producto
        self._cantidad = cantidad    # Cantidad disponible en inventario
        self._precio = precio   # Precio del producto

    # Getters (Métodos para obtener valores de los atributos)
    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def precio(self):
        return self._precio

    # Setters con validación (No hay setter para ID, es inmutable)
    @nombre.setter
    def nombre(self, nuevo_nombre):
        # Validación: El nombre debe ser una cadena no vacía
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre.strip()
        else:
            print(Fore.RED + "Error: El nombre no puede estar vacío.")

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        # Validación: La cantidad debe ser un número entero no negativo
        if isinstance(nueva_cantidad, int) and nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            print(Fore.RED + "Error: La cantidad debe ser un número entero no negativo.")

    @precio.setter
    def precio(self, nuevo_precio):
        # Validación: El precio debe ser un número no negativo (int o float)
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print(Fore.RED + "Error: El precio debe ser un número no negativo.")

    # Método especial para mostrar la información del producto de forma legible y colorida
    def __str__(self):
        # Muestra el producto con colores diferenciados para etiquetas y valores
        return f"{Fore.GREEN}ID:{Fore.WHITE}{self._id}  {Fore.GREEN}Nombre: {Fore.WHITE}{self._nombre}  {Fore.GREEN}Cantidad: {Fore.WHITE}{self._cantidad}  {Fore.GREEN}Precio: {Fore.WHITE}${self._precio:.2f}"


# ==============================
# Clase Inventario
# ==============================
# Clase Inventario para gestionar productos
class Inventario:
    def __init__(self):
        # Diccionario para almacenar productos usando el ID como clave
        self._productos = {}

    def agregar_producto(self, producto):
        # Verifica si el ID del producto ya existe en el inventario
        if producto.id in self._productos:
            print(Fore.RED + "Error: Ya existe un producto con ese ID.")
            return False
        else:
            # Agrega el producto al inventario
            self._productos[producto.id] = producto
            print(Fore.GREEN + f"Producto '{producto.nombre}' agregado con éxito.")
            return True

    def eliminar_producto(self, id):
        # Elimina un producto por su ID
        if id in self._productos:
            producto_eliminado = self._productos.pop(id)
            print(Fore.GREEN + f"Producto '{producto_eliminado.nombre}' eliminado con éxito.")
        else:
            print(Fore.RED + "Error: No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, nombre=None, cantidad=None, precio=None):
        # Actualiza la información de un producto existente
        if id in self._productos:
            producto = self._productos[id]

            # Si se proporciona un nombre válido, se actualiza
            if nombre is not None:
                if isinstance(nombre, str) and nombre.strip():
                    producto.nombre = nombre.strip()
                else:
                    print(Fore.RED + "Error: El nombre no puede estar vacío.")

            # Si se proporciona una cantidad válida, se actualiza
            if cantidad is not None:
                producto.cantidad = cantidad

            # Si se proporciona un precio válido, se actualiza
            if precio is not None:
                producto.precio = precio

            print(Fore.GREEN + f"Producto '{producto.nombre}' actualizado con éxito.")
        else:
            print(Fore.RED + "Error: No se encontró un producto con ese ID.")

    def buscar_producto_por_id(self, id):
        # Busca un producto por su ID y lo muestra si existe
        if id in self._productos:
            print(Fore.YELLOW + "Producto encontrado:")
            print(Fore.MAGENTA + self._productos[id].__str__())
        else:
            print(Fore.RED + "Error: No se encontró un producto con ese ID.")

    def mostrar_inventario(self):
        # Muestra todos los productos en el inventario
        if not self._productos:
            print(Fore.RED + "El inventario está vacío.")
        else:
            print(Fore.YELLOW + "\n--- Inventario ---")
            for producto in self._productos.values():
                print(Fore.MAGENTA + f"{producto}")


# ==============================
# Función Principal: Menú de Usuario
# ==============================
def menu():
    inventario = Inventario()# Crea un objeto Inventario para gestionar productos

    # Bucle infinito para mostrar el menú hasta que el usuario decida salir
    while True:
        print(Fore.CYAN + "\n--- Sistema de Gestión de Inventarios ---")
        print(Fore.WHITE + "1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por ID")
        print("5. Mostrar inventario")
        print("6. Salir")

        # Solicita al usuario que elija una opción del menú
        opcion = input("Seleccione una opción (1-6): ")

        # Opción 1: Agregar producto
        if opcion == "1":
            while True:
                try:
                    id = int(input(Fore.WHITE + "\nIngrese el ID del producto: "))
                    if id in inventario._productos:
                        print(Fore.RED + "Error: El ID ya existe.")
                    else:
                        break
                except ValueError:
                    print(Fore.RED + "Error: El ID debe ser un número entero.")

            nombre = input(Fore.WHITE + "Ingrese el nombre del producto: ")

            while True:
                cantidad = input(Fore.WHITE + "Ingrese la cantidad: ")
                try:
                    cantidad = int(cantidad)
                    if cantidad >= 0:
                        break
                    else:
                        print(Fore.RED + "Error: La cantidad no puede ser negativa.")
                except ValueError:
                    print(Fore.RED + "Error: La cantidad debe ser un número entero no negativo.")

            while True:
                precio = input(Fore.WHITE + "Ingrese el precio: ")
                try:
                    precio = float(precio)
                    if precio > 0:
                        break
                    else:
                        print(Fore.RED + "Error: El precio no puede ser negativo.")
                except ValueError:
                    print(Fore.RED + "Error: Debe ingresar un número válido para el precio.")

            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            # Eliminar producto por ID
            try:
                id = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print(Fore.RED + "Error: El ID debe ser un número entero.")

        elif opcion == "3":
            # Actualizar producto
            try:
                id = int(input("Ingrese el ID del producto a actualizar: "))

                nombre = input("Ingrese el nuevo nombre (deje en blanco para no cambiar): ")
                if not nombre.strip():
                    nombre = None

                cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
                if cantidad.strip():
                    try:
                        cantidad = int(cantidad)
                        if cantidad < 0:
                            print(Fore.RED + "Error: La cantidad no puede ser negativa.")
                            cantidad = None
                    except ValueError:
                        print(Fore.RED + "Error: La cantidad debe ser un número entero no negativo.")
                        cantidad = None

                precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
                if precio.strip():
                    try:
                        precio = float(precio)
                        if precio < 0:
                            print(Fore.RED + "Error: El precio no puede ser negativo.")
                            precio = None
                    except ValueError:
                        print(Fore.RED + "Error: Debe ingresar un número válido para el precio.")
                        precio = None

                inventario.actualizar_producto(id, nombre, cantidad, precio)
            except ValueError:
                print(Fore.RED + "Error: El ID debe ser un número entero.")

        elif opcion == "4":
            # Buscar un producto
            try:
                id = int(input("Ingrese el ID del producto a buscar: "))
                inventario.buscar_producto_por_id(id)
            except ValueError:
                print(Fore.RED + "Error: El ID debe ser un número entero.")

        elif opcion == "5":
            # Muestratodo el inventario
            inventario.mostrar_inventario()

        elif opcion == "6":
            print(Fore.GREEN + "Saliendo del sistema...")
            break

        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.")

# Ejecucion del programa
if __name__ == "__main__":
    menu()
