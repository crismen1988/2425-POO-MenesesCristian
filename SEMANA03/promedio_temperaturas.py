# Función para obtener las temperaturas diarias
def obtener_temperaturas():
    temperaturas = []  # Lista vacía para almacenar las temperaturas
    for i in range(7):  # Solicitar temperaturas para los 7 días
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i+1}: "))  # Pedir temperatura diaria
                if temp > 45:
                    print("La temperatura no puede ser mayor a 45 grados. Intente nuevamente.")
                else:
                    temperaturas.append(temp)  # Agregar la temperatura a la lista
                    break  # Salir del bucle si el dato es válido
            except ValueError:  # Manejar el error si no se ingresa un número válido
                print("Por favor, ingrese un número válido para la temperatura.")
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    suma_temperaturas = 0
    for temp in temperaturas:  # Sumar todas las temperaturas utilizando un bucle
        suma_temperaturas += temp
    promedio = suma_temperaturas / len(temperaturas)  # Calcular el promedio
    return promedio

# Función para mostrar el resultado
def mostrar_resultado(promedio):
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f} °C")

# Flujo del programa directamente
print("Programa para calcular el promedio semanal del clima.")
temperaturas = obtener_temperaturas()  # Obtener las temperaturas para los 7 días
promedio = calcular_promedio(temperaturas)  # Calcular el promedio
mostrar_resultado(promedio)  # Mostrar el resultado final
