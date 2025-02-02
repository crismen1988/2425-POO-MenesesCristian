# Sistema de Gestión de una Tienda con Datos Ingresados por Teclado
# Ejemplo práctico de Programación Orientada a Objetos (POO) en Python

print("**** Tienda ****")
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
        print(f"Producto: {self.nombre}\tCódigo: {self.codigo}\tPrecio: ${self.precio}\tStock: {self.stock}")

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
    # Ingreso de datos del cliente
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cedula_ruc_cliente = input("Ingrese la cédula o RUC del cliente: ")
    direccion_cliente = input("Ingrese la dirección del cliente: ")
    telefono_cliente = input("Ingrese el teléfono del cliente: ")
    cliente1 = Cliente(nombre_cliente, cedula_ruc_cliente, direccion_cliente, telefono_cliente)

    # Creamos algunos productos
    producto1 = Producto("001", "Laptop", 800, 10)
    producto2 = Producto("002", "Mouse", 20, 50)
    producto3 = Producto("003", "Teclado", 40, 30)

    # Creamos una venta
    venta1 = Venta(cliente1)

    # Agregamos productos a la venta con datos ingresados por teclado
    while True:
        print("\nProductos disponibles:")
        producto1.mostrar_informacion()
        producto2.mostrar_informacion()
        producto3.mostrar_informacion()

        codigo_producto = input("Ingrese el código del producto que desea comprar (o 's' para finalizar): ")
        if codigo_producto.lower() == 's':
            break
           
        cantidad_productos = int(input("Ingrese la cantidad que desea comprar: "))

        if codigo_producto == "001":
            venta1.agregar_producto(producto1, cantidad_productos)
        elif codigo_producto == "002":
            venta1.agregar_producto(producto2, cantidad_productos)
        elif codigo_producto == "003":
            venta1.agregar_producto(producto3, cantidad_productos)
        else:
            print("Código de producto no válido.")
            break

        # Preguntar si desea agregar otro producto
        agregar_mas = input("¿Desea agregar otro producto? (s/n): ").lower()
        if agregar_mas != 's':
            break

    # Mostramos los detalles de la venta
    print("\nDetalles de la venta:")
    venta1.mostrar_venta()

    # Mostramos el estado final de los productos
    # Mostramos Inventario descontado los productos vendidos
    print("\nEstado final de los productos:")
    producto1.mostrar_informacion()
    producto2.mostrar_informacion()
    producto3.mostrar_informacion()
