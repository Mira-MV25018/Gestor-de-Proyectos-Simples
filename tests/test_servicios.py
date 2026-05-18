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