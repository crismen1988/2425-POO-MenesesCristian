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
              Salario: {self.__salario:.2f} $""")

    # Método para modificar el salario
    def set_salario(self, nuevo_salario):
        # Aseguramos que el nuevo salario sea mayor que el actual
        if nuevo_salario > self.__salario:
            self.__salario = nuevo_salario
        else:
            print("El nuevo salario no debe ser menor al salario actual")

    # Método para obtener el salario (Encapsulación)
    def get_salario(self):
        return self.__salario  # Retorna el salario, no se puede acceder directamente al atributo privado


# Definición de la Clase derivada (Herencia)
class Gerente(Empleado):  # Herencia de la clase Empleado
    def __init__(self, nombre, apellido, salario, cargo):
        # Llamada al constructor de la clase base para inicializar los atributos heredados
        super().__init__(nombre, apellido, salario)
        self.cargo = cargo  # Atributo específico de la clase Gerente

    # Sobrescritura del método 'mostrar_informacion' (Polimorfismo)
    def mostrar_informacion(self):
        print(f"""\nDatos del Gerente 
        Nombre: {self.nombre} 
        Apellido: {self.apellido}
        Salario: {self.get_salario():.2f} $
        Cargo: {self.get_cargo()}""")  # Sobrescribe la informacion para agregar más detalles

    # Método para obtener el cargo (Encapsulación)
    def get_cargo(self):
        return self.cargo  # Retorna el cargo del gerente


# Función principal para demostrar el uso de las clases y la herencia
def main():
    # Creación de un objeto de la clase Empleado
    empleado = Empleado("Cristian", "Meneses", 460)
    # Llamada al método 'mostrar_informacion' de la clase base
    empleado.mostrar_informacion()
    # Modificación del salario del empleado
    nuevo_salario = float(input("Ingrese el nuevo salario del empleado: "))
    empleado.set_salario(nuevo_salario)
    print(f"El nuevo salario de {empleado.nombre} {empleado.apellido} es: {empleado.get_salario():.2f} $")

    # Creación de un objeto de la clase Gerente
    gerente = Gerente("Alexandra", "Moreta", 800, "Gerente General")
    # Llamada al método 'mostrar_informacion' de la clase derivada
    gerente.mostrar_informacion()

# Ejecución del programa
main()
