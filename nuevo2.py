# ------------------------------------------------------------------------
#   GESTOR DE PROYECTOS SIMPLE - INTERFAZ PROFESIONAL
#   Asignatura : Lógica de Programación Orientada a Objetos
#   Ciclo      : III/2026 — Universidad de El Salvador
#   Tema       : 7 — Gestor de Proyectos Simple
# ------------------------------------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, Toplevel, Text, Scrollbar
from datetime import datetime

# --------------------------------------------------------------------------
#   ALMACENAMIENTO EN MEMORIA
# --------------------------------------------------------------------------

nom_empleado = []
cargo_empleado = []
nom_proyecto = []
nom_tarea = []
tarea_proyecto = []
tarea_empleado = []
reg_tarea = []
reg_empleado = []
reg_fecha = []
reg_horas = []


# --------------------------------------------------------------------------
#   CLASE PRINCIPAL
# --------------------------------------------------------------------------

class GestorProyectosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Manager Pro")
        self.root.geometry("1280x720")
        self.root.configure(bg="#f5f7fa")
        self.root.minsize(1024, 600)

        # Configurar estilos
        self.setup_styles()

        # Crear interfaz
        self.create_menu_bar()
        self.create_toolbar()
        self.create_main_content()
        self.create_status_bar()

        # Actualizar datos
        self.refresh_all_tables()

    def setup_styles(self):
        """Configurar estilos profesionales"""
        # Paleta de colores corporativa
        self.colors = {
            "primary": "#2c3e50",  # Azul oscuro ejecutivo
            "secondary": "#34495e",  # Azul grisáceo
            "accent": "#3498db",  # Azul brillante (acento)
            "success": "#27ae60",  # Verde éxito
            "danger": "#e74c3c",  # Rojo peligro
            "warning": "#f39c12",  # Naranja advertencia
            "light": "#ecf0f1",  # Gris claro
            "white": "#ffffff",  # Blanco
            "dark": "#2c3e50",  # Oscuro
            "border": "#bdc3c7",  # Borde gris
        }

        # Configurar estilo ttk
        style = ttk.Style()
        style.theme_use('clam')

        # Treeview
        style.configure("Treeview",
                        font=("Segoe UI", 9),
                        rowheight=28,
                        background=self.colors["white"],
                        fieldbackground=self.colors["white"])

        style.configure("Treeview.Heading",
                        font=("Segoe UI", 9, "bold"),
                        background=self.colors["primary"],
                        foreground="white",
                        padding=5)

        # Botones
        style.configure("Accent.TButton",
                        font=("Segoe UI", 9),
                        padding=6,
                        background=self.colors["accent"],
                        foreground="white")

        style.map("Accent.TButton",
                  background=[('active', '#2980b9')])

    def create_menu_bar(self):
        """Crear barra de menú profesional"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Menú Archivo
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Exportar Reporte", command=self.exportar_reporte)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.quit)

        # Menú Registros
        reg_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Registros", menu=reg_menu)
        reg_menu.add_command(label="Nuevo Empleado", command=self.registrar_empleado)
        reg_menu.add_command(label="Nuevo Proyecto", command=self.registrar_proyecto)
        reg_menu.add_command(label="Nueva Tarea", command=self.registrar_tarea)
        reg_menu.add_command(label="Registrar Horas", command=self.registrar_horas)

        # Menú Consultas
        query_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Consultas", menu=query_menu)
        query_menu.add_command(label="Horas por Tarea", command=self.ver_horas_tarea)
        query_menu.add_command(label="Horas por Proyecto", command=self.ver_horas_proyecto)
        query_menu.add_command(label="Horas por Empleado", command=self.ver_horas_empleado)

        # Menú Ayuda
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        help_menu.add_command(label="Acerca de", command=self.acerca_de)

    def create_toolbar(self):
        """Crear barra de herramientas"""
        toolbar = tk.Frame(self.root, bg=self.colors["white"], height=50, relief=tk.RAISED, bd=1)
        toolbar.pack(fill=tk.X, pady=(0, 1))
        toolbar.pack_propagate(False)

        # Logo / Título
        title_label = tk.Label(toolbar,
                               text="PROJECT MANAGER PRO",
                               font=("Segoe UI", 14, "bold"),
                               bg=self.colors["white"],
                               fg=self.colors["primary"])
        title_label.pack(side=tk.LEFT, padx=20)

        # Separador
        tk.Frame(toolbar, width=1, bg=self.colors["border"]).pack(side=tk.LEFT, fill=tk.Y, padx=10)

        # Botones rápidos
        quick_buttons = [
            ("👤", "Nuevo Empleado", self.registrar_empleado),
            ("📁", "Nuevo Proyecto", self.registrar_proyecto),
            ("✓", "Nueva Tarea", self.registrar_tarea),
            ("⏱", "Registrar Horas", self.registrar_horas),
        ]

        for icon, tooltip, command in quick_buttons:
            btn = tk.Button(toolbar,
                            text=icon,
                            font=("Segoe UI", 12),
                            bg=self.colors["white"],
                            fg=self.colors["primary"],
                            relief=tk.FLAT,
                            cursor="hand2",
                            width=3,
                            command=command)
            btn.pack(side=tk.LEFT, padx=2)

            # Tooltip
            self.create_tooltip(btn, tooltip)

    def create_tooltip(self, widget, text):
        """Crear tooltip simple"""

        def show_tooltip(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
            label = tk.Label(tooltip, text=text, background="#ffffe0", relief=tk.SOLID, borderwidth=1)
            label.pack()
            widget.tooltip = tooltip

        def hide_tooltip(event):
            if hasattr(widget, 'tooltip'):
                widget.tooltip.destroy()

        widget.bind('<Enter>', show_tooltip)
        widget.bind('<Leave>', hide_tooltip)

    def create_main_content(self):
        """Crear contenido principal"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.colors["light"])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Panel izquierdo (estadísticas)
        self.create_stats_panel(main_frame)

        # Panel derecho (tabs)
        self.create_tabs_panel(main_frame)

    def create_stats_panel(self, parent):
        """Crear panel de estadísticas"""
        stats_frame = tk.Frame(parent, bg=self.colors["white"], relief=tk.RAISED, bd=1)
        stats_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        # Título
        tk.Label(stats_frame,
                 text="RESUMEN",
                 font=("Segoe UI", 10, "bold"),
                 bg=self.colors["primary"],
                 fg="white",
                 padx=20,
                 pady=8).pack(fill=tk.X)

        # Cards de estadísticas
        self.stats_cards = {}
        stats = [
            ("👥 Empleados", "emp_count", "#3498db"),
            ("📁 Proyectos", "proy_count", "#27ae60"),
            ("✓ Tareas", "task_count", "#e67e22"),
            ("⏱ Horas", "hours_total", "#9b59b6"),
        ]

        for title, key, color in stats:
            card = tk.Frame(stats_frame, bg=self.colors["white"], pady=10)
            card.pack(fill=tk.X, padx=15, pady=10)

            tk.Label(card,
                     text=title,
                     font=("Segoe UI", 9),
                     bg=self.colors["white"],
                     fg="#7f8c8d").pack()

            value_label = tk.Label(card,
                                   text="0",
                                   font=("Segoe UI", 20, "bold"),
                                   bg=self.colors["white"],
                                   fg=color)
            value_label.pack()

            self.stats_cards[key] = value_label

        # Actualizar estadísticas
        self.update_stats()

    def update_stats(self):
        """Actualizar estadísticas"""
        self.stats_cards["emp_count"].config(text=str(len(nom_empleado)))
        self.stats_cards["proy_count"].config(text=str(len(nom_proyecto)))
        self.stats_cards["task_count"].config(text=str(len(nom_tarea)))
        total_horas = sum(reg_horas) if reg_horas else 0
        self.stats_cards["hours_total"].config(text=f"{total_horas:.1f}")

        # Actualizar cada 2 segundos
        self.root.after(2000, self.update_stats)

    def create_tabs_panel(self, parent):
        """Crear panel de pestañas"""
        tabs_frame = tk.Frame(parent, bg=self.colors["light"])
        tabs_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.notebook = ttk.Notebook(tabs_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Crear pestañas
        self.empleados_frame = self.create_table_tab("Empleados",
                                                     ["ID", "Nombre", "Cargo"],
                                                     self.get_empleados_data)
        self.notebook.add(self.empleados_frame, text="👥 Empleados")

        self.proyectos_frame = self.create_table_tab("Proyectos",
                                                     ["ID", "Nombre", "Tareas"],
                                                     self.get_proyectos_data)
        self.notebook.add(self.proyectos_frame, text="📁 Proyectos")

        self.tareas_frame = self.create_table_tab("Tareas",
                                                  ["ID", "Nombre", "Proyecto", "Empleado", "Horas"],
                                                  self.get_tareas_data)
        self.notebook.add(self.tareas_frame, text="✓ Tareas")

        self.horas_frame = self.create_table_tab("Registro Horas",
                                                 ["Tarea", "Empleado", "Fecha", "Horas"],
                                                 self.get_horas_data)
        self.notebook.add(self.horas_frame, text="⏱ Registro Horas")

    def create_table_tab(self, title, columns, data_func):
        """Crear una pestaña con tabla"""
        frame = tk.Frame(self.notebook, bg=self.colors["light"])

        # Frame para tabla y scroll
        table_frame = tk.Frame(frame, bg=self.colors["light"])
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Scrollbars
        scroll_y = Scrollbar(table_frame, orient=tk.VERTICAL)
        scroll_x = Scrollbar(table_frame, orient=tk.HORIZONTAL)

        # Treeview
        tree = ttk.Treeview(table_frame, columns=columns, show='headings',
                            yscrollcommand=scroll_y.set,
                            xscrollcommand=scroll_x.set)

        scroll_y.config(command=tree.yview)
        scroll_x.config(command=tree.xview)

        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        tree.pack(fill=tk.BOTH, expand=True)

        # Configurar columnas
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor='center')

        # Botón refrescar
        refresh_btn = tk.Button(frame,
                                text="Refrescar",
                                command=lambda: self.refresh_table(tree, data_func),
                                bg=self.colors["accent"],
                                fg="white",
                                font=("Segoe UI", 9),
                                padx=15,
                                pady=5,
                                relief=tk.FLAT,
                                cursor="hand2")
        refresh_btn.pack(pady=5)

        frame.tree = tree
        frame.data_func = data_func

        return frame

    def refresh_table(self, tree, data_func):
        """Refrescar tabla"""
        for item in tree.get_children():
            tree.delete(item)
        for row in data_func():
            tree.insert('', 'end', values=row)

    def refresh_all_tables(self):
        """Refrescar todas las tablas"""
        for tab in [self.empleados_frame, self.proyectos_frame,
                    self.tareas_frame, self.horas_frame]:
            if hasattr(tab, 'tree') and hasattr(tab, 'data_func'):
                self.refresh_table(tab.tree, tab.data_func)

    # ----------------------------------------------------------------------
    # DATOS PARA TABLAS
    # ----------------------------------------------------------------------

    def get_empleados_data(self):
        return [(i + 1, nombre, cargo) for i, (nombre, cargo) in enumerate(zip(nom_empleado, cargo_empleado))]

    def get_proyectos_data(self):
        return [(i + 1, nombre, sum(1 for x in tarea_proyecto if x == i)) for i, nombre in enumerate(nom_proyecto)]

    def get_tareas_data(self):
        data = []
        for i in range(len(nom_tarea)):
            total_h = sum(reg_horas[j] for j in range(len(reg_horas)) if reg_tarea[j] == i)
            proyecto = nom_proyecto[tarea_proyecto[i]] if tarea_proyecto[i] < len(nom_proyecto) else "N/A"
            empleado = nom_empleado[tarea_empleado[i]] if tarea_empleado[i] < len(nom_empleado) else "N/A"
            data.append((i + 1, nom_tarea[i], proyecto, empleado, f"{total_h:.1f}h"))
        return data

    def get_horas_data(self):
        data = []
        for i in range(len(reg_horas)):
            tarea = nom_tarea[reg_tarea[i]] if reg_tarea[i] < len(nom_tarea) else "N/A"
            empleado = nom_empleado[reg_empleado[i]] if reg_empleado[i] < len(nom_empleado) else "N/A"
            data.append((tarea, empleado, reg_fecha[i], f"{reg_horas[i]:.1f}h"))
        return data

    def create_status_bar(self):
        """Crear barra de estado minimalista"""
        status_frame = tk.Frame(self.root, bg=self.colors["primary"], height=28)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)

        self.status_label = tk.Label(status_frame,
                                     text="Ready",
                                     bg=self.colors["primary"],
                                     fg=self.colors["light"],
                                     font=("Segoe UI", 8),
                                     anchor=tk.W)
        self.status_label.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

        # Versión
        version_label = tk.Label(status_frame,
                                 text="v2.0",
                                 bg=self.colors["primary"],
                                 fg=self.colors["light"],
                                 font=("Segoe UI", 8))
        version_label.pack(side=tk.RIGHT, padx=10)

    # ----------------------------------------------------------------------
    # FUNCIONALIDADES
    # ----------------------------------------------------------------------

    def registrar_empleado(self):
        dialog = Toplevel(self.root)
        dialog.title("Nuevo Empleado")
        dialog.geometry("400x250")
        dialog.configure(bg=self.colors["white"])
        dialog.transient(self.root)
        dialog.grab_set()

        tk.Label(dialog, text="Registrar Empleado",
                 font=("Segoe UI", 12, "bold"),
                 bg=self.colors["white"],
                 fg=self.colors["primary"]).pack(pady=15)

        tk.Label(dialog, text="Nombre completo:", bg=self.colors["white"]).pack(pady=5)
        nombre_entry = tk.Entry(dialog, font=("Segoe UI", 11), width=30)
        nombre_entry.pack(pady=5)

        tk.Label(dialog, text="Cargo / Puesto:", bg=self.colors["white"]).pack(pady=5)
        cargo_entry = tk.Entry(dialog, font=("Segoe UI", 11), width=30)
        cargo_entry.pack(pady=5)

        def guardar():
            nombre = nombre_entry.get().strip()
            cargo = cargo_entry.get().strip()
            if nombre and cargo:
                nom_empleado.append(nombre)
                cargo_empleado.append(cargo)
                self.refresh_all_tables()
                self.status_label.config(text=f"Empleado registrado: {nombre}")
                messagebox.showinfo("Éxito", f"Empleado '{nombre}' registrado")
                dialog.destroy()
            else:
                messagebox.showwarning("Error", "Complete todos los campos")

        tk.Button(dialog, text="Registrar", command=guardar,
                  bg=self.colors["success"], fg="white",
                  font=("Segoe UI", 10), padx=20, pady=5,
                  relief=tk.FLAT, cursor="hand2").pack(pady=20)

    def registrar_proyecto(self):
        nombre = simpledialog.askstring("Nuevo Proyecto", "Nombre del proyecto:")
        if nombre:
            nom_proyecto.append(nombre)
            self.refresh_all_tables()
            self.status_label.config(text=f"Proyecto registrado: {nombre}")
            messagebox.showinfo("Éxito", f"Proyecto '{nombre}' registrado")

    def registrar_tarea(self):
        if not nom_proyecto:
            messagebox.showwarning("Error", "No hay proyectos registrados")
            return
        if not nom_empleado:
            messagebox.showwarning("Error", "No hay empleados registrados")
            return

        dialog = Toplevel(self.root)
        dialog.title("Nueva Tarea")
        dialog.geometry("400x350")
        dialog.configure(bg=self.colors["white"])
        dialog.transient(self.root)
        dialog.grab_set()

        tk.Label(dialog, text="Registrar Tarea",
                 font=("Segoe UI", 12, "bold"),
                 bg=self.colors["white"],
                 fg=self.colors["primary"]).pack(pady=15)

        tk.Label(dialog, text="Nombre de la tarea:", bg=self.colors["white"]).pack(pady=5)
        nombre_entry = tk.Entry(dialog, font=("Segoe UI", 11), width=30)
        nombre_entry.pack(pady=5)

        tk.Label(dialog, text="Proyecto:", bg=self.colors["white"]).pack(pady=5)
        proyecto_var = tk.StringVar()
        proyecto_combo = ttk.Combobox(dialog, textvariable=proyecto_var,
                                      values=nom_proyecto, width=27)
        proyecto_combo.pack(pady=5)

        tk.Label(dialog, text="Empleado asignado:", bg=self.colors["white"]).pack(pady=5)
        empleado_var = tk.StringVar()
        empleado_combo = ttk.Combobox(dialog, textvariable=empleado_var,
                                      values=nom_empleado, width=27)
        empleado_combo.pack(pady=5)

        def guardar():
            nombre = nombre_entry.get().strip()
            proyecto = proyecto_var.get()
            empleado = empleado_var.get()

            if not nombre or not proyecto or not empleado:
                messagebox.showwarning("Error", "Complete todos los campos")
                return

            id_proy = nom_proyecto.index(proyecto)
            id_emp = nom_empleado.index(empleado)

            nom_tarea.append(nombre)
            tarea_proyecto.append(id_proy)
            tarea_empleado.append(id_emp)

            self.refresh_all_tables()
            self.status_label.config(text=f"Tarea registrada: {nombre}")
            messagebox.showinfo("Éxito", f"Tarea '{nombre}' registrada")
            dialog.destroy()

        tk.Button(dialog, text="Registrar", command=guardar,
                  bg=self.colors["success"], fg="white",
                  font=("Segoe UI", 10), padx=20, pady=5,
                  relief=tk.FLAT, cursor="hand2").pack(pady=20)

    def registrar_horas(self):
        if not nom_tarea:
            messagebox.showwarning("Error", "No hay tareas registradas")
            return

        dialog = Toplevel(self.root)
        dialog.title("Registrar Horas")
        dialog.geometry("400x350")
        dialog.configure(bg=self.colors["white"])
        dialog.transient(self.root)
        dialog.grab_set()

        tk.Label(dialog, text="Registrar Horas Trabajadas",
                 font=("Segoe UI", 12, "bold"),
                 bg=self.colors["white"],
                 fg=self.colors["primary"]).pack(pady=15)

        tk.Label(dialog, text="Tarea:", bg=self.colors["white"]).pack(pady=5)
        tarea_var = tk.StringVar()
        tarea_combo = ttk.Combobox(dialog, textvariable=tarea_var,
                                   values=nom_tarea, width=27)
        tarea_combo.pack(pady=5)

        tk.Label(dialog, text="Fecha (DD/MM/AAAA):", bg=self.colors["white"]).pack(pady=5)
        fecha_entry = tk.Entry(dialog, font=("Segoe UI", 11), width=30)
        fecha_entry.insert(0, datetime.now().strftime("%d/%m/%Y"))
        fecha_entry.pack(pady=5)

        tk.Label(dialog, text="Horas:", bg=self.colors["white"]).pack(pady=5)
        horas_entry = tk.Entry(dialog, font=("Segoe UI", 11), width=30)
        horas_entry.pack(pady=5)

        def guardar():
            try:
                tarea = tarea_var.get()
                fecha = fecha_entry.get().strip()
                horas = float(horas_entry.get())

                if not tarea or not fecha or horas <= 0:
                    messagebox.showwarning("Error", "Complete todos los campos correctamente")
                    return

                if horas > 24:
                    messagebox.showwarning("Error", "No se pueden registrar más de 24 horas")
                    return

                id_tarea = nom_tarea.index(tarea)
                id_emp = tarea_empleado[id_tarea]

                # Validar total día
                acum_dia = sum(reg_horas[i] for i in range(len(reg_horas))
                               if reg_empleado[i] == id_emp and reg_fecha[i] == fecha)

                if acum_dia + horas > 24:
                    restante = 24 - acum_dia
                    messagebox.showwarning("Error", f"Límite diario: solo puede registrar {restante:.1f}h más")
                    return

                reg_tarea.append(id_tarea)
                reg_empleado.append(id_emp)
                reg_fecha.append(fecha)
                reg_horas.append(horas)

                self.refresh_all_tables()
                self.status_label.config(text=f"Horas registradas: {horas}h en {tarea}")
                messagebox.showinfo("Éxito", f"{horas:.1f} horas registradas")
                dialog.destroy()

            except ValueError:
                messagebox.showwarning("Error", "Las horas deben ser un número válido")

        tk.Button(dialog, text="Registrar", command=guardar,
                  bg=self.colors["success"], fg="white",
                  font=("Segoe UI", 10), padx=20, pady=5,
                  relief=tk.FLAT, cursor="hand2").pack(pady=20)

    def ver_horas_tarea(self):
        if not nom_tarea:
            messagebox.showinfo("Información", "No hay tareas registradas")
            return

        resultado = "HORAS POR TAREA\n\n"
        for i in range(len(nom_tarea)):
            total_h = sum(reg_horas[j] for j in range(len(reg_horas)) if reg_tarea[j] == i)
            proyecto = nom_proyecto[tarea_proyecto[i]] if tarea_proyecto[i] < len(nom_proyecto) else "N/A"
            empleado = nom_empleado[tarea_empleado[i]] if tarea_empleado[i] < len(nom_empleado) else "N/A"
            resultado += f"{i + 1}. {nom_tarea[i]}\n"
            resultado += f"   Proyecto: {proyecto} | Empleado: {empleado}\n"
            resultado += f"   Horas: {total_h:.1f}h\n\n"

        self.show_info_window("Horas por Tarea", resultado)

    def ver_horas_proyecto(self):
        if not nom_proyecto:
            messagebox.showinfo("Información", "No hay proyectos registrados")
            return

        resultado = "HORAS POR PROYECTO\n\n"
        gran_total = 0
        for i in range(len(nom_proyecto)):
            total_h = sum(reg_horas[j] for j in range(len(reg_horas))
                          if tarea_proyecto[reg_tarea[j]] == i)
            gran_total += total_h
            resultado += f"{i + 1}. {nom_proyecto[i]}: {total_h:.1f}h\n"

        resultado += f"\n{'=' * 30}\n"
        resultado += f"TOTAL: {gran_total:.1f}h"

        self.show_info_window("Horas por Proyecto", resultado)

    def ver_horas_empleado(self):
        if not nom_empleado:
            messagebox.showinfo("Información", "No hay empleados registrados")
            return

        resultado = "HORAS POR EMPLEADO\n\n"
        for i in range(len(nom_empleado)):
            total_h = sum(reg_horas[j] for j in range(len(reg_horas)) if reg_empleado[j] == i)
            resultado += f"{i + 1}. {nom_empleado[i]} ({cargo_empleado[i]}): {total_h:.1f}h\n"

        self.show_info_window("Horas por Empleado", resultado)

    def exportar_reporte(self):
        """Exportar reporte simple"""
        if not nom_proyecto and not nom_empleado:
            messagebox.showwarning("Error", "No hay datos para exportar")
            return

        reporte = "=== REPORTE DE PROYECTOS ===\n\n"
        reporte += f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"

        reporte += "PROYECTOS:\n"
        for i, p in enumerate(nom_proyecto):
            total_h = sum(reg_horas[j] for j in range(len(reg_horas))
                          if tarea_proyecto[reg_tarea[j]] == i)
            reporte += f"  - {p}: {total_h:.1f}h\n"

        reporte += "\nEMPLEADOS:\n"
        for i, e in enumerate(nom_empleado):
            total_h = sum(reg_horas[j] for j in range(len(reg_horas)) if reg_empleado[j] == i)
            reporte += f"  - {e}: {total_h:.1f}h\n"

        self.show_info_window("Reporte Exportado", reporte)

    def acerca_de(self):
        acerca = "Project Manager Pro\n\n"
        acerca += "Gestor de Proyectos Simple\n"
        acerca += "Universidad de El Salvador\n"
        acerca += "Ciclo III/2026\n\n"
        acerca += "Lógica de Programación Orientada a Objetos"

        messagebox.showinfo("Acerca de", acerca)

    def show_info_window(self, title, content):
        dialog = Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("500x400")
        dialog.configure(bg=self.colors["white"])
        dialog.transient(self.root)

        text_area = Text(dialog, wrap=tk.WORD, font=("Consolas", 10),
                         bg=self.colors["light"], fg=self.colors["dark"])
        text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        scrollbar = Scrollbar(text_area)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_area.yview)

        text_area.insert(tk.END, content)
        text_area.config(state=tk.DISABLED)

        tk.Button(dialog, text="Cerrar", command=dialog.destroy,
                  bg=self.colors["accent"], fg="white",
                  font=("Segoe UI", 9), padx=20, pady=5,
                  relief=tk.FLAT, cursor="hand2").pack(pady=10)


# --------------------------------------------------------------------------
#   EJECUCIÓN
# --------------------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = GestorProyectosApp(root)
    root.mainloop()