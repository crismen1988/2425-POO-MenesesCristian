#El nuevo código del dashboard hace uso de la librería colorama para mejorar la experiencia visual del usuario
#con colores aplicados a los títulos, opciones de menú, mensajes de error, y otros textos relevantes.
#Se añadio una espera breve antes de ejecutar el script para mejorar la fluidez de la interacción.
#Se utilizaron colores llamativos para hacer que el menú y las interacciones sean más claras y atractivas para el usuario.
#Estas modificaciones hacen que el código sea más visualmente atractivo y fácil de usar


import os
import subprocess
import time
from colorama import Fore, Style, init

# Inicializa colorama para colorear texto en la consola
init(autoreset=True)

def mostrar_codigo(ruta_script):
    """Muestra el contenido de un script Python en la consola."""
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n{Fore.CYAN}--- Código de {ruta_script} ---{Style.RESET_ALL}\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print(f"{Fore.RED}Error: El archivo no se encontró.{Style.RESET_ALL}")
        return None
    except Exception as e:
        print(f"{Fore.RED}Error al leer el archivo: {e}{Style.RESET_ALL}")
        return None

def ejecutar_codigo(ruta_script):
    """Ejecuta un script Python en una nueva ventana de terminal."""
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Mac/Linux
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"{Fore.RED}Error al ejecutar el código: {e}{Style.RESET_ALL}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    # Se definen manualmente las carpetas permitidas
    unidades = {
        '1': os.path.join(ruta_base, 'Bloque 1'),
        '2': os.path.join(ruta_base, 'Bloque 2')
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key, nombre in unidades.items():
            print(f"{key} - {os.path.basename(nombre)}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(unidades[eleccion_unidad])  # Pasamos la ruta correcta
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


def mostrar_sub_menu(ruta_unidad):
    """Muestra las subcarpetas dentro de una unidad específica."""
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print(f"\n{Fore.MAGENTA}{'='*30}")
        print(f"  📂 SUBMENÚ - {os.path.basename(ruta_unidad)}")
        print(f"{'='*30}{Style.RESET_ALL}")

        # Mostrar las subcarpetas detectadas
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{Fore.CYAN}{i}{Style.RESET_ALL} - {carpeta}")
        print(f"{Fore.RED}0 - Regresar al menú principal{Style.RESET_ALL}")

        eleccion_carpeta = input("\nElige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print(f"{Fore.RED}Opción no válida. Inténtalo de nuevo.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Por favor, ingresa un número válido.{Style.RESET_ALL}")

def mostrar_scripts(ruta_sub_carpeta):
    """Muestra los scripts disponibles en una subcarpeta y permite ejecutarlos."""
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print(f"\n{Fore.LIGHTBLUE_EX}{'='*30}")
        print(f"  📝 SCRIPTS DISPONIBLES")
        print(f"{'='*30}{Style.RESET_ALL}")

        # Mostrar los scripts disponibles en la carpeta
        for i, script in enumerate(scripts, start=1):
            print(f"{Fore.GREEN}{i}{Style.RESET_ALL} - {script}")
        print(f"{Fore.RED}0 - Regresar al submenú anterior")
        print(f"9 - Regresar al menú principal{Style.RESET_ALL}")

        eleccion_script = input("\nElige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input(f"{Fore.YELLOW}¿Deseas ejecutar el script? (1: Sí, 0: No): {Style.RESET_ALL}")
                        if ejecutar == '1':
                            print(f"{Fore.BLUE}Ejecutando script...{Style.RESET_ALL}")
                            time.sleep(1)
                            ejecutar_codigo(ruta_script)
                        else:
                            print(f"{Fore.RED}El script no fue ejecutado.{Style.RESET_ALL}")
                        input(f"{Fore.CYAN}\nPresiona Enter para volver al menú de scripts.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Opción no válida. Inténtalo de nuevo.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Por favor, ingresa un número válido.{Style.RESET_ALL}")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
