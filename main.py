# ------------------------------------------------------------------------
#   GESTOR DE PROYECTOS SIMPLE
#   Asignatura : Lógica de Programación Orientada a Objetos
#   Ciclo      : I/2026 — Universidad de El Salvador
#   Tema       : 7 — Gestor de Proyectos Simple
#   Integrantes: José Amilcar Mira Vásquez
#                Kenia Yamileth Murillo Gutiérrez
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------

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
#   UTILIDADES
# --------------------------------------------------------------------------

def separador():
    print("=" * 60)


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  ⚠ Ingrese un número entero válido.")


def pedir_real(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("  ⚠ Ingrese un número válido (ej: 4.5).")


# ⬇️⬇️⬇️ AQUÍ VA LA FUNCIÓN validar_fecha() ⬇️⬇️⬇️

def validar_fecha(fecha):
    """
    Valida que la fecha tenga formato DD/MM/AAAA y sea una fecha real.
    Validación completa incluyendo días por mes y años bisiestos.
    """
    if not fecha or len(fecha) != 10:
        return False
    if fecha[2] != '/' or fecha[5] != '/':
        return False
    partes = fecha.split('/')
    if len(partes) != 3:
        return False
    dia, mes, anio = partes
    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
        return False
    dia, mes, anio = int(dia), int(mes), int(anio)

    if mes < 1 or mes > 12:
        return False
    if dia < 1:
        return False
    if anio < 2000 or anio > 2100:
        return False

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def es_bisiesto(a):
        return (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)

    if es_bisiesto(anio):
        dias_por_mes[1] = 29

    if dia > dias_por_mes[mes - 1]:
        return False

    return True


# --------------------------------------------------------------------------
#   OPCIÓN 1 — REGISTRAR EMPLEADO
# --------------------------------------------------------------------------

def registrar_empleado():
    print("\n--- REGISTRAR EMPLEADO ---")
    nombre = input("Nombre del empleado: ").strip()
    if not nombre:
        print("  ❌ ERROR: El nombre no puede estar vacío.")
        return
    cargo = input("Cargo: ").strip()
    if not cargo:
        print("  ❌ ERROR: El cargo no puede estar vacío.")
        return
    nom_empleado.append(nombre)
    cargo_empleado.append(cargo)
    print(f"  ✅ Empleado registrado | ID: {len(nom_empleado)}")
    print(f"     Nombre: {nombre} | Cargo: {cargo}")


# --------------------------------------------------------------------------
#   OPCIÓN 2 — REGISTRAR PROYECTO
# --------------------------------------------------------------------------

def registrar_proyecto():
    print("\n--- REGISTRAR PROYECTO ---")
    nombre = input("Nombre del proyecto: ").strip()
    if not nombre:
        print("  ❌ ERROR: El nombre no puede estar vacío.")
        return
    nom_proyecto.append(nombre)
    print(f"  ✅ Proyecto registrado | ID: {len(nom_proyecto)}")
    print(f"     Nombre: {nombre}")


# --------------------------------------------------------------------------
#   OPCIÓN 3 — REGISTRAR TAREA
# --------------------------------------------------------------------------

def registrar_tarea():
    print("\n--- REGISTRAR TAREA ---")
    if not nom_proyecto:
        print("  ❌ ERROR: No hay proyectos. Registra un proyecto primero.")
        return
    if not nom_empleado:
        print("  ❌ ERROR: No hay empleados. Registra un empleado primero.")
        return

    print("\n  Proyectos disponibles:")
    for i, p in enumerate(nom_proyecto, start=1):
        print(f"     [{i}] {p}")
    id_proy = pedir_entero("  ID del proyecto: ")
    if id_proy < 1 or id_proy > len(nom_proyecto):
        print("  ❌ ERROR: ID de proyecto no válido.")
        return

    print("\n  Empleados disponibles:")
    for i, e in enumerate(nom_empleado, start=1):
        print(f"     [{i}] {e} ({cargo_empleado[i - 1]})")
    id_emp = pedir_entero("  ID del empleado asignado: ")
    if id_emp < 1 or id_emp > len(nom_empleado):
        print("  ❌ ERROR: ID de empleado no válido.")
        return

    nombre = input("  Nombre de la tarea: ").strip()
    if not nombre:
        print("  ❌ ERROR: El nombre no puede estar vacío.")
        return

    nom_tarea.append(nombre)
    tarea_proyecto.append(id_proy - 1)
    tarea_empleado.append(id_emp - 1)
    print(f"  ✅ Tarea registrada | ID: {len(nom_tarea)}")
    print(f"     Tarea   : {nombre}")
    print(f"     Proyecto: {nom_proyecto[id_proy - 1]}")
    print(f"     Empleado: {nom_empleado[id_emp - 1]}")


# --------------------------------------------------------------------------
#   OPCIÓN 4 — REGISTRAR HORAS TRABAJADAS
# --------------------------------------------------------------------------

def registrar_horas():
    print("\n--- REGISTRAR HORAS TRABAJADAS ---")
    if not nom_tarea:
        print("  ❌ ERROR: No hay tareas registradas.")
        return
    if not nom_empleado:
        print("  ❌ ERROR: No hay empleados registrados.")
        return

    print("\n  Tareas disponibles:")
    for i, t in enumerate(nom_tarea, start=1):
        print(f"     [{i}] {t} (Proyecto: {nom_proyecto[tarea_proyecto[i - 1]]})")
    id_tarea = pedir_entero("  ID de la tarea: ")
    if id_tarea < 1 or id_tarea > len(nom_tarea):
        print("  ❌ ERROR: ID de tarea no válido.")
        return

    print("\n  Empleados disponibles:")
    for i, e in enumerate(nom_empleado, start=1):
        print(f"     [{i}] {e}")
    id_emp = pedir_entero("  ID del empleado: ")
    if id_emp < 1 or id_emp > len(nom_empleado):
        print("  ❌ ERROR: ID de empleado no válido.")
        return

    fecha = input("  Fecha (DD/MM/AAAA): ").strip()
    if not validar_fecha(fecha):
        print("  ❌ ERROR: Formato de fecha inválido. Use DD/MM/AAAA (ej: 15/06/2026)")
        return

    horas = pedir_real("  Horas trabajadas: ")
    if horas <= 0:
        print("  ❌ ERROR: Las horas deben ser mayores a 0.")
        return
    if horas > 24:
        print("  ❌ ERROR: No se pueden registrar más de 24 horas en un solo registro.")
        return

    # Validar que no exceda 24 horas en el mismo día
    acum_dia = sum(
        reg_horas[i] for i in range(len(reg_horas))
        if reg_empleado[i] == id_emp - 1 and reg_fecha[i] == fecha
    )
    if acum_dia + horas > 24:
        restante = 24 - acum_dia
        print(f"  ❌ ERROR: {nom_empleado[id_emp - 1]} ya tiene {acum_dia:.1f}h ese día.")
        print(f"            Solo puede registrar hasta {restante:.1f} hora(s) más.")
        return

    reg_tarea.append(id_tarea - 1)
    reg_empleado.append(id_emp - 1)
    reg_fecha.append(fecha)
    reg_horas.append(horas)
    print("  ✅ Horas registradas correctamente.")
    print(f"     Empleado: {nom_empleado[id_emp - 1]} | Tarea: {nom_tarea[id_tarea - 1]}")
    print(f"     Fecha: {fecha} | Horas: {horas:.1f}")
    print(f"     Total acumulado ese día: {acum_dia + horas:.1f}h")


# --------------------------------------------------------------------------
#   OPCIÓN 5 — VER HORAS POR TAREA
# --------------------------------------------------------------------------

def ver_horas_por_tarea():
    print("\n--- HORAS POR TAREA ---")
    if not nom_tarea:
        print("  No hay tareas registradas.")
        return
    for i in range(len(nom_tarea)):
        total_h = sum(reg_horas[j] for j in range(len(reg_horas)) if reg_tarea[j] == i)
        print(f"  [{i + 1}] {nom_tarea[i]}")
        print(f"       Proyecto: {nom_proyecto[tarea_proyecto[i]]}")
        print(f"       Empleado: {nom_empleado[tarea_empleado[i]]}")
        print(f"       Horas: {total_h:.1f}h")
        print()


# --------------------------------------------------------------------------
#   OPCIÓN 6 — VER HORAS POR PROYECTO
# --------------------------------------------------------------------------

def ver_horas_por_proyecto():
    print("\n--- HORAS POR PROYECTO ---")
    if not nom_proyecto:
        print("  No hay proyectos registrados.")
        return
    gran_total = 0.0
    for i in range(len(nom_proyecto)):
        total_h = sum(
            reg_horas[j] for j in range(len(reg_horas))
            if tarea_proyecto[reg_tarea[j]] == i
        )
        gran_total += total_h
        print(f"  [{i + 1}] {nom_proyecto[i]} → {total_h:.1f}h")
    print("-" * 40)
    print(f"  📊 TOTAL GENERAL: {gran_total:.1f}h")


# --------------------------------------------------------------------------
#   OPCIÓN 7 — ACTUALIZAR EMPLEADO
# --------------------------------------------------------------------------

def actualizar_empleado():
    print("\n--- ACTUALIZAR EMPLEADO ---")
    if not nom_empleado:
        print("  ❌ ERROR: No hay empleados registrados.")
        return
    print("\n  Empleados disponibles:")
    for i, e in enumerate(nom_empleado, start=1):
        print(f"     [{i}] {e} ({cargo_empleado[i - 1]})")
    id_emp = pedir_entero("  ID del empleado a actualizar: ")
    if id_emp < 1 or id_emp > len(nom_empleado):
        print("  ❌ ERROR: ID no válido.")
        return
    print(f"     Nombre actual: {nom_empleado[id_emp - 1]}")
    print(f"     Cargo actual: {cargo_empleado[id_emp - 1]}")
    nuevo_nombre = input("  Nuevo nombre (ENTER para no cambiar): ").strip()
    nuevo_cargo = input("  Nuevo cargo (ENTER para no cambiar): ").strip()
    if nuevo_nombre:
        nom_empleado[id_emp - 1] = nuevo_nombre
    if nuevo_cargo:
        cargo_empleado[id_emp - 1] = nuevo_cargo
    print(f"  ✅ Empleado actualizado → {nom_empleado[id_emp - 1]} | {cargo_empleado[id_emp - 1]}")


# --------------------------------------------------------------------------
#   OPCIÓN 8 — ACTUALIZAR PROYECTO
# --------------------------------------------------------------------------

def actualizar_proyecto():
    print("\n--- ACTUALIZAR PROYECTO ---")
    if not nom_proyecto:
        print("  ❌ ERROR: No hay proyectos registrados.")
        return
    print("\n  Proyectos disponibles:")
    for i, p in enumerate(nom_proyecto, start=1):
        print(f"     [{i}] {p}")
    id_proy = pedir_entero("  ID del proyecto a actualizar: ")
    if id_proy < 1 or id_proy > len(nom_proyecto):
        print("  ❌ ERROR: ID no válido.")
        return
    print(f"     Nombre actual: {nom_proyecto[id_proy - 1]}")
    nuevo_nombre = input("  Nuevo nombre (ENTER para no cambiar): ").strip()
    if nuevo_nombre:
        nom_proyecto[id_proy - 1] = nuevo_nombre
        print(f"  ✅ Proyecto actualizado → {nom_proyecto[id_proy - 1]}")
    else:
        print("  Sin cambios.")


# --------------------------------------------------------------------------
#   OPCIÓN 9 — ELIMINAR TAREA
# --------------------------------------------------------------------------

def eliminar_tarea():
    print("\n--- ELIMINAR TAREA ---")
    if not nom_tarea:
        print("  ❌ ERROR: No hay tareas registradas.")
        return
    print("\n  Tareas disponibles:")
    for i, t in enumerate(nom_tarea, start=1):
        print(f"     [{i}] {t} (Proyecto: {nom_proyecto[tarea_proyecto[i - 1]]})")
    id_tarea = pedir_entero("  ID de la tarea a eliminar: ")
    if id_tarea < 1 or id_tarea > len(nom_tarea):
        print("  ❌ ERROR: ID no válido.")
        return

    idx = id_tarea - 1
    confirmacion = input(f"  ¿Eliminar tarea '{nom_tarea[idx]}'? (s/n): ").strip().lower()
    if confirmacion != 's':
        print("  Operación cancelada.")
        return

    nombre_eliminado = nom_tarea[idx]

    # Eliminar registros de horas asociados
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
    print(f"  ✅ Tarea '{nombre_eliminado}' eliminada correctamente.")


# --------------------------------------------------------------------------
#   OPCIÓN 10 — ELIMINAR EMPLEADO
# --------------------------------------------------------------------------

def eliminar_empleado():
    print("\n--- ELIMINAR EMPLEADO ---")
    if not nom_empleado:
        print("  ❌ ERROR: No hay empleados registrados.")
        return

    print("\n  Empleados disponibles:")
    for i, e in enumerate(nom_empleado, start=1):
        tareas_asignadas = sum(1 for x in tarea_empleado if x == i - 1)
        print(f"     [{i}] {e} ({cargo_empleado[i - 1]}) - {tareas_asignadas} tarea(s)")

    id_emp = pedir_entero("  ID del empleado a eliminar: ")
    if id_emp < 1 or id_emp > len(nom_empleado):
        print("  ❌ ERROR: ID no válido.")
        return

    idx = id_emp - 1
    nombre_eliminado = nom_empleado[idx]

    tareas_asignadas = [i for i, emp in enumerate(tarea_empleado) if emp == idx]
    if tareas_asignadas:
        print(f"  ⚠ ATENCIÓN: El empleado tiene {len(tareas_asignadas)} tarea(s) asignada(s):")
        for t_id in tareas_asignadas:
            print(f"     - {nom_tarea[t_id]} (Proyecto: {nom_proyecto[tarea_proyecto[t_id]]})")
        confirmacion = input("  ¿Eliminar empleado y REASIGNAR sus tareas? (s/n): ").strip().lower()
        if confirmacion != 's':
            print("  Operación cancelada.")
            return
        if len(nom_empleado) > 1:
            # Buscar otro empleado para reasignar (preferiblemente el primero diferente)
            nuevo_emp = 0 if idx != 0 else 1
            for t_id in tareas_asignadas:
                tarea_empleado[t_id] = nuevo_emp
            print(f"  ✅ Tareas reasignadas a: {nom_empleado[nuevo_emp]}")
        else:
            print("  ❌ ERROR: No hay otros empleados para reasignar tareas.")
            print("     Elimine las tareas primero o registre otro empleado.")
            return

    # Eliminar registros de horas
    i = 0
    while i < len(reg_empleado):
        if reg_empleado[i] == idx:
            for lista in [reg_tarea, reg_empleado, reg_fecha, reg_horas]:
                lista.pop(i)
        else:
            if reg_empleado[i] > idx:
                reg_empleado[i] -= 1
            i += 1

    # Reindexar tareas
    for i in range(len(tarea_empleado)):
        if tarea_empleado[i] > idx:
            tarea_empleado[i] -= 1

    nom_empleado.pop(idx)
    cargo_empleado.pop(idx)

    print(f"  ✅ Empleado '{nombre_eliminado}' eliminado correctamente.")


# --------------------------------------------------------------------------
#   OPCIÓN 11 — ELIMINAR PROYECTO
# --------------------------------------------------------------------------

def eliminar_proyecto():
    print("\n--- ELIMINAR PROYECTO ---")
    if not nom_proyecto:
        print("  ❌ ERROR: No hay proyectos registrados.")
        return

    print("\n  Proyectos disponibles:")
    for i, p in enumerate(nom_proyecto, start=1):
        tareas_asociadas = sum(1 for x in tarea_proyecto if x == i - 1)
        print(f"     [{i}] {p} - {tareas_asociadas} tarea(s)")

    id_proy = pedir_entero("  ID del proyecto a eliminar: ")
    if id_proy < 1 or id_proy > len(nom_proyecto):
        print("  ❌ ERROR: ID no válido.")
        return

    idx = id_proy - 1
    nombre_eliminado = nom_proyecto[idx]

    tareas_a_eliminar = [i for i, proy in enumerate(tarea_proyecto) if proy == idx]

    if tareas_a_eliminar:
        print(f"  ⚠ ATENCIÓN: El proyecto tiene {len(tareas_a_eliminar)} tarea(s):")
        for t_id in tareas_a_eliminar:
            print(f"     - {nom_tarea[t_id]} (Empleado: {nom_empleado[tarea_empleado[t_id]]})")
        confirmacion = input("  ¿Eliminar proyecto y TODAS sus tareas? (s/n): ").strip().lower()
        if confirmacion != 's':
            print("  Operación cancelada.")
            return

        # Eliminar tareas de mayor a menor índice
        for t_id in sorted(tareas_a_eliminar, reverse=True):
            # Eliminar registros de horas
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

        # Reindexar tareas restantes
        for i in range(len(tarea_proyecto)):
            if tarea_proyecto[i] > idx:
                tarea_proyecto[i] -= 1

    nom_proyecto.pop(idx)
    print(f"  ✅ Proyecto '{nombre_eliminado}' eliminado correctamente.")


# --------------------------------------------------------------------------
#   OPCIÓN 12 (EXTRA) — VER HORAS POR EMPLEADO
# --------------------------------------------------------------------------

def ver_horas_por_empleado():
    """Función adicional para cumplir con el CRUD completo y mostrar horas individuales"""
    print("\n--- HORAS POR EMPLEADO ---")
    if not nom_empleado:
        print("  No hay empleados registrados.")
        return
    for i in range(len(nom_empleado)):
        total_h = sum(
            reg_horas[j] for j in range(len(reg_horas))
            if reg_empleado[j] == i
        )
        print(f"  [{i + 1}] {nom_empleado[i]} ({cargo_empleado[i]}) → {total_h:.1f}h")

# --------------------------------------------------------------------------
#   OPCIÓN 13  — BUSCAR EMPLEADO 
# --------------------------------------------------------------------------
def buscar_empleado():
    print("\n--- BUSCAR EMPLEADO ---")

    if not nom_empleado:
        print("ERROR: No hay empleados registrados.")
        return

    nombre = input("Ingrese el nombre del empleado: ").strip().lower()

    encontrados = False

    for i, empleado in enumerate(nom_empleado):
        if nombre in empleado.lower():
            print(f"[{i+1}] {empleado}")
            print(f"     Cargo: {cargo_empleado[i]}")
            encontrados = True

    if not encontrados:
        print("No se encontraron empleados.")

# --------------------------------------------------------------------------
#   OPCIÓN 14  — BUSCAR PROYECTO
# --------------------------------------------------------------------------
def buscar_proyecto():
    print("\n--- BUSCAR PROYECTO ---")

    if not nom_proyecto:
        print("ERROR: No hay proyectos registrados.")
        return

    nombre = input("Ingrese el nombre del proyecto: ").strip().lower()

    encontrados = False

    for i, proyecto in enumerate(nom_proyecto):
        if nombre in proyecto.lower():
            print(f"[{i+1}] {proyecto}")
            encontrados = True

    if not encontrados:
        print("No se encontraron proyectos.")

# --------------------------------------------------------------------------
#   MENÚ PRINCIPAL
# --------------------------------------------------------------------------

def menu_principal():
    opcion = -1
    while opcion != 0:
        print()
        separador()
        print("       🚀 GESTOR DE PROYECTOS SIMPLE")
        print("  Universidad de El Salvador — Ciclo I/2026")
        separador()
        print("  📋 REGISTROS:")
        print("  [1] Registrar empleado")
        print("  [2] Registrar proyecto")
        print("  [3] Registrar tarea")
        print("  [4] Registrar horas trabajadas")
        print()
        print("  📊 CONSULTAS:")
        print("  [5] Ver horas por tarea")
        print("  [6] Ver horas por proyecto")
        print("  [7] Ver horas por empleado (extra)")
        print()
        print("  ✏️  CRUD COMPLETO:")
        print("  [8] Actualizar empleado")
        print("  [9] Actualizar proyecto")
        print(" [10] Eliminar tarea")
        print(" [11] Eliminar empleado")
        print(" [12] Eliminar proyecto")
        print(" [13] Buscar empleado")
        separador()
        print("  [0] Salir")
        separador()
        opcion = pedir_entero("  Elige una opción: ")

        if opcion == 1:
            registrar_empleado()
        elif opcion == 2:
            registrar_proyecto()
        elif opcion == 3:
            registrar_tarea()
        elif opcion == 4:
            registrar_horas()
        elif opcion == 5:
            ver_horas_por_tarea()
        elif opcion == 6:
            ver_horas_por_proyecto()
        elif opcion == 7:
            ver_horas_por_empleado()
        elif opcion == 8:
            actualizar_empleado()
        elif opcion == 9:
            actualizar_proyecto()
        elif opcion == 10:
            eliminar_tarea()
        elif opcion == 11:
            eliminar_empleado()
        elif opcion == 12:
            eliminar_proyecto()
        elif opcion == 0:
            print("\n  👋 ¡Hasta luego! Gracias por usar el gestor.")
        else:
            print("  ⚠ Opción no válida. Intente de nuevo.")


# --------------------------------------------------------------------------
#   PUNTO DE ENTRADA PRINCIPAL
# --------------------------------------------------------------------------

if __name__ == "__main__":
    menu_principal()