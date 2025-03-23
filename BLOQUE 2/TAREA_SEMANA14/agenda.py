import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Importa el widget de calendario

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")  # Título de la ventana

        # Frame para contener la lista de eventos
        self.frame_lista = ttk.Frame(root)
        self.frame_lista.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Treeview para mostrar los eventos en forma de tabla
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")  # Encabezado de la columna Fecha
        self.tree.heading("Hora", text="Hora")  # Encabezado de la columna Hora
        self.tree.heading("Descripción", text="Descripción")  # Encabezado de la columna Descripción
        self.tree.pack(fill=tk.BOTH, expand=True)  # Hace que el Treeview ocupe todo el espacio disponible

        # Frame para los campos de entrada de datos
        self.frame_entrada = ttk.Frame(root)
        self.frame_entrada.pack(padx=10, pady=10, fill=tk.X)

        # Etiqueta y campo de entrada para la fecha
        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(self.frame_entrada, date_pattern='yyyy-mm-dd')  # Widget de calendario
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y campo de entrada para la hora
        ttk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.hora_entry = ttk.Entry(self.frame_entrada)  # Campo de texto para la hora
        self.hora_entry.grid(row=1, column=1, padx=5, pady=5)

        # Etiqueta y campo de entrada para la descripción
        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.descripcion_entry = ttk.Entry(self.frame_entrada)  # Campo de texto para la descripción
        self.descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame para los botones
        self.frame_botones = ttk.Frame(root)
        self.frame_botones.pack(padx=10, pady=10, fill=tk.X)

        # Botón para agregar un evento
        ttk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=5)

        # Botón para eliminar el evento seleccionado
        ttk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side=tk.LEFT, padx=5)

        # Botón para borrar todos los eventos
        ttk.Button(self.frame_botones, text="Borrar Todo", command=self.borrar_todo).pack(side=tk.LEFT, padx=5)

        # Botón para salir de la aplicación
        ttk.Button(self.frame_botones, text="Salir", command=root.quit).pack(side=tk.RIGHT, padx=5)

    def agregar_evento(self):
        # Obtiene los valores de los campos de entrada
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        # Verifica que todos los campos estén completos
        if fecha and hora and descripcion:
            # Insertar el evento en el Treeview
            self.tree.insert("", tk.END, values=(fecha, hora, descripcion))
            # Limpia los campos de entrada después de agregar el evento
            self.fecha_entry.set_date(None)
            self.hora_entry.delete(0, tk.END)
            self.descripcion_entry.delete(0, tk.END)
        else:
            # Muestra una advertencia si algún campo está vacío
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        # Obtiene el evento seleccionado en el Treeview
        seleccionado = self.tree.selection()
        if seleccionado:
            # Pide confirmación antes de eliminar
            confirmacion = messagebox.askyesno("Eliminar Evento", "¿Estás seguro de que deseas eliminar el evento seleccionado?")
            if confirmacion:
                # Elimina el evento seleccionado
                self.tree.delete(seleccionado)
        else:
            # Muestra una advertencia si no hay ningún evento seleccionado
            messagebox.showwarning("Nada seleccionado", "Por favor, selecciona un evento para eliminar.")

    def borrar_todo(self):
        # Verifica si hay eventos en el Treeview
        if self.tree.get_children():
            # Pide confirmación antes de borrar todos los eventos
            confirmacion = messagebox.askyesno("Borrar Todo", "¿Estás seguro de que deseas borrar todos los eventos?")
            if confirmacion:
                # Elimina todos los eventos del Treeview
                for item in self.tree.get_children():
                    self.tree.delete(item)
        else:
            # Muestra una advertencia si no hay eventos para borrar
            messagebox.showwarning("Lista vacía", "No hay eventos para borrar.")

if __name__ == "__main__":
    # Crea la ventana principal de la aplicación
    root = tk.Tk()
    # Instancia la clase AgendaApp
    app = AgendaApp(root)
    # Inicia el bucle principal de la aplicación
    root.mainloop()