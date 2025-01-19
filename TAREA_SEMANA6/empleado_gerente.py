# Clase Base
class Empleado:
    def __init__(self, nombre, apellido, salario):
        # Encapsulación: El atributo __salario es privado
        self.nombre = nombre
        self.apellido = apellido
        self.__salario = salario  # Atributo privado, no se puede acceder fuera de la clase

    # Método para mostrar la información del empleado
    def mostrar_informacion(self):
        print(f"""Datos del Empleado 
              Nombre: {self.nombre} 
              Apellido: {self.apellido}
              Salario: {self.__salario} $""")

    # Método para modificar el salario
    def modificar_salario(self):
        print("Al empleado se le debe dar un aumento de salario")
        salir = False
        # Mientras no se ingrese un salario acorde el sistema seguira pidiendo un salario correcto
        while not salir:
            nuevo_salario = float(input("Ingrese el nuevo salario del empleado: "))
            # Aseguramos que el nuevo salario sea mayor que el actual
            if nuevo_salario > self.__salario:
                self.__salario = nuevo_salario
                salir = True
            else:
                print("El nuevo salario no debe ser menor al salario actual")

    # Método para obtener el salario (Encapsulación)
    def obtener_salario(self):
        return self.__salario  # Retorna el salario, no se puede acceder directamente al atributo privado


# Definición de la Clase derivada (Herencia)
class Gerente(Empleado):  # Herencia de la clase Empleado
    def __init__(self, nombre, apellido, salario, cargo):
        # Llamada al constructor de la clase base para inicializar los atributos heredados
        super().__init__(nombre, apellido, salario)
        self.cargo = cargo  # Atributo específico de la clase Gerente

    # Sobrescritura del método 'mostrar_informacion' (Polimorfismo)
    def mostrar_informacion(self):
        print(f"""Datos del Gerente 
        Nombre: {self.nombre} 
        Apellido: {self.apellido}
        Salario: {self.obtener_salario()} $
        Cargo: {self.cargo}""")  # Sobrescribe la informacion para agregar más detalles


# Función principal para demostrar el uso de las clases y la herencia
def main():
    # Creación de un objeto de la clase Empleado (Definición de objeto)
    empleado = Empleado("Cristian", "Meneses", 460)
    # Llamada al método 'mostrar_informacion' de la clase base
    empleado.mostrar_informacion()
    # Modificación del salario del empleado
    empleado.modificar_salario()
    print(f"El nuevo salario de {empleado.nombre} {empleado.apellido} es: {empleado.obtener_salario()} $")

    # Creación de un objeto de la clase Gerente (Definición de objeto, usando la clase derivada)
    gerente = Gerente("Alexandra", "Moreta", 800, "Gerente")
    # Llamada al método 'mostrar_informacion' de la clase derivada (Polimorfismo)
    gerente.mostrar_informacion()

# Ejecución del programa
main()
