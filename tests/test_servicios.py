"""
tests/test_servicios.py - Pruebas unitarias del Gestor de Proyectos Simple
- Integrante 1: pruebas de empleados y proyectos
- Integrante 2: pruebas de tareas y registro de horas
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import main as m

def resetear():
    """Limpia todas las listas antes de cada prueba."""
    m.nom_empleado.clear();   m.cargo_empleado.clear()
    m.nom_proyecto.clear()
    m.nom_tarea.clear();      m.tarea_proyecto.clear(); m.tarea_empleado.clear()
    m.reg_tarea.clear();      m.reg_empleado.clear()
    m.reg_fecha.clear();      m.reg_horas.clear()

# ─────────────────────────────────────────────
# PRUEBAS UNITARIAS DE LOS EMPLEADOS
# ─────────────────────────────────────────────

class TestEmpleados(unittest.TestCase):

    def setUp(self):
        resetear()

    def test_registrar_empleado_agrega_a_lista(self):
        m.nom_empleado.append("Ana"); m.cargo_empleado.append("Dev")
        self.assertEqual(m.nom_empleado[0], "Ana")
        self.assertEqual(m.cargo_empleado[0], "Dev")

    def test_lista_inicia_vacia(self):
        self.assertEqual(len(m.nom_empleado), 0)

    def test_actualizar_nombre_empleado(self):
        m.nom_empleado.append("Pedro"); m.cargo_empleado.append("QA")
        m.nom_empleado[0] = "Pedro García"
        self.assertEqual(m.nom_empleado[0], "Pedro García")

    def test_actualizar_cargo_empleado(self):
        m.nom_empleado.append("Luis"); m.cargo_empleado.append("Dev")
        m.cargo_empleado[0] = "Senior Dev"
        self.assertEqual(m.cargo_empleado[0], "Senior Dev")

    def test_multiples_empleados(self):
        for nombre in ["Ana", "Luis", "María"]:
            m.nom_empleado.append(nombre)
            m.cargo_empleado.append("Dev")
        self.assertEqual(len(m.nom_empleado), 3)

    def test_id_empleado_es_posicion_mas_uno(self):
        m.nom_empleado.append("Carlos"); m.cargo_empleado.append("PM")
        id_emp = len(m.nom_empleado)
        self.assertEqual(id_emp, 1)

# ─────────────────────────────────────────────
# AGREGANDO PRUEBAS UNITARIAS DE PROYECTOS
# ─────────────────────────────────────────────
class TestProyectos(unittest.TestCase):

    def setUp(self):
        resetear()

    def test_registrar_proyecto_agrega_a_lista(self):
        m.nom_proyecto.append("Sistema Web")
        self.assertIn("Sistema Web", m.nom_proyecto)

    def test_lista_proyectos_inicia_vacia(self):
        self.assertEqual(len(m.nom_proyecto), 0)

    def test_actualizar_nombre_proyecto(self):
        m.nom_proyecto.append("Proyecto Viejo")
        m.nom_proyecto[0] = "Proyecto Nuevo"
        self.assertEqual(m.nom_proyecto[0], "Proyecto Nuevo")

    def test_multiples_proyectos(self):
        m.nom_proyecto.extend(["P1", "P2", "P3"])
        self.assertEqual(len(m.nom_proyecto), 3)

    def test_id_proyecto_es_posicion_mas_uno(self):
        m.nom_proyecto.append("App Ventas")
        self.assertEqual(len(m.nom_proyecto), 1)

    def test_horas_proyecto_suma_tareas(self):
        # Proyecto 0, empleado 0, tarea 0
        m.nom_proyecto.append("P1")
        m.nom_empleado.append("Dev"); m.cargo_empleado.append("Dev")
        m.nom_tarea.append("T1"); m.tarea_proyecto.append(0); m.tarea_empleado.append(0)
        m.reg_tarea.append(0); m.reg_empleado.append(0)
        m.reg_fecha.append("01/05/2026"); m.reg_horas.append(5.0)
        m.reg_tarea.append(0); m.reg_empleado.append(0)
        m.reg_fecha.append("02/05/2026"); m.reg_horas.append(3.0)
        total = sum(
            m.reg_horas[j]
            for j in range(len(m.reg_horas))
            if m.tarea_proyecto[m.reg_tarea[j]] == 0
        )
        self.assertEqual(total, 8.0)

# ───────────────────────────────────────────────
# AGREGANDO PRUEBAS DE TAREAS Y REGISTRO DE HORA
# ───────────────────────────────────────────────
class TestTareas(unittest.TestCase):

    def setUp(self):
        resetear()
        m.nom_proyecto.append("P1")
        m.nom_empleado.append("Dev"); m.cargo_empleado.append("Dev")

    def test_registrar_tarea_agrega_a_lista(self):
        m.nom_tarea.append("Login")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)
        self.assertEqual(m.nom_tarea[0], "Login")

    def test_tarea_referencia_proyecto_correcto(self):
        m.nom_tarea.append("T1"); m.tarea_proyecto.append(0); m.tarea_empleado.append(0)
        self.assertEqual(m.tarea_proyecto[0], 0)

    def test_tarea_referencia_empleado_correcto(self):
        m.nom_tarea.append("T1"); m.tarea_proyecto.append(0); m.tarea_empleado.append(0)
        self.assertEqual(m.tarea_empleado[0], 0)

    def test_eliminar_tarea_reduce_lista(self):
        m.nom_tarea.append("T1"); m.tarea_proyecto.append(0); m.tarea_empleado.append(0)
        m.nom_tarea.pop(0); m.tarea_proyecto.pop(0); m.tarea_empleado.pop(0)
        self.assertEqual(len(m.nom_tarea), 0)

    def test_multiples_tareas_mismo_proyecto(self):
        for nombre in ["T1", "T2", "T3"]:
            m.nom_tarea.append(nombre)
            m.tarea_proyecto.append(0)
            m.tarea_empleado.append(0)
        tareas_p0 = [i for i in range(len(m.tarea_proyecto)) if m.tarea_proyecto[i] == 0]
        self.assertEqual(len(tareas_p0), 3)

    def test_horas_tarea_acumula_correctamente(self):
        m.nom_tarea.append("T1"); m.tarea_proyecto.append(0); m.tarea_empleado.append(0)
        m.reg_tarea.append(0); m.reg_empleado.append(0)
        m.reg_fecha.append("10/05/2026"); m.reg_horas.append(4.0)
        m.reg_tarea.append(0); m.reg_empleado.append(0)
        m.reg_fecha.append("11/05/2026"); m.reg_horas.append(6.0)
        total = sum(m.reg_horas[j] for j in range(len(m.reg_horas)) if m.reg_tarea[j] == 0)
        self.assertEqual(total, 10.0)
