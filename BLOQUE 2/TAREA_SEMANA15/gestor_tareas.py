# Importa la biblioteca tkinter para la interfaz gráfica
import tkinter as tk
# Importa el módulo ttk (widgets temáticos) y messagebox (ventanas emergentes) de tkinter
from tkinter import ttk, messagebox
# Importa la clase Font para manejar fuentes de texto
from tkinter.font import Font


# Define la clase principal de la aplicación
class AplicacionTareas:
    # Método constructor, recibe la ventana principal (root)
    def __init__(self, root):
        self.root = root  # Guarda la referencia a la ventana principal
        self.root.title("Gestor de Tareas")  # Establece el título de la ventana
        self.root.geometry("650x450")  # Define el tamaño inicial de la ventana

        # Llama a métodos para configurar la aplicación
        self.configurar_estilos()  # Configura estilos visuales
        self.tareas = []  # Inicializa lista vacía para almacenar tareas
        self.crear_widgets()  # Crea todos los elementos de la interfaz
        self.configurar_eventos()  # Configura eventos

    # Método para configurar estilos visuales
    def configurar_estilos(self):
        self.style = ttk.Style()  # Crea un objeto Style para personalizar widgets

        # Configura estilos para diferentes elementos:
        self.style.configure('Titulo.TLabel', font=('Helvetica', 16, 'bold'))  # Estilo para título
        self.style.configure('Boton.TButton', font=('Helvetica', 10), padding=5)  # Estilo para botones normales
        self.style.configure('BotonRojo.TButton', font=('Helvetica', 10), padding=5,
                             foreground='red')  # Estilo para botón rojo

        # Crea fuentes de texto para tareas:
        self.fuente_completada = Font(family='Helvetica', size=10,
                                      overstrike=1)  # Fuente tachada para tareas completadas
        self.fuente_normal = Font(family='Helvetica', size=10)  # Fuente normal para tareas pendientes

    # Método para crear todos los widgets de la interfaz
    def crear_widgets(self):
        # Frame principal que contendrá todos los elementos
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)  # Expande para ocupar todo el espacio

        # Etiqueta del título
        ttk.Label(self.main_frame, text="Lista de Tareas", style='Titulo.TLabel').pack(pady=(0, 10))

        # Frame para la entrada de nuevas tareas
        self.frame_entrada = ttk.Frame(self.main_frame)
        self.frame_entrada.pack(fill=tk.X, pady=(0, 10))

        # Campo de entrada para nuevas tareas
        self.entry_tarea = ttk.Entry(self.frame_entrada, font=self.fuente_normal)
        self.entry_tarea.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        # Botón para añadir tareas
        self.btn_anadir = ttk.Button(self.frame_entrada, text="Añadir", command=self.anadir_tarea,
                                     style='Boton.TButton')
        self.btn_anadir.pack(side=tk.LEFT)

        # Frame para botones superiores (cambiar estado y eliminar)
        self.frame_botones_superiores = ttk.Frame(self.main_frame)
        self.frame_botones_superiores.pack(fill=tk.X, pady=(0, 10))

        # Botón para cambiar estado de tarea (completada/pendiente)
        self.btn_cambiar_estado = ttk.Button(self.frame_botones_superiores, text="Cambiar Estado",
                                             command=self.cambiar_estado_tarea, style='Boton.TButton')
        self.btn_cambiar_estado.pack(side=tk.LEFT, padx=(0, 5))

        # Botón para eliminar tarea seleccionada
        self.btn_eliminar = ttk.Button(self.frame_botones_superiores, text="Eliminar", command=self.eliminar_tarea,
                                       style='Boton.TButton')
        self.btn_eliminar.pack(side=tk.LEFT, padx=(0, 5))

        # Frame para botón inferior (borrar todas)
        self.frame_boton_inferior = ttk.Frame(self.main_frame)
        self.frame_boton_inferior.pack(fill=tk.X, pady=(10, 0))

        # Botón para borrar todas las tareas (con estilo rojo)
        self.btn_borrar_todas = ttk.Button(self.frame_boton_inferior, text="Borrar Todas las Tareas",
                                           command=self.borrar_todas_tareas, style='BotonRojo.TButton')
        self.btn_borrar_todas.pack(fill=tk.X)

        # Treeview (tabla) para mostrar la lista de tareas
        self.tree = ttk.Treeview(self.main_frame, columns=('estado', 'tarea'), show='headings', selectmode='browse')

        # Configura encabezados de columnas
        self.tree.heading('estado', text='Estado', anchor=tk.W)  # Columna estado
        self.tree.heading('tarea', text='Tarea', anchor=tk.W)  # Columna tarea

        # Configura ancho de columnas
        self.tree.column('estado', width=100, stretch=tk.NO)  # Columna estado no se expande
        self.tree.column('tarea', width=400, stretch=tk.YES)  # Columna tarea sí se expande

        # Muestra el treeview en la interfaz
        self.tree.pack(fill=tk.BOTH, expand=True)

    # Método para configurar eventos
    def configurar_eventos(self):
        # Enter en el campo de texto añade tarea
        self.entry_tarea.bind('<Return>', lambda event: self.anadir_tarea())
        # Doble click en una tarea cambia su estado
        self.tree.bind('<Double-1>', lambda event: self.cambiar_estado_tarea())

    # Método para añadir nueva tarea
    def anadir_tarea(self):
        tarea_texto = self.entry_tarea.get().strip()  # Obtiene texto del campo de entrada
        if tarea_texto:  # Si no está vacío
            # Añade diccionario con texto y estado a la lista de tareas
            self.tareas.append({'texto': tarea_texto, 'completada': False})
            self.actualizar_lista_tareas()  # Actualiza la visualización
            self.entry_tarea.delete(0, tk.END)  # Limpia el campo de entrada
        else:
            # Muestra advertencia si el campo está vacío
            messagebox.showwarning("Campo vacío", "Por favor ingresa una tarea")

    # Método para cambiar estado de una tarea (completada/pendiente)
    def cambiar_estado_tarea(self):
        seleccion = self.tree.selection()  # Obtiene la selección actual
        if not seleccion:  # Si no hay nada seleccionado
            messagebox.showwarning("Error", "Por favor, selecciona una tarea primero")
            return

        item = seleccion[0]  # Obtiene el item seleccionado
        index = self.tree.index(item)  # Obtiene su índice
        # Cambia el estado (toggle)
        self.tareas[index]['completada'] = not self.tareas[index]['completada']
        self.actualizar_lista_tareas()  # Actualiza la visualización

    # Método para eliminar una tarea
    def eliminar_tarea(self):
        seleccion = self.tree.selection()  # Obtiene la selección actual
        if not seleccion:  # Si no hay nada seleccionado
            messagebox.showwarning("Error", "Por favor, selecciona una tarea primero")
            return

        item = seleccion[0]  # Obtiene el item seleccionado
        index = self.tree.index(item)  # Obtiene su índice
        # Pide confirmación antes de eliminar
        confirmar = messagebox.askyesno("Confirmar eliminación",
                                        f"¿Eliminar la tarea: '{self.tareas[index]['texto']}'?")

        if confirmar:  # Si confirma
            del self.tareas[index]  # Elimina la tarea
            self.actualizar_lista_tareas()  # Actualiza la visualización

    # Método para borrar todas las tareas
    def borrar_todas_tareas(self):
        if not self.tareas:  # Si no hay tareas
            messagebox.showinfo("Información", "No hay tareas para borrar")
            return

        # Pide confirmación
        confirmar = messagebox.askyesno("Confirmar eliminación total",
                                        "¿Estás seguro de que quieres borrar TODAS las tareas?\nEsta acción no se puede deshacer.",
                                        icon='warning')

        if confirmar:  # Si confirma
            self.tareas.clear()  # Vacía la lista de tareas
            self.actualizar_lista_tareas()  # Actualiza la visualización
            messagebox.showinfo("Éxito", "Todas las tareas han sido eliminadas")  # Mensaje de confirmación

    # Método para actualizar la visualización de la lista de tareas
    def actualizar_lista_tareas(self):
        # Limpia el treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Recorre todas las tareas y las añade al treeview
        for tarea in self.tareas:
            estado = "Completada" if tarea['completada'] else "Pendiente"  # Texto según estado
            tags = ('completada',) if tarea['completada'] else ()  # Tags para aplicar estilo

            # Inserta la tarea en el treeview
            self.tree.insert('', tk.END, values=(estado, tarea['texto']), tags=tags)

        # Configura el estilo para las tareas completadas (texto tachado y gris)
        self.tree.tag_configure('completada', font=self.fuente_completada, foreground='#888888')


# Punto de entrada principal
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = AplicacionTareas(root)  # Crea la instancia de la aplicación
    root.mainloop()  # Inicia el bucle principal de la interfaz