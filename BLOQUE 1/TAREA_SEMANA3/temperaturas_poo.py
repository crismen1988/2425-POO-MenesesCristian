class ClimaDiario:
    def __init__(self, temperatura):
        # Definimos la temperatura como un atributo privado
        if temperatura > 45:
            raise ValueError("La temperatura no puede ser mayor a 45 grados.")
        self.__temperatura = temperatura  # Atributo privado para la temperatura

    # Método para obtener la temperatura
    def obtener_temperatura(self):
        return self.__temperatura

    # Método para mostrar la temperatura
    def mostrar_temperatura(self):
        print(f"Temperatura del día: {self.__temperatura} °C")

class SemanaClima:
    def __init__(self):
        self.__dias = []  # Lista para almacenar los días de la semana

    # Método para agregar un clima diario a la semana
    def agregar_clima_diario(self, temperatura):
        clima = ClimaDiario(temperatura)  # Crea una instancia de ClimaDiario
        self.__dias.append(clima)  # Añade el clima a la lista

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        #sumamos las temperaturas
        suma_temperaturas = sum([clima.obtener_temperatura() for clima in self.__dias])
        promedio = suma_temperaturas / len(self.__dias) if self.__dias else 0
        return promedio

    # Método para mostrar el promedio
    def mostrar_promedio(self):
        #Calculamos el promedio
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f} °C")


semana_clima = SemanaClima()  # Crea una instancia llamada SemanaClima

print("Programa para calcular el promedio semanal del clima.")

# Ingresa las temperaturas para los 7 días de la semana
for i in range(7):
    while True:
        try:
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            semana_clima.agregar_clima_diario(temp)  # Agrega el clima diario a la semana
            break  # Salimos del bucle si el dato es válido
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")

# Mostramos el resultado obtenido del promedio semanal
semana_clima.mostrar_promedio()  
