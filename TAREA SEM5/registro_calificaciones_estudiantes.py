# Programa para registrar las calificaciones de estudiantes en asignaturas fijas y calcular su promedio
# Las asignaturas son fijas y predefinidas en el programa. Las calificaciones deben estar en el rango de 0 a 10.

# Lista de asignaturas fijas
asignaturas = [
    "Matemáticas", "Ciencias Naturales", "Física",
    "Estudios Sociales", "Química", "Cívica",
    "Cultura Física", "Lengua y Literatura", "Inglés"
]

def ingresar_calificaciones():
    """
    Función que solicita las calificaciones de un estudiante para asignaturas fijas,
    asegurándose de que las calificaciones estén en el rango de 0 a 10.
    :return: Lista de calificaciones (list)
    """
    calificaciones = []
    print("Ingresa las calificaciones para las siguientes asignaturas (deben estar en el rango de 0 a 10):")
    for asignatura in asignaturas:
        while True:
            try:
                calificacion = float(input(f"{asignatura}: "))  # Ingresar calificación para cada asignatura
                if 0 <= calificacion <= 10:
                    calificaciones.append(calificacion)  # Guardar la calificación en la lista
                    break  # Salir del bucle si la calificación es válida
                else:
                    print("Error: La calificación debe estar en el rango de 0 a 10. Inténtalo de nuevo.")
            except ValueError:
                print("Error: Ingresa un número válido para la calificación.")
    return calificaciones

def calcular_promedio(calificaciones):
    """
    Función que calcula el promedio de las calificaciones de un estudiante.
    :param calificaciones: Lista de calificaciones (list)
    :return: Promedio de las calificaciones (float)
    """
    if len(calificaciones) == 0:
        return 0
    return sum(calificaciones) / len(calificaciones)  # Calcular el promedio

def registrar_estudiante():
    """
    Función que solicita el nombre y las calificaciones de un estudiante y devuelve un diccionario con la información.
    :return: Diccionario con nombre y calificaciones del estudiante (dict)
    """
    nombre = input("Ingresa el nombre del estudiante: ")  # Solicitar nombre del estudiante
    calificaciones = ingresar_calificaciones()  # Llamada a la función para ingresar las calificaciones
    promedio = calcular_promedio(calificaciones)  # Calcular el promedio de las calificaciones
    return {"nombre": nombre.capitalize(), "calificaciones": calificaciones, "promedio": promedio}  # Devolver la información

def mostrar_resultados(estudiantes):
    """
    Función que muestra los resultados de los estudiantes, incluyendo sus calificaciones y promedios.
    :param estudiantes: Lista de diccionarios con la información de los estudiantes (list)
    """
    for estudiante in estudiantes:
        print(f"\nEstudiante: {estudiante['nombre']}")
        for i, asignatura in enumerate(asignaturas):
            print(f"{asignatura}: {estudiante['calificaciones'][i]}")  # Mostrar las calificaciones por asignatura
        print(f"Promedio: {estudiante['promedio']:.2f}")
        if estudiante["promedio"] >= 6:
            print("Estado: Aprobado")
        else:
            print("Estado: Reprobado")

# Función principal que ejecuta el programa
def main():
    estudiantes = []  # Lista para almacenar los datos de los estudiantes
    continuar = True
    while continuar:
        estudiante = registrar_estudiante()  # Registrar un nuevo estudiante
        estudiantes.append(estudiante)  # Añadir el estudiante a la lista
        respuesta = input("¿Deseas registrar otro estudiante? (s/n): ").lower()  # Preguntar si se desea continuar
        if respuesta != "s":
            continuar = False

    # Mostrar los resultados de todos los estudiantes
    mostrar_resultados(estudiantes)

# Ejecutar el programa
if __name__ == "__main__":
    main()
