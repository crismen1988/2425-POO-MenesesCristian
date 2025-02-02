# Función para obtener las temperaturas diarias
def obtener_temperaturas():
    temperaturas = []  # Inicializamos una Lista para almacenar las temperaturas
    for i in range(7):  # Solicitamos las temperaturas para los 7 días
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i+1}: "))  # Pedimos las temperaturas diarias
                if temp > 40:
                    print("La temperatura no puede ser mayor a 40 grados. Intente nuevamente.")
                else:
                    temperaturas.append(temp)  # Añadimos la temperatura a la lista
                    break  # Salimos del bucle si el dato es válido
            except ValueError:  # Producimos un error si el ingreso es un dato erroneo
                print("Por favor, ingrese un número válido para la temperatura.")
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    suma_temperaturas = 0
    for temp in temperaturas:  # Sumamos todas las temperaturas utilizando un bucle
        suma_temperaturas += temp
    promedio = suma_temperaturas / len(temperaturas)  # Calculamos el promedio
    return promedio

# Función para mostrar el resultado
def mostrar_resultado(promedio):
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f} °C")

print("Programa para calcular el promedio semanal del clima.")
temperaturas = obtener_temperaturas()  # Obtenemos las temperaturas para los 7 días
promedio = calcular_promedio(temperaturas)  # Calculamos el promedio
mostrar_resultado(promedio)  # Mostramos el resultado final
