import tkinter as tk
from tkinter import messagebox


# Función para agregar nombre y apellido a la lista
def agregar_nombre():
    nombre = entry_nombre.get().capitalize()
    apellido = entry_apellido.get().capitalize()

    if nombre and apellido:  # Verifica que ambos campos no estén vacíos
        if nombre.isalpha() and apellido.isalpha(): #Verifica que el dato ingresado sea solo letras
            nombre_completo = f"{nombre} {apellido}" #Nombre y Apellido se adigna a la variable
            lista.insert(tk.END, nombre_completo) #
            entry_nombre.delete(0, tk.END)  # Limpiar el campo de nombre
            entry_apellido.delete(0, tk.END)  # Limpiar el campo de apellido
            messagebox.showinfo("Éxito", "Nombre y Apellido agregados correctamente.") #Muestra un mensaje de exito
        else:
            messagebox.showwarning("Error", "Solo se permiten letras en el nombre y apellido.") #Muestra un mensaje de rror
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, ingresa tanto el nombre como el apellido.") #Muestra mensaje de error campo vacio


# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END) #Borra todos los elementos de la Lista


# Función para eliminar el elemento seleccionado
def eliminar_seleccionado():
    try:
        seleccionado = lista.curselection()  # Obtener el índice del elemento seleccionado
        lista.delete(seleccionado)  # Eliminar el elemento seleccionado
    except:
        messagebox.showwarning("Error", "Ningún elemento seleccionado.") #Mensaje de error cuando no se selcciona algun elemento


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("*** DATOS PERSONALES ***") #Agrega un titulo a la ventana
ventana.geometry("400x400") #Configura ancho y altura de la ventana
ventana.configure(background="steel blue")

# Crear y colocar los componentes en la ventana
label_nombre = tk.Label(ventana, text="Nombre:", font=("Arial", 12, "bold"), bg="steel blue") #Crea Label
label_nombre.pack(pady=5) #Muestra en pantalla el Label

entry_nombre = tk.Entry(ventana, width=40, bd=2) #Agrega un campo para ingreso de nombre
entry_nombre.pack(pady=5) #Muestra en la ventana el espacio para ingresar el nombre

label_apellido = tk.Label(ventana, text="Apellido:", font=("Arial", 12, "bold"), bg="steel blue") #Crea un Label
label_apellido.pack(pady=5) #Muestra en pantalla el Label

entry_apellido = tk.Entry(ventana, width=40, bd=2) #Agrega un campo para ingreso de apellido
entry_apellido.pack(pady=5) #Muestra en la ventana el espacio para ingresar el apellido

boton_agregar = tk.Button(ventana, text="Agregar", font=("Arial", 10, "bold"), command=agregar_nombre, bd=5) #Crea un Boton agregar en la ventana
boton_agregar.pack(pady=10)#Muestra el boton en la ventana

boton_limpiar = tk.Button(ventana, text="Borrar Todo", font=("Arial", 10, "bold"), command=limpiar_lista, bd=5) #Crea un Boton Borrar todo en la ventana
boton_limpiar.pack(pady=5)#Muestra el boton en la ventana

# Botón para eliminar el elemento seleccionado
boton_eliminar = tk.Button(ventana, text="Eliminar Un Elemento de la Lista", font=("Arial", 10, "bold"),
                           command=eliminar_seleccionado, bd=5)
boton_eliminar.pack(pady=5)#Muestra el boton en la ventana

lista = tk.Listbox(ventana, width=40) #Crea un espacio  en la ventana para la lista
lista.pack(pady=10)#Muestra la Lista en la ventana

# Iniciar el bucle principal de la aplicación
ventana.mainloop()