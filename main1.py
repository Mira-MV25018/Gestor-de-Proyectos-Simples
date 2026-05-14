
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


