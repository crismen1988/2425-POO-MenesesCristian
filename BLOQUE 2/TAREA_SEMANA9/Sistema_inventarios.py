from colorama import Fore

# Definimos la clase Producto para manejar información de productos
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        # Atributos privados para encapsulamiento
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
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

    # Setters con validación
    @id.setter
    def id(self, nuevo_id):
        if isinstance(nuevo_id, int) and nuevo_id > 0:
            self._id = nuevo_id
        else:
            print(Fore.RED + "Error: El ID debe ser un número entero positivo.")

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre.strip()
        else:
            print(Fore.RED + "Error: El nombre no puede estar vacío.")

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if isinstance(nueva_cantidad, int) and nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            print(Fore.RED + "Error: La cantidad debe ser un número entero no negativo.")

    @precio.setter
    def precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print(Fore.RED + "Error: El precio debe ser un número no negativo.")

    def __str__(self):
        return f"{Fore.GREEN}ID:{Fore.WHITE}{self._id}  {Fore.GREEN}Nombre: {Fore.WHITE}{self._nombre}  {Fore.GREEN}Cantidad: {Fore.WHITE}{self._cantidad}  {Fore.GREEN}Precio: {Fore.WHITE}${self._precio:.2f}"


# Clase Inventario para gestionar productos
class Inventario:
    def __init__(self):
        self._productos = {}

    def agregar_producto(self, producto):
        if producto.id in self._productos:
            return False
        else:
            self._productos[producto.id] = producto
            return True

    def eliminar_producto(self, id):
        if id in self._productos:
            producto_eliminado = self._productos.pop(id)
            print(Fore.GREEN + f"Producto '{producto_eliminado.nombre}' eliminado con éxito.")
        else:
            print(Fore.RED + "Error: No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self._productos:
            producto = self._productos[id]
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
        if id in self._productos:
            print(Fore.YELLOW + "Producto encontrado:")
            print(self._productos[id].__str__())
        else:
            print(Fore.RED + "Error: No se encontró un producto con ese ID.")

    def mostrar_inventario(self):
        if not self._productos:
            print(Fore.RED + "El inventario está vacío.")
        else:
            print(Fore.YELLOW + "\n--- Inventario ---")
            for producto in self._productos.values():
                print(f"{producto}")


# Función principal para el menú del sistema de inventario
def menu():
    inventario = Inventario()

    while True:
        print(Fore.CYAN + "\n--- Sistema de Gestión de Inventarios ---")
        print(Fore.WHITE + "1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por ID")
        print("5. Mostrar inventario")
        print("6. Salir")

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

            # Validación de cantidad
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

            # Validación de precio
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
            if inventario.agregar_producto(producto):
                print(Fore.GREEN + f"Producto '{producto.nombre}' agregado con éxito.")

        # Opción 2: Eliminar producto
        elif opcion == "2":
            try:
                id = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print(Fore.RED + "Error: El ID debe ser un número entero.")

        # Opción 3: Actualizar producto
        elif opcion == "3":
            try:
                id = int(input("Ingrese el ID del producto a actualizar: "))

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

                inventario.actualizar_producto(id, cantidad, precio)
            except ValueError:
                print(Fore.RED + "Error: El ID debe ser un número entero.")

        elif opcion == "4":
            try:
                id = int(input("Ingrese el ID del producto a buscar: "))
                inventario.buscar_producto_por_id(id)
            except ValueError:
                print(Fore.RED + "Error: El ID debe ser un número entero.")

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print(Fore.GREEN + "Saliendo del sistema...")
            break

        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
