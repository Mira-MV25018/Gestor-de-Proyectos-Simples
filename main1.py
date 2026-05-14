
# ------------------------------------------------------------
#   ALMACENAMIENTO EN MEMORIA
#--------------------------------------------------------------

nom_empleado   = []
cargo_empleado = []

nom_proyecto   = []

nom_tarea      = []
tarea_proyecto = []   # índice 0-based del proyecto de cada tarea
tarea_empleado = []   # índice 0-based del empleado asignado

reg_tarea      = []   # índice 0-based de la tarea
reg_empleado   = []   # índice 0-based del empleado
reg_fecha      = []   # "DD/MM/AAAA"
reg_horas      = []   # float


# --------------------------------------------------------------
#   UTILIDADES
# ---------------------------------------------------------------------

def separador():
    print("--------------------------------------------------------------------")

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Ingrese un número entero válido.")

def pedir_real(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("  Ingrese un número válido (ej: 4.5).")


# ------------------------------------------------------------------------
#   OPCIÓN 1 - REGISTRAR EMPLEADO
# --------------------------------------------------------------------------

def registrar_empleado():
    print("\n--- REGISTRAR EMPLEADO ---")
    nombre = input("Nombre del empleado: ").strip()
    if not nombre:
        print("ERROR: El nombre no puede estar vacío.")
        return
    cargo = input("Cargo: ").strip()
    if not cargo:
        print("ERROR: El cargo no puede estar vacío.")
        return
    nom_empleado.append(nombre)
    cargo_empleado.append(cargo)
    print(f"Empleado registrado. ID: {len(nom_empleado)}")
    print(f"Nombre: {nombre} | Cargo: {cargo}")


# ---------------------------------------------------------------------------
#   OPCIÓN 2 - REGISTRAR PROYECTO
# ---------------------------------------------------------------------

def registrar_proyecto():
    print("\n--- REGISTRAR PROYECTO ---")
    nombre = input("Nombre del proyecto: ").strip()
    if not nombre:
        print("ERROR: El nombre no puede estar vacío.")
        return
    nom_proyecto.append(nombre)
    print(f"Proyecto registrado. ID: {len(nom_proyecto)}")
    print(f"Nombre: {nombre}")


# --------------------------------------------------------------------
#   OPCIÓN 3 - REGISTRAR TAREA
# ----------------------------------------------------------------------------

def registrar_tarea():
    print("\n--- REGISTRAR TAREA ---")
    if not nom_proyecto:
        print("ERROR: No hay proyectos. Registra un proyecto primero.")
        return
    if not nom_empleado:
        print("ERROR: No hay empleados. Registra un empleado primero.")
        return

    print("Proyectos disponibles:")
    for i, p in enumerate(nom_proyecto, start=1):
        print(f"  [{i}] {p}")
    id_proy = pedir_entero("ID del proyecto: ")
    if id_proy < 1 or id_proy > len(nom_proyecto):
        print("ERROR: ID de proyecto no válido.")
        return

    print("Empleados disponibles:")
    for i, e in enumerate(nom_empleado, start=1):
        print(f"  [{i}] {e} - {cargo_empleado[i-1]}")
    id_emp = pedir_entero("ID del empleado asignado: ")
    if id_emp < 1 or id_emp > len(nom_empleado):
        print("ERROR: ID de empleado no válido.")
        return

    nombre = input("Nombre de la tarea: ").strip()
    if not nombre:
        print("ERROR: El nombre no puede estar vacío.")
        return

    nom_tarea.append(nombre)
    tarea_proyecto.append(id_proy - 1)
    tarea_empleado.append(id_emp - 1)
    print(f"Tarea registrada. ID: {len(nom_tarea)}")
    print(f"Tarea: {nombre}")
    print(f"Proyecto: {nom_proyecto[id_proy-1]}")
    print(f"Empleado: {nom_empleado[id_emp-1]}")

# --------------------------------------------------------------------
#   OPCIÓN 4 - REGISTRAR HORAS TRABAJADAS
# -----------------------------------------------------------------------

def registrar_horas():
    print("\n--- REGISTRAR HORAS TRABAJADAS ---")
    if not nom_tarea:
        print("ERROR: No hay tareas registradas.")
        return
    if not nom_empleado:
        print("ERROR: No hay empleados registrados.")
        return

    print("Tareas disponibles:")
    for i, t in enumerate(nom_tarea, start=1):
        print(f"  [{i}] {t}  (Proyecto: {nom_proyecto[tarea_proyecto[i-1]]})")
    id_tarea = pedir_entero("ID de la tarea: ")
    if id_tarea < 1 or id_tarea > len(nom_tarea):
        print("ERROR: ID de tarea no válido.")
        return

    print("Empleados disponibles:")
    for i, e in enumerate(nom_empleado, start=1):
        print(f"  [{i}] {e}")
    id_emp = pedir_entero("ID del empleado: ")
    if id_emp < 1 or id_emp > len(nom_empleado):
        print("ERROR: ID de empleado no válido.")
        return

    fecha = input("Fecha (DD/MM/AAAA): ").strip()
    horas = pedir_real("Horas trabajadas: ")

    if horas <= 0 or horas > 24:
        print("ERROR: Las horas deben ser entre 0.5 y 24.")
        return

    # Validar máximo 24h por día por empleado (igual que en PSeInt)
    acum_dia = sum(
        reg_horas[i]
        for i in range(len(reg_horas))
        if reg_empleado[i] == id_emp - 1 and reg_fecha[i] == fecha
    )
    if acum_dia + horas > 24:
        print(f"ERROR: {nom_empleado[id_emp-1]} ya tiene {acum_dia}h ese día.")
        print(f"Puede registrar hasta {24 - acum_dia:.1f} hora(s) más.")
        return

    reg_tarea.append(id_tarea - 1)
    reg_empleado.append(id_emp - 1)
    reg_fecha.append(fecha)
    reg_horas.append(horas)
    print("Horas registradas correctamente.")
    print(f"Empleado: {nom_empleado[id_emp-1]} | Tarea: {nom_tarea[id_tarea-1]}")
    print(f"Fecha: {fecha} | Horas: {horas}")
    print(f"Total acumulado ese día: {acum_dia + horas:.1f}h")

