# Sistema de Gestión de una Tienda con Datos Ingresados por Teclado
# Ejemplo práctico de Programación Orientada a Objetos (POO) en Python

# Definimos la clase Producto
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        # Atributos de la clase Producto
        self.codigo = codigo  # Código único del producto
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio unitario
        self.stock = stock    # Cantidad disponible en stock

    # Método para mostrar información del producto
    def mostrar_informacion(self):
        print(f"Producto: {self.nombre} (Código: {self.codigo}), Precio: ${self.precio}, Stock: {self.stock}")

    # Método para actualizar el stock después de una venta
    def actualizar_stock(self, cantidad):
        if cantidad > self.stock:
            print(f"No hay suficiente stock de {self.nombre}.")
            return False
        self.stock -= cantidad
        return True


# Definimos la clase Cliente
class Cliente:
    def __init__(self, nombre, cedula_ruc, direccion, telefono):
        # Atributos de la clase Cliente
        self.nombre = nombre          # Nombre del cliente
        self.cedula_ruc = cedula_ruc  # Cédula o RUC del cliente
        self.direccion = direccion    # Dirección del cliente
        self.telefono = telefono      # Teléfono del cliente

    # Método para mostrar información del cliente
    def mostrar_informacion(self):
        print(f"Cliente: {self.nombre}, Cédula/RUC: {self.cedula_ruc}")
        print(f"Dirección: {self.direccion}, Teléfono: {self.telefono}")


# Definimos la clase Habitacion
class Habitacion:
    def __init__(self, numero, tipo, precio, disponible=True):
        # Atributos de la clase Habitacion
        self.numero = numero          # Número de la habitación
        self.tipo = tipo              # Tipo de habitación (simple, doble, suite, etc.)
        self.precio = precio          # Precio por noche
        self.disponible = disponible  # Disponibilidad de la habitación

    # Método para mostrar información de la habitación
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        print(f"Habitación {self.numero} ({self.tipo}): ${self.precio} - {estado}")

    # Método para ocupar la habitación
    def ocupar(self):
        if not self.disponible:
            print(f"La habitación {self.numero} ya está ocupada.")
            return False
        self.disponible = False
        return True

    # Método para liberar la habitación
    def liberar(self):
        self.disponible = True


# Definimos la clase Venta
class Venta:
    def __init__(self, cliente):
        # Atributos de la clase Venta
        self.cliente = cliente  # Objeto Cliente asociado
        self.productos = []     # Lista de productos comprados
        self.total = 0          # Costo total de la venta

    # Método para agregar un producto a la venta
    def agregar_producto(self, producto, cantidad):
        if producto.actualizar_stock(cantidad):
            self.productos.append((producto, cantidad))
            self.total += producto.precio * cantidad

    # Método para mostrar los detalles de la venta
    def mostrar_venta(self):
        print("--- Detalles de la Venta ---")
        self.cliente.mostrar_informacion()
        print("Productos comprados:")
        for producto, cantidad in self.productos:
            print(f"  - {producto.nombre} x{cantidad} (${producto.precio} c/u)")
        print(f"Total: ${self.total}")


# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Creación de habitaciones
    habitaciones = [
        Habitacion(101, "Simple", 50),
        Habitacion(102, "Doble", 80),
        Habitacion(103, "Suite", 120)
    ]

    while True:
        print("\nHabitaciones disponibles:")
        for habitacion in habitaciones:
            habitacion.mostrar_informacion()

        numero_habitacion = int(input("Ingrese el número de la habitación que desea ocupar (o 0 para salir): "))
        if numero_habitacion == 0:
            break

        # Buscar la habitación seleccionada
        habitacion_seleccionada = next((h for h in habitaciones if h.numero == numero_habitacion), None)

        if habitacion_seleccionada and habitacion_seleccionada.disponible:
            # Ingreso de datos del cliente
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            cedula_ruc_cliente = input("Ingrese la cédula o RUC del cliente: ")
            direccion_cliente = input("Ingrese la dirección del cliente: ")
            telefono_cliente = input("Ingrese el teléfono del cliente: ")

            cliente = Cliente(nombre_cliente, cedula_ruc_cliente, direccion_cliente, telefono_cliente)

            # Ocupar la habitación
            if habitacion_seleccionada.ocupar():
                print(f"La habitación {habitacion_seleccionada.numero} ha sido asignada a {cliente.nombre}.")
            else:
                print("No se pudo ocupar la habitación.")
        else:
            print("Número de habitación no válido o ya está ocupada.")

        # Preguntar si desea registrar otro cliente
        continuar = input("¿Desea registrar otro cliente? (S/N): ").lower()
        if continuar != "s":
            break

    print("\nEstado final de las habitaciones:")
    for habitacion in habitaciones:
        habitacion.mostrar_informacion()
