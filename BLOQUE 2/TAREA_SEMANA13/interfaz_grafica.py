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
            messagebox.showinfo("Éxito", "Nombre y Apellido agregados correctamente.")
        else:
            messagebox.showwarning("Error", "Solo se permiten letras en el nombre y apellido.")
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, ingresa tanto el nombre como el apellido.")


# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)


# Función para eliminar el elemento seleccionado
def eliminar_seleccionado():
    try:
        seleccionado = lista.curselection()  # Obtener el índice del elemento seleccionado
        lista.delete(seleccionado)  # Eliminar el elemento seleccionado
    except:
        messagebox.showwarning("Error", "Ningún elemento seleccionado.")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("*** DATOS PERSONALES ***")
ventana.geometry("400x400")
ventana.configure(background="steel blue")

# Crear y colocar los componentes en la ventana
label_nombre = tk.Label(ventana, text="Nombre:", font=("Arial", 12, "bold"), bg="steel blue")
label_nombre.pack(pady=5)

entry_nombre = tk.Entry(ventana, width=40, bd=2)
entry_nombre.pack(pady=5)

label_apellido = tk.Label(ventana, text="Apellido:", font=("Arial", 12, "bold"), bg="steel blue")
label_apellido.pack(pady=5)

entry_apellido = tk.Entry(ventana, width=40, bd=2)
entry_apellido.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", font=("Arial", 10, "bold"), command=agregar_nombre, bd=5)
boton_agregar.pack(pady=10)

boton_limpiar = tk.Button(ventana, text="Borrar Todo", font=("Arial", 10, "bold"), command=limpiar_lista, bd=5)
boton_limpiar.pack(pady=5)

# Botón para eliminar el elemento seleccionado
boton_eliminar = tk.Button(ventana, text="Eliminar Un Elemento de la Lista", font=("Arial", 10, "bold"),
                           command=eliminar_seleccionado, bd=5)
boton_eliminar.pack(pady=5)

lista = tk.Listbox(ventana, width=40)
lista.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()