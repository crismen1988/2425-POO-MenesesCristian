# Importar los módulos necesarios de tkinter
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font


# Definir la clase principal de la aplicación
class AplicacionTareas:
    # Método constructor que inicializa la aplicación
    def __init__(self, root):
        # Guardar referencia a la ventana principal
        self.root = root
        # Establecer título de la ventana
        self.root.title("Gestor de Tareas Avanzado")
        # Establecer tamaño inicial de la ventana
        self.root.geometry("700x500")

        # Configurar los estilos visuales
        self.configurar_estilos()
        # Inicializar lista vacía para almacenar tareas
        self.tareas = []
        # Crear los elementos de la interfaz
        self.crear_interfaz()
        # Configurar los eventos y atajos de teclado
        self.configurar_eventos()
        # Poner el foco en el campo de entrada al iniciar
        self.entry_tarea.focus_set()

    # Método para configurar los estilos visuales
    def configurar_estilos(self):
        # Crear objeto Style para personalizar widgets
        self.style = ttk.Style()

        # Configurar estilo base para todos los labels (negrita)
        self.style.configure('TLabel', font=('Helvetica', 10, 'bold'))
        # Configurar estilo especial para el título
        self.style.configure('Titulo.TLabel',
                             font=('Helvetica', 18, 'bold'),
                             foreground='#333333')

        # Configurar estilo para botones normales
        self.style.configure('Boton.TButton',
                             font=('Helvetica', 10, 'bold'),
                             padding=5,
                             relief=tk.RAISED)

        # Configurar estilo especial para el botón de borrar todo (más pequeño)
        self.style.configure('BorrarTodo.TButton',
                             font=('Helvetica', 9, 'bold'),
                             foreground='black',
                             padding=2,
                             relief=tk.RAISED)

        # Configurar estilo para los encabezados del Treeview
        self.style.configure('Treeview.Heading',
                             font=('Helvetica', 10, 'bold'))

        # Crear fuente normal para tareas (negrita)
        self.fuente_normal = Font(family='Helvetica', size=11, weight='bold')
        # Crear fuente para tareas completadas (tachada y negrita)
        self.fuente_completada = Font(family='Helvetica', size=11, overstrike=1, weight='bold')

    # Método para crear todos los elementos de la interfaz
    def crear_interfaz(self):
        # Crear frame principal con padding
        self.main_frame = ttk.Frame(self.root, padding="15")
        # Empacar el frame para que ocupe todo el espacio disponible
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Crear y colocar el título de la aplicación
        ttk.Label(self.main_frame,
                  text="Gestor de Tareas",
                  style='Titulo.TLabel').pack(pady=(0, 15))

        # Frame para el área de entrada de nuevas tareas
        self.frame_entrada = ttk.Frame(self.main_frame)
        self.frame_entrada.pack(fill=tk.X, pady=(0, 10))

        # Crear campo de entrada para nuevas tareas
        self.entry_tarea = ttk.Entry(self.frame_entrada,
                                     font=self.fuente_normal)
        # Colocar el campo de entrada (expandible)
        self.entry_tarea.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8))

        # Botón para añadir tareas
        self.btn_anadir = ttk.Button(self.frame_entrada,
                                     text="Añadir (Enter)",
                                     command=self.anadir_tarea,
                                     style='Boton.TButton')
        # Colocar el botón a la derecha del campo de entrada
        self.btn_anadir.pack(side=tk.LEFT)

        # Frame para los botones de acción secundarios
        self.frame_botones = ttk.Frame(self.main_frame)
        self.frame_botones.pack(fill=tk.X, pady=(0, 10))

        # Botón para cambiar estado de tarea
        self.btn_cambiar_estado = ttk.Button(self.frame_botones,
                                             text="Cambiar Estado (C)",
                                             command=self.cambiar_estado_tarea,
                                             style='Boton.TButton')
        # Colocar botón con margen derecho
        self.btn_cambiar_estado.pack(side=tk.LEFT, padx=(0, 8))

        # Botón para eliminar tareas
        self.btn_eliminar = ttk.Button(self.frame_botones,
                                       text="Eliminar (←)",
                                       command=self.eliminar_tarea,
                                       style='Boton.TButton')
        # Colocar botón junto al anterior
        self.btn_eliminar.pack(side=tk.LEFT)

        # Botón para borrar todas las tareas (estilo compacto)
        self.btn_borrar_todas = ttk.Button(self.main_frame,
                                           text="Borrar Todas",
                                           command=self.borrar_todas_tareas,
                                           style='BorrarTodo.TButton')
        # Colocar botón en la parte inferior
        self.btn_borrar_todas.pack(fill=tk.X, pady=(8, 12), ipady=1)

        # Crear Treeview para mostrar la lista de tareas
        self.tree = ttk.Treeview(self.main_frame,
                                 columns=('estado', 'tarea'),
                                 show='headings',
                                 selectmode='browse',
                                 height=15)

        # Configurar encabezados de columnas
        self.tree.heading('estado', text='Estado', anchor=tk.W)
        self.tree.heading('tarea', text='Tarea', anchor=tk.W)
        # Configurar ancho de columnas
        self.tree.column('estado', width=120, stretch=tk.NO)
        self.tree.column('tarea', width=400, stretch=tk.YES)

        # Configurar estilos para diferentes estados de tareas
        self.tree.tag_configure('pendiente', font=self.fuente_normal)
        self.tree.tag_configure('completada',
                                font=self.fuente_completada,
                                foreground='#666666',
                                background='#f5f5f5')
        self.tree.tag_configure('seleccionada', background='#e3f2fd')

        # Crear barra de desplazamiento vertical
        scrollbar = ttk.Scrollbar(self.main_frame,
                                  orient=tk.VERTICAL,
                                  command=self.tree.yview)
        # Configurar scrollbar en el Treeview
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Colocar Treeview y scrollbar en la interfaz
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Método para configurar eventos y atajos de teclado
    def configurar_eventos(self):
        # Evento al presionar Enter en el campo de entrada
        self.entry_tarea.bind('<Return>', lambda e: self.anadir_tarea())

        # Eventos para cambiar estado con tecla C (mayúscula/minúscula)
        self.tree.bind('<c>', lambda e: self.cambiar_estado_tarea())
        self.tree.bind('<C>', lambda e: self.cambiar_estado_tarea())

        # Evento para eliminar con Backspace
        self.tree.bind('<BackSpace>', lambda e: self.eliminar_tarea())

        # Evento para cerrar aplicación con Escape
        self.root.bind('<Escape>', lambda e: self.root.destroy())

        # Eventos de ratón (doble clic y selección)
        self.tree.bind('<Double-1>', lambda e: self.cambiar_estado_tarea())
        self.tree.bind('<<TreeviewSelect>>', self.resaltar_seleccion)

        # Configurar manejo de foco para atajos
        self.entry_tarea.bind('<FocusIn>', lambda e: self.tree.unbind('<BackSpace>'))
        self.tree.bind('<FocusIn>', lambda e: self.tree.bind('<BackSpace>', lambda e: self.eliminar_tarea()))

    # Método para resaltar la tarea seleccionada
    def resaltar_seleccion(self, event=None):
        # Quitar resaltado de todos los items
        for item in self.tree.get_children():
            current_tags = list(self.tree.item(item, 'tags'))
            if 'seleccionada' in current_tags:
                current_tags.remove('seleccionada')
            self.tree.item(item, tags=current_tags)

        # Aplicar resaltado al item seleccionado
        for item in self.tree.selection():
            current_tags = list(self.tree.item(item, 'tags'))
            current_tags.append('seleccionada')
            self.tree.item(item, tags=current_tags)

    # Método para añadir nueva tarea
    def anadir_tarea(self, event=None):
        # Obtener texto del campo de entrada (sin espacios al inicio/fin)
        tarea_texto = self.entry_tarea.get().strip()

        # Verificar que no esté vacío
        if tarea_texto:
            # Añadir nueva tarea a la lista (inicialmente no completada)
            self.tareas.append({
                'texto': tarea_texto,
                'completada': False
            })
            # Actualizar la lista visual
            self.actualizar_lista_tareas()
            # Limpiar campo de entrada
            self.entry_tarea.delete(0, tk.END)
            # Regresar foco al campo de entrada
            self.entry_tarea.focus_set()
        else:
            # Mostrar advertencia si el campo está vacío
            messagebox.showwarning("Campo vacío", "Por favor ingresa una tarea")

    # Método para cambiar estado de una tarea (completada/pendiente)
    def cambiar_estado_tarea(self, event=None):
        # Obtener tarea seleccionada
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Error", "Por favor, selecciona una tarea primero")
            return

        # Obtener item e índice de la tarea seleccionada
        item = seleccion[0]
        index = self.tree.index(item)
        # Cambiar estado (toggle)
        self.tareas[index]['completada'] = not self.tareas[index]['completada']

        # Determinar nuevo estado y etiquetas
        estado = "✅ Completada" if self.tareas[index]['completada'] else "🔄 Pendiente"
        tags = ('completada', 'seleccionada') if self.tareas[index]['completada'] else ('pendiente', 'seleccionada')
        # Actualizar item en el Treeview
        self.tree.item(item, values=(estado, self.tareas[index]['texto']), tags=tags)

    # Método para eliminar una tarea
    def eliminar_tarea(self, event=None):
        # Obtener selección actual
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Error", "Por favor, selecciona una tarea primero")
            return

        # Obtener item e índice de la tarea a eliminar
        item = seleccion[0]
        index = self.tree.index(item)
        tarea_texto = self.tareas[index]['texto']

        # Pedir confirmación antes de eliminar
        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Estás seguro de que deseas eliminar la tarea:\n\"{tarea_texto}\"?",
            icon='warning'
        )

        if confirmar:
            # Guardar posición antes de eliminar
            posicion = index

            # Eliminar tarea de la lista
            del self.tareas[posicion]

            # Actualizar lista visual
            self.actualizar_lista_tareas()

            # Seleccionar automáticamente la siguiente tarea (o última si es necesario)
            if self.tareas:
                nueva_posicion = min(posicion, len(self.tareas) - 1)
                nuevo_item = self.tree.get_children()[nueva_posicion]
                self.tree.selection_set(nuevo_item)
                self.tree.focus(nuevo_item)

    # Método para borrar todas las tareas
    def borrar_todas_tareas(self):
        # Verificar si hay tareas para borrar
        if not self.tareas:
            messagebox.showinfo("Información", "No hay tareas para borrar")
            return

        # Pedir confirmación
        confirmar = messagebox.askyesno(
            "Confirmar eliminación total",
            "¿Estás seguro de que quieres borrar TODAS las tareas?\nEsta acción no se puede deshacer.",
            icon='warning'
        )

        if confirmar:
            # Vaciar lista de tareas
            self.tareas.clear()
            # Actualizar lista visual
            self.actualizar_lista_tareas()
            # Mostrar confirmación
            messagebox.showinfo("Éxito", "Todas las tareas han sido eliminadas")

    # Método para actualizar la lista visual de tareas
    def actualizar_lista_tareas(self):
        # Guardar selección actual (si existe)
        seleccion_actual = self.tree.selection()
        indice_seleccionado = self.tree.index(seleccion_actual[0]) if seleccion_actual else None

        # Limpiar todo el Treeview
        self.tree.delete(*self.tree.get_children())

        # Recorrer todas las tareas y añadirlas al Treeview
        for i, tarea in enumerate(self.tareas):
            # Determinar texto e icono según estado
            estado = "✅ Completada" if tarea['completada'] else "🔄 Pendiente"
            # Determinar etiquetas de estilo
            tags = ('completada',) if tarea['completada'] else ('pendiente',)

            # Mantener selección si corresponde
            if indice_seleccionado is not None and i == indice_seleccionado:
                tags += ('seleccionada',)

            # Insertar tarea en el Treeview
            self.tree.insert('', tk.END, values=(estado, tarea['texto']), tags=tags)

        # Restaurar selección si es posible
        if indice_seleccionado is not None and indice_seleccionado < len(self.tareas):
            nuevo_item = self.tree.get_children()[indice_seleccionado]
            self.tree.selection_set(nuevo_item)
            self.tree.focus(nuevo_item)


# Punto de entrada principal
if __name__ == "__main__":
    # Crear ventana principal
    root = tk.Tk()
    # Crear instancia de la aplicación
    app = AplicacionTareas(root)
    # Iniciar bucle principal de la aplicación
    root.mainloop()