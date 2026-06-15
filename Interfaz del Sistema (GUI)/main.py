# ------------------------------------------------------------------------
#   GESTOR DE PROYECTOS SIMPLE - INTERFAZ PROFESIONAL
#   Asignatura : Logica de Programacion Orientada a Objetos
#   Ciclo      : I/2026 - Universidad de El Salvador
#   Tema       : 7 - Gestor de Proyectos Simple
#   Integrantes: Jose Amilcar Mira Vasquez
#                Kenia Yamileth Murillo Gutierrez
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
#   FUNCION DE VALIDACION DE FECHAS (NECESARIA PARA PRUEBAS)
# --------------------------------------------------------------------------

def validar_fecha(fecha):
    """Valida formato DD/MM/AAAA y fecha real (años bisiestos incluidos)"""
    if not fecha or len(fecha) != 10:
        return False
    if fecha[2] != '/' or fecha[5] != '/':
        return False
    try:
        dia, mes, anio = map(int, fecha.split('/'))
    except:
        return False

    if mes < 1 or mes > 12 or dia < 1 or anio < 2000 or anio > 2100:
        return False

    # Determinar si es bisiesto
    es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

    # Dias por mes
    if mes == 2:
        return dia <= (29 if es_bisiesto else 28)
    elif mes in [4, 6, 9, 11]:
        return dia <= 30
    else:
        return dia <= 31


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

        self.setup_styles()
        self.create_menu_bar()
        self.create_toolbar()
        self.create_main_content()
        self.create_status_bar()
        self.refresh_all_tables()

    def setup_styles(self):
        self.colors = {
            "primary": "#2c3e50", "secondary": "#34495e", "accent": "#3498db",
            "success": "#27ae60", "danger": "#e74c3c", "warning": "#f39c12",
            "light": "#ecf0f1", "white": "#ffffff", "dark": "#2c3e50", "border": "#bdc3c7",
        }
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=("Segoe UI", 9), rowheight=28,
                        background=self.colors["white"], fieldbackground=self.colors["white"])
        style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"),
                        background=self.colors["primary"], foreground="white", padding=5)

    def create_menu_bar(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Exportar Reporte", command=self.exportar_reporte)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.quit)

        reg_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Registros", menu=reg_menu)
        reg_menu.add_command(label="Nuevo Empleado", command=self.registrar_empleado)
        reg_menu.add_command(label="Nuevo Proyecto", command=self.registrar_proyecto)
        reg_menu.add_command(label="Nueva Tarea", command=self.registrar_tarea)
        reg_menu.add_command(label="Registrar Horas", command=self.registrar_horas)

        query_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Consultas", menu=query_menu)
        query_menu.add_command(label="Horas por Tarea", command=self.ver_horas_tarea)
        query_menu.add_command(label="Horas por Proyecto", command=self.ver_horas_proyecto)
        query_menu.add_command(label="Horas por Empleado", command=self.ver_horas_empleado)

        crud_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="CRUD", menu=crud_menu)
        crud_menu.add_command(label="Actualizar Empleado", command=self.actualizar_empleado)
        crud_menu.add_command(label="Actualizar Proyecto", command=self.actualizar_proyecto)
        crud_menu.add_separator()
        crud_menu.add_command(label="Eliminar Tarea", command=self.eliminar_tarea)
        crud_menu.add_command(label="Eliminar Empleado", command=self.eliminar_empleado)
        crud_menu.add_command(label="Eliminar Proyecto", command=self.eliminar_proyecto)
        crud_menu.add_separator()
        crud_menu.add_command(label="Buscar Empleado", command=self.buscar_empleado)
        crud_menu.add_command(label="Buscar Proyecto", command=self.buscar_proyecto)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        help_menu.add_command(label="Acerca de", command=self.acerca_de)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bg=self.colors["white"], height=50, relief=tk.RAISED, bd=1)
        toolbar.pack(fill=tk.X, pady=(0, 1))
        toolbar.pack_propagate(False)

        tk.Label(toolbar, text="Gestor de Proyectos Simple", font=("Segoe UI", 14, "bold"),
                 bg=self.colors["white"], fg=self.colors["primary"]).pack(side=tk.LEFT, padx=20)

        tk.Frame(toolbar, width=1, bg=self.colors["border"]).pack(side=tk.LEFT, fill=tk.Y, padx=10)

        for icon, tip, cmd in [("👤", "Nuevo Empleado", self.registrar_empleado),
                               ("📁", "Nuevo Proyecto", self.registrar_proyecto),
                               ("✓", "Nueva Tarea", self.registrar_tarea),
                               ("⏱", "Registrar Horas", self.registrar_horas)]:
            tk.Button(toolbar, text=icon, font=("Segoe UI", 12), bg=self.colors["white"],
                      fg=self.colors["primary"], relief=tk.FLAT, cursor="hand2", width=3,
                      command=cmd).pack(side=tk.LEFT, padx=2)

    def create_main_content(self):
        main_frame = tk.Frame(self.root, bg=self.colors["light"])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.create_stats_panel(main_frame)
        self.create_tabs_panel(main_frame)

    def create_stats_panel(self, parent):
        stats_frame = tk.Frame(parent, bg=self.colors["white"], relief=tk.RAISED, bd=1)
        stats_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        tk.Label(stats_frame, text="RESUMEN", font=("Segoe UI", 10, "bold"),
                 bg=self.colors["primary"], fg="white", padx=20, pady=8).pack(fill=tk.X)

        self.stats_cards = {}
        for title, key, color in [("👥 Empleados", "emp", "#3498db"), ("📁 Proyectos", "proy", "#27ae60"),
                                  ("✓ Tareas", "task", "#e67e22"), ("⏱ Horas", "hours", "#9b59b6")]:
            card = tk.Frame(stats_frame, bg=self.colors["white"], pady=10)
            card.pack(fill=tk.X, padx=15, pady=5)
            tk.Label(card, text=title, font=("Segoe UI", 9), bg=self.colors["white"], fg="#7f8c8d").pack()
            self.stats_cards[key] = tk.Label(card, text="0", font=("Segoe UI", 20, "bold"), bg=self.colors["white"],
                                             fg=color)
            self.stats_cards[key].pack()

        self.update_stats()

    def update_stats(self):
        self.stats_cards["emp"].config(text=str(len(nom_empleado)))
        self.stats_cards["proy"].config(text=str(len(nom_proyecto)))
        self.stats_cards["task"].config(text=str(len(nom_tarea)))
        self.stats_cards["hours"].config(text=f"{sum(reg_horas):.1f}" if reg_horas else "0.0")
        self.root.after(2000, self.update_stats)

    def create_tabs_panel(self, parent):
        tabs_frame = tk.Frame(parent, bg=self.colors["light"])
        tabs_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.notebook = ttk.Notebook(tabs_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.empleados_frame = self.create_table_tab(["ID", "Nombre", "Cargo"], self.get_empleados_data, "👥 Empleados")
        self.proyectos_frame = self.create_table_tab(["ID", "Nombre", "Tareas"], self.get_proyectos_data, "📁 Proyectos")
        self.tareas_frame = self.create_table_tab(["ID", "Nombre", "Proyecto", "Empleado", "Horas"],
                                                  self.get_tareas_data, "✓ Tareas")
        self.horas_frame = self.create_table_tab(["Tarea", "Empleado", "Fecha", "Horas"], self.get_horas_data,
                                                 "⏱ Registro Horas")

    def create_table_tab(self, columns, data_func, text):
        frame = tk.Frame(self.notebook, bg=self.colors["light"])
        self.notebook.add(frame, text=text)

        table_frame = tk.Frame(frame, bg=self.colors["light"])
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        scroll_y, scroll_x = Scrollbar(table_frame, orient=tk.VERTICAL), Scrollbar(table_frame, orient=tk.HORIZONTAL)
        tree = ttk.Treeview(table_frame, columns=columns, show='headings',
                            yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=tree.yview)
        scroll_x.config(command=tree.xview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        tree.pack(fill=tk.BOTH, expand=True)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor='center')

        tk.Button(frame, text="Refrescar", command=lambda: self.refresh_table(tree, data_func),
                  bg=self.colors["accent"], fg="white", font=("Segoe UI", 9), padx=15, pady=5,
                  relief=tk.FLAT, cursor="hand2").pack(pady=5)

        frame.tree, frame.data_func = tree, data_func
        return frame

    def refresh_table(self, tree, data_func):
        for item in tree.get_children():
            tree.delete(item)
        for row in data_func():
            tree.insert('', 'end', values=row)

    def refresh_all_tables(self):
        for tab in [self.empleados_frame, self.proyectos_frame, self.tareas_frame, self.horas_frame]:
            if hasattr(tab, 'tree') and hasattr(tab, 'data_func'):
                self.refresh_table(tab.tree, tab.data_func)

    def get_empleados_data(self):
        return [(i + 1, n, c) for i, (n, c) in enumerate(zip(nom_empleado, cargo_empleado))]

    def get_proyectos_data(self):
        return [(i + 1, n, sum(1 for x in tarea_proyecto if x == i)) for i, n in enumerate(nom_proyecto)]

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
        status_frame = tk.Frame(self.root, bg=self.colors["primary"], height=28)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)
        self.status_label = tk.Label(status_frame, text="Ready", bg=self.colors["primary"],
                                     fg=self.colors["light"], font=("Segoe UI", 8), anchor=tk.W)
        self.status_label.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        tk.Label(status_frame, text="v3.0", bg=self.colors["primary"], fg=self.colors["light"],
                 font=("Segoe UI", 8)).pack(side=tk.RIGHT, padx=10)

    # ----------------------------------------------------------------------
    # FUNCIONALIDADES PRINCIPALES
    # ----------------------------------------------------------------------

    def registrar_empleado(self):
        dialog = Toplevel(self.root)
        dialog.title("Nuevo Empleado")
        dialog.geometry("400x250")
        dialog.configure(bg=self.colors["white"])
        dialog.transient(self.root)
        dialog.grab_set()

        tk.Label(dialog, text="Registrar Empleado", font=("Segoe UI", 12, "bold"),
                 bg=self.colors["white"], fg=self.colors["primary"]).pack(pady=15)
        tk.Label(dialog, text="Nombre:", bg=self.colors["white"]).pack(pady=5)
        nombre_entry = tk.Entry(dialog, font=("Segoe UI", 11), width=30)
        nombre_entry.pack(pady=5)
        tk.Label(dialog, text="Cargo:", bg=self.colors["white"]).pack(pady=5)
        cargo_entry = tk.Entry(dialog, font=("Segoe UI", 11), width=30)
        cargo_entry.pack(pady=5)

        def guardar():
            n, c = nombre_entry.get().strip(), cargo_entry.get().strip()
            if n and c:
                nom_empleado.append(n)
                cargo_empleado.append(c)
                self.refresh_all_tables()
                self.status_label.config(text=f"Empleado registrado: {n}")
                messagebox.showinfo("Exito", f"Empleado '{n}' registrado")
                dialog.destroy()
            else:
                messagebox.showwarning("Error", "Complete todos los campos")

        tk.Button(dialog, text="Registrar", command=guardar, bg=self.colors["success"],
                  fg="white", font=("Segoe UI", 10), padx=20, pady=5,
                  relief=tk.FLAT, cursor="hand2").pack(pady=20)

    def registrar_proyecto(self):
        nombre = simpledialog.askstring("Nuevo Proyecto", "Nombre del proyecto:")
        if nombre:
            nom_proyecto.append(nombre)
            self.refresh_all_tables()
            self.status_label.config(text=f"Proyecto registrado: {nombre}")
            messagebox.showinfo("Exito", f"Proyecto '{nombre}' registrado")

    def registrar_tarea(self):
        if not nom_proyecto or not nom_empleado:
            messagebox.showwarning("Error", "Faltan proyectos o empleados")
            return

        dialog = Toplevel(self.root)
        dialog.title("Nueva Tarea")
        dialog.geometry("400x350")
        dialog.configure(bg=self.colors["white"])
        dialog.transient(self.root)
        dialog.grab_set()

        tk.Label(dialog, text="Registrar Tarea", font=("Segoe UI", 12, "bold"),
                 bg=self.colors["white"], fg=self.colors["primary"]).pack(pady=15)
        tk.Label(dialog, text="Nombre:", bg=self.colors["white"]).pack(pady=5)
        nombre_entry = tk.Entry(dialog, font=("Segoe UI", 11), width=30)
        nombre_entry.pack(pady=5)
        tk.Label(dialog, text="Proyecto:", bg=self.colors["white"]).pack(pady=5)
        proyecto_var = tk.StringVar()
        ttk.Combobox(dialog, textvariable=proyecto_var, values=nom_proyecto, width=27).pack(pady=5)
        tk.Label(dialog, text="Empleado:", bg=self.colors["white"]).pack(pady=5)
        empleado_var = tk.StringVar()
        ttk.Combobox(dialog, textvariable=empleado_var, values=nom_empleado, width=27).pack(pady=5)

        def guardar():
            n, p, e = nombre_entry.get().strip(), proyecto_var.get(), empleado_var.get()
            if n and p and e:
                nom_tarea.append(n)
                tarea_proyecto.append(nom_proyecto.index(p))
                tarea_empleado.append(nom_empleado.index(e))
                self.refresh_all_tables()
                self.status_label.config(text=f"Tarea registrada: {n}")
                messagebox.showinfo("Exito", f"Tarea '{n}' registrada")
                dialog.destroy()
            else:
                messagebox.showwarning("Error", "Complete todos los campos")

        tk.Button(dialog, text="Registrar", command=guardar, bg=self.colors["success"],
                  fg="white", font=("Segoe UI", 10), padx=20, pady=5,
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

        tk.Label(dialog, text="Registrar Horas", font=("Segoe UI", 12, "bold"),
                 bg=self.colors["white"], fg=self.colors["primary"]).pack(pady=15)
        tk.Label(dialog, text="Tarea:", bg=self.colors["white"]).pack(pady=5)
        tarea_var = tk.StringVar()
        ttk.Combobox(dialog, textvariable=tarea_var, values=nom_tarea, width=27).pack(pady=5)
        tk.Label(dialog, text="Fecha (DD/MM/AAAA):", bg=self.colors["white"]).pack(pady=5)
        fecha_entry = tk.Entry(dialog, font=("Segoe UI", 11), width=30)
        fecha_entry.insert(0, datetime.now().strftime("%d/%m/%Y"))
        fecha_entry.pack(pady=5)
        tk.Label(dialog, text="Horas:", bg=self.colors["white"]).pack(pady=5)
        horas_entry = tk.Entry(dialog, font=("Segoe UI", 11), width=30)
        horas_entry.pack(pady=5)

        def guardar():
            try:
                tarea, fecha, horas = tarea_var.get(), fecha_entry.get().strip(), float(horas_entry.get())
                if not tarea or not fecha or horas <= 0 or horas > 24 or not validar_fecha(fecha):
                    messagebox.showwarning("Error", "Datos invalidos")
                    return
                id_t = nom_tarea.index(tarea)
                id_e = tarea_empleado[id_t]
                acum = sum(
                    reg_horas[i] for i in range(len(reg_horas)) if reg_empleado[i] == id_e and reg_fecha[i] == fecha)
                if acum + horas > 24:
                    messagebox.showwarning("Error", f"Limite diario: solo puede registrar {24 - acum:.1f}h mas")
                    return
                reg_tarea.append(id_t)
                reg_empleado.append(id_e)
                reg_fecha.append(fecha)
                reg_horas.append(horas)
                self.refresh_all_tables()
                self.status_label.config(text=f"Horas registradas: {horas}h")
                messagebox.showinfo("Exito", f"{horas:.1f} horas registradas")
                dialog.destroy()
            except:
                messagebox.showwarning("Error", "Horas debe ser un numero")

        tk.Button(dialog, text="Registrar", command=guardar, bg=self.colors["success"],
                  fg="white", font=("Segoe UI", 10), padx=20, pady=5,
                  relief=tk.FLAT, cursor="hand2").pack(pady=20)

    def actualizar_empleado(self):
        if not nom_empleado:
            messagebox.showwarning("Error", "No hay empleados")
            return
        idx = simpledialog.askinteger("Actualizar", f"ID del empleado (1-{len(nom_empleado)}):", minvalue=1,
                                      maxvalue=len(nom_empleado))
        if idx:
            nuevo = simpledialog.askstring("Actualizar", f"Nuevo nombre para '{nom_empleado[idx - 1]}':")
            if nuevo:
                nom_empleado[idx - 1] = nuevo
                self.refresh_all_tables()
                messagebox.showinfo("Exito", "Empleado actualizado")

    def actualizar_proyecto(self):
        if not nom_proyecto:
            messagebox.showwarning("Error", "No hay proyectos")
            return
        idx = simpledialog.askinteger("Actualizar", f"ID del proyecto (1-{len(nom_proyecto)}):", minvalue=1,
                                      maxvalue=len(nom_proyecto))
        if idx:
            nuevo = simpledialog.askstring("Actualizar", f"Nuevo nombre para '{nom_proyecto[idx - 1]}':")
            if nuevo:
                nom_proyecto[idx - 1] = nuevo
                self.refresh_all_tables()
                messagebox.showinfo("Exito", "Proyecto actualizado")

    def eliminar_tarea(self):
        if not nom_tarea:
            messagebox.showwarning("Error", "No hay tareas")
            return
        idx = simpledialog.askinteger("Eliminar", f"ID de tarea (1-{len(nom_tarea)}):", minvalue=1,
                                      maxvalue=len(nom_tarea))
        if idx and messagebox.askyesno("Confirmar", "¿Eliminar tarea?"):
            idx -= 1
            i = 0
            while i < len(reg_tarea):
                if reg_tarea[i] == idx:
                    for lista in [reg_tarea, reg_empleado, reg_fecha, reg_horas]:
                        lista.pop(i)
                else:
                    if reg_tarea[i] > idx:
                        reg_tarea[i] -= 1
                    i += 1
            nom_tarea.pop(idx)
            tarea_proyecto.pop(idx)
            tarea_empleado.pop(idx)
            self.refresh_all_tables()
            messagebox.showinfo("Exito", "Tarea eliminada")

    def eliminar_empleado(self):
        if not nom_empleado:
            messagebox.showwarning("Error", "No hay empleados")
            return
        idx = simpledialog.askinteger("Eliminar", f"ID de empleado (1-{len(nom_empleado)}):", minvalue=1,
                                      maxvalue=len(nom_empleado))
        if idx and messagebox.askyesno("Confirmar", "¿Eliminar empleado?"):
            idx -= 1
            i = 0
            while i < len(reg_empleado):
                if reg_empleado[i] == idx:
                    for lista in [reg_tarea, reg_empleado, reg_fecha, reg_horas]:
                        lista.pop(i)
                else:
                    if reg_empleado[i] > idx:
                        reg_empleado[i] -= 1
                    i += 1
            for i in range(len(tarea_empleado)):
                if tarea_empleado[i] > idx:
                    tarea_empleado[i] -= 1
            nom_empleado.pop(idx)
            cargo_empleado.pop(idx)
            self.refresh_all_tables()
            messagebox.showinfo("Exito", "Empleado eliminado")

    def eliminar_proyecto(self):
        if not nom_proyecto:
            messagebox.showwarning("Error", "No hay proyectos")
            return
        idx = simpledialog.askinteger("Eliminar", f"ID de proyecto (1-{len(nom_proyecto)}):", minvalue=1,
                                      maxvalue=len(nom_proyecto))
        if idx and messagebox.askyesno("Confirmar", "¿Eliminar proyecto y sus tareas?"):
            idx -= 1
            tareas_a_eliminar = [i for i, p in enumerate(tarea_proyecto) if p == idx]
            for t_id in sorted(tareas_a_eliminar, reverse=True):
                i = 0
                while i < len(reg_tarea):
                    if reg_tarea[i] == t_id:
                        for lista in [reg_tarea, reg_empleado, reg_fecha, reg_horas]:
                            lista.pop(i)
                    else:
                        if reg_tarea[i] > t_id:
                            reg_tarea[i] -= 1
                        i += 1
                nom_tarea.pop(t_id)
                tarea_proyecto.pop(t_id)
                tarea_empleado.pop(t_id)
            for i in range(len(tarea_proyecto)):
                if tarea_proyecto[i] > idx:
                    tarea_proyecto[i] -= 1
            nom_proyecto.pop(idx)
            self.refresh_all_tables()
            messagebox.showinfo("Exito", "Proyecto eliminado")

    def buscar_empleado(self):
        if not nom_empleado:
            messagebox.showinfo("Info", "No hay empleados")
            return
        busq = simpledialog.askstring("Buscar", "Ingrese nombre:").lower()
        if busq:
            res = [f"[{i + 1}] {n} - {c}" for i, (n, c) in enumerate(zip(nom_empleado, cargo_empleado)) if
                   busq in n.lower()]
            messagebox.showinfo("Resultados", "\n".join(res) if res else "No encontrado")

    def buscar_proyecto(self):
        if not nom_proyecto:
            messagebox.showinfo("Info", "No hay proyectos")
            return
        busq = simpledialog.askstring("Buscar", "Ingrese nombre:").lower()
        if busq:
            res = [f"[{i + 1}] {n}" for i, n in enumerate(nom_proyecto) if busq in n.lower()]
            messagebox.showinfo("Resultados", "\n".join(res) if res else "No encontrado")

    def ver_horas_tarea(self):
        if not nom_tarea:
            messagebox.showinfo("Info", "No hay tareas")
            return
        res = "\n".join(
            [f"{i + 1}. {nom_tarea[i]}: {sum(reg_horas[j] for j in range(len(reg_horas)) if reg_tarea[j] == i):.1f}h"
             for i in range(len(nom_tarea))])
        messagebox.showinfo("Horas por Tarea", res)

    def ver_horas_proyecto(self):
        if not nom_proyecto:
            messagebox.showinfo("Info", "No hay proyectos")
            return
        res = "\n".join([
            f"{i + 1}. {nom_proyecto[i]}: {sum(reg_horas[j] for j in range(len(reg_horas)) if tarea_proyecto[reg_tarea[j]] == i):.1f}h"
            for i in range(len(nom_proyecto))])
        messagebox.showinfo("Horas por Proyecto", res)

    def ver_horas_empleado(self):
        if not nom_empleado:
            messagebox.showinfo("Info", "No hay empleados")
            return
        res = "\n".join([
            f"{i + 1}. {nom_empleado[i]}: {sum(reg_horas[j] for j in range(len(reg_horas)) if reg_empleado[j] == i):.1f}h"
            for i in range(len(nom_empleado))])
        messagebox.showinfo("Horas por Empleado", res)

    def exportar_reporte(self):
        res = "=== REPORTE ===\n\nPROYECTOS:\n" + "\n".join(
            [f"- {p}: {sum(reg_horas[j] for j in range(len(reg_horas)) if tarea_proyecto[reg_tarea[j]] == i):.1f}h" for
             i, p in enumerate(nom_proyecto)])
        res += "\n\nEMPLEADOS:\n" + "\n".join(
            [f"- {e}: {sum(reg_horas[j] for j in range(len(reg_horas)) if reg_empleado[j] == i):.1f}h" for i, e in
             enumerate(nom_empleado)])
        self.show_info_window("Reporte", res)

    def acerca_de(self):
        messagebox.showinfo("Acerca de", "Gestor de Proyectos Simple\nUniversidad de El Salvador\nCiclo I/2026")

    def show_info_window(self, title, content):
        d = Toplevel(self.root)
        d.title(title)
        d.geometry("500x400")
        d.configure(bg=self.colors["white"])
        t = Text(d, wrap=tk.WORD, font=("Consolas", 10), bg=self.colors["light"], fg=self.colors["dark"])
        t.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        t.insert(tk.END, content)
        t.config(state=tk.DISABLED)
        tk.Button(d, text="Cerrar", command=d.destroy, bg=self.colors["accent"], fg="white").pack(pady=10)


# --------------------------------------------------------------------------
#   EJECUCION
# --------------------------------------------------------------------------

if __name__ == "__main__":
    print("✅ Iniciando aplicacion...")
    print(f"✅ validar_fecha existe: {callable(validar_fecha)}")
    root = tk.Tk()
    app = GestorProyectosApp(root)
    root.mainloop()