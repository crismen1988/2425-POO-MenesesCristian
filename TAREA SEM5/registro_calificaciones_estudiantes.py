class Asignatura:
    """
    Clase que representa una asignatura con su nombre y calificación.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificacion = None  # Calificación inicialmente en blanco

    def ingresar_calificacion(self):
        """
        Solicita al usuario que ingrese una calificación válida (0 a 10) para la asignatura.
        """
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación para {self.nombre}: "))
                if 0 <= calificacion <= 10:
                    self.calificacion = calificacion
                    break
                else:
                    print("Error: La calificación debe estar en el rango de 0 a 10.")
            except ValueError:
                print("Error: Ingresa un número válido.")


class Estudiante:
    """
    Clase que representa a un estudiante con su nombre, asignaturas y promedio.
    """
    def __init__(self, nombre):
        self.nombre = nombre.capitalize()
        self.asignaturas = [Asignatura(nombre) for nombre in [
            "Matemáticas", "Ciencias Naturales", "Física",
            "Estudios Sociales", "Química", "Cívica",
            "Cultura Física", "Lengua y Literatura", "Inglés"
        ]]
        self.promedio = 0.0

    def ingresar_calificaciones(self):
        """
        Solicita las calificaciones para todas las asignaturas del estudiante.
        """
        print(f"\nIngresa las calificaciones para {self.nombre}:")
        for asignatura in self.asignaturas:
            asignatura.ingresar_calificacion()

    def calcular_promedio(self):
        """
        Calcula el promedio de las calificaciones del estudiante.
        """
        total = sum(asignatura.calificacion for asignatura in self.asignaturas)
        self.promedio = total / len(self.asignaturas)

    def mostrar_resultados(self):
        """
        Muestra las calificaciones y el promedio del estudiante.
        """
        print(f"\nEstudiante: {self.nombre}")
        for asignatura in self.asignaturas:
            print(f"{asignatura.nombre}: {asignatura.calificacion}")
        print(f"Promedio: {self.promedio:.2f}")
        print("Estado:", "Aprobado" if self.promedio >= 6 else "Reprobado")


class SistemaRegistro:
    """
    Clase que gestiona el registro y los resultados de los estudiantes.
    """
    def __init__(self):
        self.estudiantes = []

    def registrar_estudiante(self):
        """
        Registra un nuevo estudiante.
        """
        nombre = input("\nIngresa el nombre del estudiante: ")
        estudiante = Estudiante(nombre)
        estudiante.ingresar_calificaciones()
        estudiante.calcular_promedio()
        self.estudiantes.append(estudiante)

    def mostrar_resultados(self):
        """
        Muestra los resultados de todos los estudiantes registrados.
        """
        print("\n--- Resultados de los estudiantes ---")
        for estudiante in self.estudiantes:
            estudiante.mostrar_resultados()

    def ejecutar(self):
        """
        Ejecuta el sistema de registro de estudiantes.
        """
        while True:
            self.registrar_estudiante()
            continuar = input("¿Deseas registrar otro estudiante? (s/n): ").lower()
            if continuar != 's':
                break
        self.mostrar_resultados()


# Ejecutar el programa
if __name__ == "__main__":
    sistema = SistemaRegistro()
    sistema.ejecutar()
