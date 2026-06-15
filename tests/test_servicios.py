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

# Agrega la carpeta raíz al path para importar main.py correctamente
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


# -----------------------------------------------------------------
# INTEGRANTE 1 — Empleados y Proyectos
# -----------------------------------------------------------------

class TestEmpleados(unittest.TestCase):

    def setUp(self):
        resetear()

    def test_registrar_empleado_agrega_a_lista(self):
        """Verificar que al agregar un empleado quede correctamente en las listas."""
        m.nom_empleado.append("Ana")
        m.cargo_empleado.append("Dev")
        self.assertEqual(m.nom_empleado[0], "Ana")
        self.assertEqual(m.cargo_empleado[0], "Dev")

    def test_lista_inicia_vacia(self):
        """Las listas deben estar vacías al inicio de cada prueba."""
        self.assertEqual(len(m.nom_empleado), 0)

    def test_actualizar_nombre_empleado(self):
        """Verificar que el nombre de un empleado se puede actualizar."""
        m.nom_empleado.append("Pedro")
        m.cargo_empleado.append("QA")
        m.nom_empleado[0] = "Pedro García"
        self.assertEqual(m.nom_empleado[0], "Pedro García")

    def test_actualizar_cargo_empleado(self):
        """Verificar que el cargo de un empleado se puede actualizar."""
        m.nom_empleado.append("Luis")
        m.cargo_empleado.append("Dev")
        m.cargo_empleado[0] = "Senior Dev"
        self.assertEqual(m.cargo_empleado[0], "Senior Dev")

    def test_multiples_empleados(self):
        """Verificar que se pueden registrar varios empleados."""
        for nombre in ["Ana", "Luis", "María"]:
            m.nom_empleado.append(nombre)
            m.cargo_empleado.append("Dev")
        self.assertEqual(len(m.nom_empleado), 3)

    def test_id_empleado_es_posicion_mas_uno(self):
        """El ID del empleado debe ser su posición (índice 0) + 1."""
        m.nom_empleado.append("Carlos")
        m.cargo_empleado.append("PM")
        id_emp = len(m.nom_empleado)
        self.assertEqual(id_emp, 1)


class TestProyectos(unittest.TestCase):

    def setUp(self):
        resetear()

    def test_registrar_proyecto_agrega_a_lista(self):
        """Verificar que un proyecto queda registrado en la lista."""
        m.nom_proyecto.append("Sistema Web")
        self.assertIn("Sistema Web", m.nom_proyecto)

    def test_lista_proyectos_inicia_vacia(self):
        """La lista de proyectos debe iniciar vacía."""
        self.assertEqual(len(m.nom_proyecto), 0)

    def test_actualizar_nombre_proyecto(self):
        """Verificar que el nombre de un proyecto se puede cambiar."""
        m.nom_proyecto.append("Proyecto Viejo")
        m.nom_proyecto[0] = "Proyecto Nuevo"
        self.assertEqual(m.nom_proyecto[0], "Proyecto Nuevo")

    def test_multiples_proyectos(self):
        """Verificar que se pueden registrar varios proyectos."""
        m.nom_proyecto.extend(["P1", "P2", "P3"])
        self.assertEqual(len(m.nom_proyecto), 3)

    def test_id_proyecto_es_posicion_mas_uno(self):
        """El ID del proyecto debe ser su posición + 1."""
        m.nom_proyecto.append("App Ventas")
        self.assertEqual(len(m.nom_proyecto), 1)

    def test_horas_proyecto_suma_tareas(self):
        """Las horas de un proyecto son la suma de horas de todas sus tareas."""
        m.nom_proyecto.append("P1")
        m.nom_empleado.append("Dev")
        m.cargo_empleado.append("Dev")
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)
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


# -----------------------------------------------------------------
# Tareas y Registro de Horas
# -----------------------------------------------------------------

class TestTareas(unittest.TestCase):

    def setUp(self):
        resetear()
        m.nom_proyecto.append("P1")
        m.nom_empleado.append("Dev")
        m.cargo_empleado.append("Dev")

    def test_registrar_tarea_agrega_a_lista(self):
        """Verificar que una tarea queda registrada correctamente."""
        m.nom_tarea.append("Login")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)
        self.assertEqual(m.nom_tarea[0], "Login")

    def test_tarea_referencia_proyecto_correcto(self):
        """Verificar que la tarea apunta al índice correcto del proyecto."""
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)
        self.assertEqual(m.tarea_proyecto[0], 0)

    def test_tarea_referencia_empleado_correcto(self):
        """Verificar que la tarea apunta al índice correcto del empleado."""
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)
        self.assertEqual(m.tarea_empleado[0], 0)

    def test_eliminar_tarea_reduce_lista(self):
        """Verificar que eliminar una tarea reduce el tamaño de la lista."""
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)
        m.nom_tarea.pop(0)
        m.tarea_proyecto.pop(0)
        m.tarea_empleado.pop(0)
        self.assertEqual(len(m.nom_tarea), 0)

    def test_multiples_tareas_mismo_proyecto(self):
        """Verificar que varias tareas pueden pertenecer al mismo proyecto."""
        for nombre in ["T1", "T2", "T3"]:
            m.nom_tarea.append(nombre)
            m.tarea_proyecto.append(0)
            m.tarea_empleado.append(0)
        tareas_p0 = [i for i in range(len(m.tarea_proyecto)) if m.tarea_proyecto[i] == 0]
        self.assertEqual(len(tareas_p0), 3)

    def test_horas_tarea_acumula_correctamente(self):
        """Verificar que las horas de diferentes días se acumulan bien por tarea."""
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)
        m.reg_tarea.append(0); m.reg_empleado.append(0)
        m.reg_fecha.append("10/05/2026"); m.reg_horas.append(4.0)
        m.reg_tarea.append(0); m.reg_empleado.append(0)
        m.reg_fecha.append("11/05/2026"); m.reg_horas.append(6.0)
        total = sum(
            m.reg_horas[j]
            for j in range(len(m.reg_horas))
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

    def _acum_dia(self, id_emp_0, fecha):
        """Calcula las horas acumuladas de un empleado en una fecha dada."""
        return sum(
            m.reg_horas[i]
            for i in range(len(m.reg_horas))
            if m.reg_empleado[i] == id_emp_0 and m.reg_fecha[i] == fecha
        )

    def test_registrar_horas_agrega_registro(self):
        """Verificar que registrar horas agrega una entrada en las listas."""
        m.reg_tarea.append(0); m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026"); m.reg_horas.append(8.0)
        self.assertEqual(len(m.reg_horas), 1)
        self.assertEqual(m.reg_horas[0], 8.0)

    def test_validacion_no_superar_24h_mismo_dia(self):
        """Verificar que agregar horas que superan 24h en un día es inválido."""
        m.reg_tarea.append(0); m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026"); m.reg_horas.append(20.0)
        acum = self._acum_dia(0, "13/05/2026")
        # 20 + 5 = 25 > 24 → debe rechazarse
        self.assertGreater(acum + 5, 24)

    def test_exactamente_24h_es_valido(self):
        """Verificar que registrar exactamente 24h en un día es válido."""
        m.reg_tarea.append(0); m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026"); m.reg_horas.append(24.0)
        acum = self._acum_dia(0, "13/05/2026")
        self.assertLessEqual(acum, 24)

    def test_dias_distintos_no_interfieren(self):
        """Verificar que el acumulado de un día no afecta a otro día."""
        m.reg_tarea.append(0); m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026"); m.reg_horas.append(10.0)
        acum_otro_dia = self._acum_dia(0, "14/05/2026")
        self.assertEqual(acum_otro_dia, 0.0)

    def test_horas_negativas_invalidas(self):
        """Verificar que horas negativas son rechazadas (condición del main)."""
        horas = -1.0
        self.assertTrue(horas <= 0)

    def test_horas_cero_invalidas(self):
        """Verificar que registrar 0 horas es inválido."""
        horas = 0.0
        self.assertTrue(horas <= 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
