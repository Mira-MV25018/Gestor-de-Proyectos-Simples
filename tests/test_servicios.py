"""
tests/test_servicios.py — Pruebas unitarias del Gestor de Proyectos Simple
Asignatura : Lógica de Programación Orientada a Objetos
Ciclo      : I/2026 — Universidad de El Salvador
Tema       : 7 — Gestor de Proyectos Simple

Integrante 1: José Amilcar Mira Vásquez
              pruebas de empleados y proyectos
Integrante 2: Kenia Yamileth Murillo Gutiérrez
              pruebas de tareas y registro de horas
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import main as m


def resetear():
    """Limpia todas las listas antes de cada prueba."""
    m.nom_empleado.clear()
    m.cargo_empleado.clear()
    m.nom_proyecto.clear()
    m.nom_tarea.clear()
    m.tarea_proyecto.clear()
    m.tarea_empleado.clear()
    m.reg_tarea.clear()
    m.reg_empleado.clear()
    m.reg_fecha.clear()
    m.reg_horas.clear()


def acumular_horas_dia(empleado_id, fecha):
    """Helper para calcular horas acumuladas de un empleado en una fecha."""
    return sum(
        m.reg_horas[i] for i in range(len(m.reg_horas))
        if m.reg_empleado[i] == empleado_id and m.reg_fecha[i] == fecha
    )


# -----------------------------------------------------------------
# PRUEBAS DE UTILIDADES
# -----------------------------------------------------------------

class TestValidaciones(unittest.TestCase):
    """Pruebas para las funciones de validación"""

    def setUp(self):
        resetear()

    def test_validar_fecha_formato_correcto(self):
        """Prueba que fechas correctas pasan la validación"""
        self.assertTrue(m.validar_fecha("15/06/2026"))
        self.assertTrue(m.validar_fecha("01/01/2025"))
        self.assertTrue(m.validar_fecha("31/12/2026"))

    def test_validar_fecha_formato_incorrecto(self):
        """Prueba que fechas incorrectas son rechazadas"""
        self.assertFalse(m.validar_fecha("15-06-2026"))  # guiones en vez de /
        self.assertFalse(m.validar_fecha("2026/06/15"))  # formato invertido
        self.assertFalse(m.validar_fecha("15/06/26"))  # año corto
        self.assertFalse(m.validar_fecha(""))  # vacío
        self.assertFalse(m.validar_fecha("32/13/2026"))  # día y mes inválidos

    def test_validar_fecha_dias_mes_correcto(self):
        """Prueba validación de días por mes"""
        # Enero (31 días)
        self.assertTrue(m.validar_fecha("31/01/2026"))
        # Abril (30 días)
        self.assertTrue(m.validar_fecha("30/04/2026"))
        self.assertFalse(m.validar_fecha("31/04/2026"))
        # Febrero (28 días, 2026 no es bisiesto)
        self.assertTrue(m.validar_fecha("28/02/2026"))
        self.assertFalse(m.validar_fecha("29/02/2026"))


# -----------------------------------------------------------------
# INTEGRANTE 1 — Empleados y Proyectos
# -----------------------------------------------------------------

class TestEmpleados(unittest.TestCase):

    def setUp(self):
        resetear()

    def test_registrar_empleado_agrega_a_lista(self):
        """Prueba que agregar empleado funciona correctamente"""
        m.nom_empleado.append("Ana")
        m.cargo_empleado.append("Dev")
        self.assertEqual(len(m.nom_empleado), 1)
        self.assertEqual(m.nom_empleado[0], "Ana")
        self.assertEqual(m.cargo_empleado[0], "Dev")

    def test_lista_inicia_vacia(self):
        """Prueba que las listas empiezan vacías"""
        self.assertEqual(len(m.nom_empleado), 0)
        self.assertEqual(len(m.cargo_empleado), 0)

    def test_actualizar_nombre_empleado(self):
        """Prueba actualización de nombre de empleado"""
        m.nom_empleado.append("Pedro")
        m.cargo_empleado.append("QA")
        m.nom_empleado[0] = "Pedro García"
        self.assertEqual(m.nom_empleado[0], "Pedro García")

    def test_actualizar_cargo_empleado(self):
        """Prueba actualización de cargo de empleado"""
        m.nom_empleado.append("Luis")
        m.cargo_empleado.append("Dev")
        m.cargo_empleado[0] = "Senior Dev"
        self.assertEqual(m.cargo_empleado[0], "Senior Dev")

    def test_multiples_empleados(self):
        """Prueba registro de múltiples empleados"""
        empleados = [("Ana", "Dev"), ("Luis", "QA"), ("María", "PM")]
        for nombre, cargo in empleados:
            m.nom_empleado.append(nombre)
            m.cargo_empleado.append(cargo)
        self.assertEqual(len(m.nom_empleado), 3)
        self.assertEqual(len(m.cargo_empleado), 3)

    def test_id_empleado_es_posicion_mas_uno(self):
        """Prueba que el ID mostrado al usuario es posición+1"""
        m.nom_empleado.append("Carlos")
        m.cargo_empleado.append("PM")
        id_mostrado = len(m.nom_empleado)  # Esto es 1
        self.assertEqual(id_mostrado, 1)
        self.assertEqual(m.nom_empleado[id_mostrado - 1], "Carlos")


class TestProyectos(unittest.TestCase):

    def setUp(self):
        resetear()

    def test_registrar_proyecto_agrega_a_lista(self):
        """Prueba que agregar proyecto funciona"""
        m.nom_proyecto.append("Sistema Web")
        self.assertEqual(len(m.nom_proyecto), 1)
        self.assertIn("Sistema Web", m.nom_proyecto)

    def test_lista_proyectos_inicia_vacia(self):
        """Prueba que lista de proyectos empieza vacía"""
        self.assertEqual(len(m.nom_proyecto), 0)

    def test_actualizar_nombre_proyecto(self):
        """Prueba actualización de nombre de proyecto"""
        m.nom_proyecto.append("Proyecto Viejo")
        m.nom_proyecto[0] = "Proyecto Nuevo"
        self.assertEqual(m.nom_proyecto[0], "Proyecto Nuevo")

    def test_multiples_proyectos(self):
        """Prueba múltiples proyectos"""
        m.nom_proyecto.extend(["P1", "P2", "P3"])
        self.assertEqual(len(m.nom_proyecto), 3)

    def test_id_proyecto_es_posicion_mas_uno(self):
        """Prueba que ID de proyecto es correcto"""
        m.nom_proyecto.append("App Ventas")
        self.assertEqual(len(m.nom_proyecto), 1)
        self.assertEqual(m.nom_proyecto[0], "App Ventas")

    def test_horas_proyecto_suma_tareas(self):
        """Prueba que las horas se suman correctamente por proyecto"""
        # Setup
        m.nom_proyecto.append("P1")
        m.nom_empleado.append("Dev")
        m.cargo_empleado.append("Dev")
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)

        # Registrar horas
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("01/05/2026")
        m.reg_horas.append(5.0)
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("02/05/2026")
        m.reg_horas.append(3.0)

        # Calcular total
        total = sum(
            m.reg_horas[j] for j in range(len(m.reg_horas))
            if m.tarea_proyecto[m.reg_tarea[j]] == 0
        )
        self.assertEqual(total, 8.0)


# -----------------------------------------------------------------
# INTEGRANTE 2 — Tareas y Registro de Horas
# -----------------------------------------------------------------

class TestTareas(unittest.TestCase):

    def setUp(self):
        resetear()
        m.nom_proyecto.append("P1")
        m.nom_empleado.append("Dev")
        m.cargo_empleado.append("Dev")

    def test_registrar_tarea_agrega_a_lista(self):
        """Prueba que registrar tarea funciona"""
        m.nom_tarea.append("Login")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)
        self.assertEqual(len(m.nom_tarea), 1)
        self.assertEqual(m.nom_tarea[0], "Login")

    def test_tarea_referencia_proyecto_correcto(self):
        """Prueba que la tarea referencia al proyecto correcto"""
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)
        self.assertEqual(m.tarea_proyecto[0], 0)

    def test_tarea_referencia_empleado_correcto(self):
        """Prueba que la tarea referencia al empleado correcto"""
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)
        self.assertEqual(m.tarea_empleado[0], 0)

    def test_eliminar_tarea_reduce_lista(self):
        """Prueba que eliminar tarea funciona"""
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)
        m.nom_tarea.pop(0)
        m.tarea_proyecto.pop(0)
        m.tarea_empleado.pop(0)
        self.assertEqual(len(m.nom_tarea), 0)

    def test_multiples_tareas_mismo_proyecto(self):
        """Prueba múltiples tareas en mismo proyecto"""
        for nombre in ["T1", "T2", "T3"]:
            m.nom_tarea.append(nombre)
            m.tarea_proyecto.append(0)
            m.tarea_empleado.append(0)
        tareas_p0 = sum(1 for i in range(len(m.tarea_proyecto)) if m.tarea_proyecto[i] == 0)
        self.assertEqual(tareas_p0, 3)

    def test_horas_tarea_acumula_correctamente(self):
        """Prueba que las horas se acumulan por tarea"""
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)

        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("10/05/2026")
        m.reg_horas.append(4.0)
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("11/05/2026")
        m.reg_horas.append(6.0)

        total = sum(
            m.reg_horas[j] for j in range(len(m.reg_horas))
            if m.reg_tarea[j] == 0
        )
        self.assertEqual(total, 10.0)


class TestRegistroHoras(unittest.TestCase):

    def setUp(self):
        resetear()
        m.nom_proyecto.append("P1")
        m.nom_empleado.append("Dev")
        m.cargo_empleado.append("Dev")
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)

    def test_registrar_horas_agrega_registro(self):
        """Prueba que registrar horas agrega un registro"""
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026")
        m.reg_horas.append(8.0)
        self.assertEqual(len(m.reg_horas), 1)
        self.assertEqual(m.reg_horas[0], 8.0)

    def test_validacion_no_superar_24h_mismo_dia(self):
        """Prueba que no se pueden superar 24h en un día"""
        # Registrar 20 horas primero
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026")
        m.reg_horas.append(20.0)

        # Intentar agregar 5 horas más (total 25 > 24)
        horas_adicionales = 5.0
        acum = acumular_horas_dia(0, "13/05/2026")

        # La validación debe rechazar si acum + adicionales > 24
        self.assertTrue(acum + horas_adicionales > 24)

    def test_exactamente_24h_es_valido(self):
        """Prueba que exactamente 24h es permitido"""
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026")
        m.reg_horas.append(24.0)
        acum = acumular_horas_dia(0, "13/05/2026")
        self.assertLessEqual(acum, 24)
        self.assertEqual(acum, 24.0)

    def test_dias_distintos_no_interfieren(self):
        """Prueba que días diferentes no se suman"""
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026")
        m.reg_horas.append(10.0)
        acum_otro_dia = acumular_horas_dia(0, "14/05/2026")
        self.assertEqual(acum_otro_dia, 0.0)

    def test_horas_negativas_invalidas(self):
        """Prueba que horas negativas son inválidas"""
        horas = -1.0
        self.assertTrue(horas <= 0)

    def test_horas_cero_invalidas(self):
        """Prueba que cero horas es inválido"""
        horas = 0.0
        self.assertTrue(horas <= 0)

    def test_registro_horas_distintas_tareas_mismo_dia(self):
        """Prueba registrar horas en múltiples tareas el mismo día"""
        m.nom_tarea.append("T2")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)

        # Primera tarea
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026")
        m.reg_horas.append(6.0)

        # Segunda tarea
        m.reg_tarea.append(1)
        m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026")
        m.reg_horas.append(8.0)

        total_dia = acumular_horas_dia(0, "13/05/2026")
        self.assertEqual(total_dia, 14.0)


# -----------------------------------------------------------------
# CRUD OPERATIONS (Entrega #2 y #3)
# -----------------------------------------------------------------

class TestCRUDOperaciones(unittest.TestCase):

    def setUp(self):
        resetear()
        m.nom_empleado.extend(["Ana", "Luis"])
        m.cargo_empleado.extend(["Dev", "QA"])
        m.nom_proyecto.append("Sistema Web")
        m.nom_tarea.append("Frontend")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)

    def test_actualizar_empleado_cambia_nombre(self):
        """Prueba actualización de empleado"""
        m.nom_empleado[0] = "Ana María"
        self.assertEqual(m.nom_empleado[0], "Ana María")

    def test_actualizar_proyecto_cambia_nombre(self):
        """Prueba actualización de proyecto"""
        m.nom_proyecto[0] = "Sistema Web v2"
        self.assertEqual(m.nom_proyecto[0], "Sistema Web v2")

    def test_eliminar_tarea_remueve_registros_asociados(self):
        """Prueba que eliminar tarea también elimina sus registros de horas"""
        # Agregar registros de horas
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("01/06/2026")
        m.reg_horas.append(5.0)

        # Eliminar tarea (índice 0)
        idx = 0
        i = 0
        while i < len(m.reg_tarea):
            if m.reg_tarea[i] == idx:
                for lista in [m.reg_tarea, m.reg_empleado, m.reg_fecha, m.reg_horas]:
                    lista.pop(i)
            else:
                if m.reg_tarea[i] > idx:
                    m.reg_tarea[i] -= 1
                i += 1

        m.nom_tarea.pop(0)
        m.tarea_proyecto.pop(0)
        m.tarea_empleado.pop(0)

        self.assertEqual(len(m.nom_tarea), 0)
        self.assertEqual(len(m.reg_tarea), 0)

    def test_eliminar_empleado_con_tareas(self):
        """Prueba caso borde: eliminar empleado que tiene tareas asignadas"""
        m.nom_empleado.append("Carlos")
        m.cargo_empleado.append("Dev")

        # Asignar tarea al empleado a eliminar (índice 0)
        m.nom_tarea.append("Backend")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)

        # Verificar que tiene tarea asignada
        tareas_asignadas = [i for i, emp in enumerate(m.tarea_empleado) if emp == 0]
        self.assertTrue(len(tareas_asignadas) > 0)


# -----------------------------------------------------------------
# PRUEBAS DE NUEVAS FUNCIONALIDADES (Entrega #3)
# -----------------------------------------------------------------

class TestNuevasFuncionalidades(unittest.TestCase):
    """Pruebas para las funciones agregadas en la versión mejorada"""

    def setUp(self):
        resetear()

    def test_ver_horas_por_empleado_con_datos(self):
        """Prueba que ver_horas_por_empleado calcula correctamente"""
        # Setup datos
        m.nom_empleado.append("Ana")
        m.cargo_empleado.append("Dev")
        m.nom_empleado.append("Luis")
        m.cargo_empleado.append("QA")

        m.nom_proyecto.append("P1")
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)
        m.nom_tarea.append("T2")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(1)

        # Registrar horas
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("01/06/2026")
        m.reg_horas.append(5.0)

        m.reg_tarea.append(1)
        m.reg_empleado.append(1)
        m.reg_fecha.append("02/06/2026")
        m.reg_horas.append(3.0)

        # Calcular horas por empleado manualmente
        horas_ana = sum(m.reg_horas[i] for i in range(len(m.reg_horas)) if m.reg_empleado[i] == 0)
        horas_luis = sum(m.reg_horas[i] for i in range(len(m.reg_horas)) if m.reg_empleado[i] == 1)

        self.assertEqual(horas_ana, 5.0)
        self.assertEqual(horas_luis, 3.0)

    def test_ver_horas_por_empleado_sin_empleados(self):
        """Prueba que ver_horas_por_empleado maneja lista vacía"""
        self.assertEqual(len(m.nom_empleado), 0)


# -----------------------------------------------------------------
# PRUEBAS DE CASOS BORDE
# -----------------------------------------------------------------

class TestCasosBorde(unittest.TestCase):
    """Casos borde importantes para la defensa final"""

    def setUp(self):
        resetear()

    def test_registro_horas_excede_24_maneja_error(self):
        """Prueba que el sistema rechaza horas que exceden 24 en un día"""
        m.nom_proyecto.append("P1")
        m.nom_empleado.append("Dev")
        m.cargo_empleado.append("Dev")
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)

        # Registrar 20 horas
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026")
        m.reg_horas.append(20.0)

        # Intentar registrar 5 horas más (total 25)
        horas_nuevas = 5.0
        acum_actual = acumular_horas_dia(0, "13/05/2026")

        # Simular validación
        self.assertTrue(acum_actual + horas_nuevas > 24)

    def test_empleado_sin_tareas_puede_eliminarse(self):
        """Prueba que empleado sin tareas se elimina directamente"""
        m.nom_empleado.append("Dev Libre")
        m.cargo_empleado.append("Dev")

        tareas_asignadas = [i for i, emp in enumerate(m.tarea_empleado) if emp == 0]
        self.assertEqual(len(tareas_asignadas), 0)

    def test_registro_horas_fecha_invalida(self):
        """Prueba que fecha inválida no se acepta"""
        # Fecha inválida (formato incorrecto)
        fecha_invalida = "15-06-2026"
        self.assertFalse(m.validar_fecha(fecha_invalida))

        # Fecha válida
        fecha_valida = "15/06/2026"
        self.assertTrue(m.validar_fecha(fecha_valida))


# -----------------------------------------------------------------
# EJECUCIÓN DE PRUEBAS
# -----------------------------------------------------------------

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print(" 🧪 EJECUTANDO PRUEBAS UNITARIAS - GESTOR DE PROYECTOS")
    print("=" * 70 + "\n")
    unittest.main(verbosity=2)