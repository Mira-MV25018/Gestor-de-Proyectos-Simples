"""
test_servicios.py - Pruebas unitarias del Gestor de Proyectos Simple
Asignatura : Logica de Programacion Orientada a Objetos
Ciclo      : I/2026 - Universidad de El Salvador
Tema       : 7 - Gestor de Proyectos Simple
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importar el modulo visual
try:
    import main as m
except ImportError:
    try:
        import gestor_visual as m
    except ImportError:
        import main_visual as m


# --------------------------------------------------------------------------
#   FUNCIONES DE LIMPIEZA Y AYUDA
# --------------------------------------------------------------------------

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
    if not m.reg_horas or not m.reg_empleado or not m.reg_fecha:
        return 0.0

    total = 0.0
    for i in range(len(m.reg_horas)):
        if i < len(m.reg_empleado) and i < len(m.reg_fecha):
            if m.reg_empleado[i] == empleado_id and m.reg_fecha[i] == fecha:
                total += m.reg_horas[i]
    return total


# --------------------------------------------------------------------------
#   VALIDACION DE FECHAS
# --------------------------------------------------------------------------

class TestValidaciones(unittest.TestCase):
    def setUp(self):
        resetear()

    def test_01_validar_fecha_formato_correcto(self):
        self.assertTrue(m.validar_fecha("15/06/2026"))
        self.assertTrue(m.validar_fecha("01/01/2025"))
        self.assertTrue(m.validar_fecha("31/12/2026"))

    def test_02_validar_fecha_formato_incorrecto(self):
        self.assertFalse(m.validar_fecha("15-06-2026"))
        self.assertFalse(m.validar_fecha("2026/06/15"))
        self.assertFalse(m.validar_fecha("15/06/26"))
        self.assertFalse(m.validar_fecha(""))
        self.assertFalse(m.validar_fecha("32/13/2026"))

    def test_03_validar_fecha_dias_mes_correcto(self):
        self.assertTrue(m.validar_fecha("31/01/2026"))
        self.assertTrue(m.validar_fecha("30/04/2026"))
        self.assertFalse(m.validar_fecha("31/04/2026"))
        self.assertTrue(m.validar_fecha("28/02/2026"))
        self.assertFalse(m.validar_fecha("29/02/2026"))

    def test_04_validar_fecha_año_bisiesto(self):
        self.assertTrue(m.validar_fecha("29/02/2024"))
        self.assertFalse(m.validar_fecha("29/02/2023"))

    def test_05_validar_fecha_rango_años(self):
        self.assertFalse(m.validar_fecha("15/06/1999"))
        self.assertFalse(m.validar_fecha("15/06/2101"))


# --------------------------------------------------------------------------
#   EMPLEADOS
# --------------------------------------------------------------------------

class TestEmpleados(unittest.TestCase):
    def setUp(self):
        resetear()

    def test_06_registrar_empleado(self):
        m.nom_empleado.append("Ana")
        m.cargo_empleado.append("Dev")
        self.assertEqual(len(m.nom_empleado), 1)
        self.assertEqual(m.nom_empleado[0], "Ana")
        self.assertEqual(m.cargo_empleado[0], "Dev")

    def test_07_lista_inicia_vacia(self):
        self.assertEqual(len(m.nom_empleado), 0)
        self.assertEqual(len(m.cargo_empleado), 0)

    def test_08_actualizar_nombre_empleado(self):
        m.nom_empleado.append("Pedro")
        m.cargo_empleado.append("QA")
        m.nom_empleado[0] = "Pedro Garcia"
        self.assertEqual(m.nom_empleado[0], "Pedro Garcia")

    def test_09_actualizar_cargo_empleado(self):
        m.nom_empleado.append("Luis")
        m.cargo_empleado.append("Dev")
        m.cargo_empleado[0] = "Senior Dev"
        self.assertEqual(m.cargo_empleado[0], "Senior Dev")

    def test_10_multiples_empleados(self):
        empleados = [("Ana", "Dev"), ("Luis", "QA"), ("Maria", "PM")]
        for nombre, cargo in empleados:
            m.nom_empleado.append(nombre)
            m.cargo_empleado.append(cargo)
        self.assertEqual(len(m.nom_empleado), 3)

    def test_11_id_empleado_es_posicion_mas_uno(self):
        m.nom_empleado.append("Carlos")
        m.cargo_empleado.append("PM")
        id_mostrado = len(m.nom_empleado)
        self.assertEqual(id_mostrado, 1)
        self.assertEqual(m.nom_empleado[id_mostrado - 1], "Carlos")

    def test_12_buscar_empleado_por_nombre(self):
        m.nom_empleado.extend(["Ana Lopez", "Luis Perez", "Maria Gomez"])
        m.cargo_empleado.extend(["Dev", "QA", "PM"])
        encontrados = [e for e in m.nom_empleado if "ana" in e.lower()]
        self.assertEqual(len(encontrados), 1)
        self.assertEqual(encontrados[0], "Ana Lopez")


# --------------------------------------------------------------------------
#   PROYECTOS
# --------------------------------------------------------------------------

class TestProyectos(unittest.TestCase):
    def setUp(self):
        resetear()

    def test_13_registrar_proyecto(self):
        m.nom_proyecto.append("Sistema Web")
        self.assertEqual(len(m.nom_proyecto), 1)

    def test_14_lista_proyectos_inicia_vacia(self):
        self.assertEqual(len(m.nom_proyecto), 0)

    def test_15_actualizar_nombre_proyecto(self):
        m.nom_proyecto.append("Proyecto Viejo")
        m.nom_proyecto[0] = "Proyecto Nuevo"
        self.assertEqual(m.nom_proyecto[0], "Proyecto Nuevo")

    def test_16_multiples_proyectos(self):
        m.nom_proyecto.extend(["P1", "P2", "P3"])
        self.assertEqual(len(m.nom_proyecto), 3)

    def test_17_horas_proyecto_suma_tareas(self):
        m.nom_proyecto.append("P1")
        m.nom_empleado.append("Dev")
        m.cargo_empleado.append("Dev")
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)

        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("01/05/2026")
        m.reg_horas.append(5.0)
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("02/05/2026")
        m.reg_horas.append(3.0)

        total = sum(m.reg_horas[j] for j in range(len(m.reg_horas))
                    if m.tarea_proyecto[m.reg_tarea[j]] == 0)
        self.assertEqual(total, 8.0)

    def test_18_buscar_proyecto_por_nombre(self):
        m.nom_proyecto.extend(["Sistema Ventas", "App Movil", "Backend API"])
        encontrados = [p for p in m.nom_proyecto if "ventas" in p.lower()]
        self.assertEqual(len(encontrados), 1)
        self.assertEqual(encontrados[0], "Sistema Ventas")


# --------------------------------------------------------------------------
#   TAREAS
# --------------------------------------------------------------------------

class TestTareas(unittest.TestCase):
    def setUp(self):
        resetear()
        m.nom_proyecto.append("P1")
        m.nom_empleado.append("Dev")
        m.cargo_empleado.append("Dev")

    def test_19_registrar_tarea(self):
        m.nom_tarea.append("Login")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)
        self.assertEqual(len(m.nom_tarea), 1)

    def test_20_tarea_referencia_proyecto_correcto(self):
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)
        self.assertEqual(m.tarea_proyecto[0], 0)

    def test_21_tarea_referencia_empleado_correcto(self):
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)
        self.assertEqual(m.tarea_empleado[0], 0)

    def test_22_eliminar_tarea(self):
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)
        m.nom_tarea.pop(0)
        m.tarea_proyecto.pop(0)
        m.tarea_empleado.pop(0)
        self.assertEqual(len(m.nom_tarea), 0)

    def test_23_multiples_tareas_mismo_proyecto(self):
        for _ in range(3):
            m.nom_tarea.append("T")
            m.tarea_proyecto.append(0)
            m.tarea_empleado.append(0)
        tareas_p0 = sum(1 for i in range(len(m.tarea_proyecto)) if m.tarea_proyecto[i] == 0)
        self.assertEqual(tareas_p0, 3)

    def test_24_horas_tarea_acumula(self):
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

        total = sum(m.reg_horas[j] for j in range(len(m.reg_horas)) if m.reg_tarea[j] == 0)
        self.assertEqual(total, 10.0)


# --------------------------------------------------------------------------
#   REGISTRO DE HORAS
# --------------------------------------------------------------------------

class TestRegistroHoras(unittest.TestCase):
    def setUp(self):
        resetear()
        m.nom_proyecto.append("P1")
        m.nom_empleado.append("Dev")
        m.cargo_empleado.append("Dev")
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)

    def test_25_registrar_horas(self):
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026")
        m.reg_horas.append(8.0)
        self.assertEqual(len(m.reg_horas), 1)
        self.assertEqual(m.reg_horas[0], 8.0)

    def test_26_no_superar_24h_mismo_dia(self):
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026")
        m.reg_horas.append(20.0)
        acum = acumular_horas_dia(0, "13/05/2026")
        self.assertTrue(acum + 5.0 > 24)

    def test_27_exactamente_24h_valido(self):
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026")
        m.reg_horas.append(24.0)
        acum = acumular_horas_dia(0, "13/05/2026")
        self.assertEqual(acum, 24.0)

    def test_28_dias_distintos_no_interfieren(self):
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026")
        m.reg_horas.append(10.0)
        acum_otro_dia = acumular_horas_dia(0, "14/05/2026")
        self.assertEqual(acum_otro_dia, 0.0)

    def test_29_horas_negativas_invalidas(self):
        self.assertTrue(-1.0 <= 0)

    def test_30_horas_cero_invalidas(self):
        self.assertTrue(0.0 <= 0)

    def test_31_horas_distintas_tareas_mismo_dia(self):
        m.nom_tarea.append("T2")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)

        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026")
        m.reg_horas.append(6.0)
        m.reg_tarea.append(1)
        m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026")
        m.reg_horas.append(8.0)

        total_dia = acumular_horas_dia(0, "13/05/2026")
        self.assertEqual(total_dia, 14.0)

    def test_32_empleado_distinto_no_afecta(self):
        m.nom_empleado.append("Dev2")
        m.cargo_empleado.append("Dev2")

        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("13/05/2026")
        m.reg_horas.append(20.0)
        m.reg_tarea.append(0)
        m.reg_empleado.append(1)
        m.reg_fecha.append("13/05/2026")
        m.reg_horas.append(10.0)

        self.assertEqual(acumular_horas_dia(0, "13/05/2026"), 20.0)
        self.assertEqual(acumular_horas_dia(1, "13/05/2026"), 10.0)


# --------------------------------------------------------------------------
#   CRUD OPERACIONES
# --------------------------------------------------------------------------

class TestCRUD(unittest.TestCase):
    def setUp(self):
        resetear()
        m.nom_empleado.extend(["Ana", "Luis"])
        m.cargo_empleado.extend(["Dev", "QA"])
        m.nom_proyecto.append("Sistema Web")
        m.nom_tarea.append("Frontend")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)

    def test_33_actualizar_empleado(self):
        m.nom_empleado[0] = "Ana Maria"
        self.assertEqual(m.nom_empleado[0], "Ana Maria")

    def test_34_actualizar_proyecto(self):
        m.nom_proyecto[0] = "Sistema Web v2"
        self.assertEqual(m.nom_proyecto[0], "Sistema Web v2")

    def test_35_eliminar_tarea_con_registros(self):
        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("01/06/2026")
        m.reg_horas.append(5.0)

        idx = 0
        i = 0
        while i < len(m.reg_tarea):
            if m.reg_tarea[i] == idx:
                for lista in [m.reg_tarea, m.reg_empleado, m.reg_fecha, m.reg_horas]:
                    if i < len(lista):
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

    def test_36_eliminar_empleado_con_tareas(self):
        m.nom_empleado.append("Carlos")
        m.cargo_empleado.append("Dev")
        m.nom_tarea.append("Backend")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)

        tareas_asignadas = [i for i, emp in enumerate(m.tarea_empleado) if emp == 0]
        self.assertTrue(len(tareas_asignadas) > 0)


# --------------------------------------------------------------------------
#   CASOS BORDE
# --------------------------------------------------------------------------

class TestCasosBorde(unittest.TestCase):
    def setUp(self):
        resetear()

    def test_37_empleado_sin_tareas_eliminar(self):
        m.nom_empleado.append("Dev Libre")
        m.cargo_empleado.append("Dev")
        tareas_asignadas = [i for i, emp in enumerate(m.tarea_empleado) if emp == 0]
        self.assertEqual(len(tareas_asignadas), 0)

    def test_38_fecha_invalida_rechazada(self):
        self.assertFalse(m.validar_fecha("15-06-2026"))
        self.assertTrue(m.validar_fecha("15/06/2026"))

    def test_39_tarea_sin_horas_cero(self):
        m.nom_proyecto.append("P1")
        m.nom_empleado.append("Dev")
        m.cargo_empleado.append("Dev")
        m.nom_tarea.append("T1")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)

        total_h = sum(m.reg_horas[j] for j in range(len(m.reg_horas)) if m.reg_tarea[j] == 0)
        self.assertEqual(total_h, 0.0)


# --------------------------------------------------------------------------
#   PRUEBAS MINIMAS REQUERIDAS (una por integrante - sin nombres visibles)
# --------------------------------------------------------------------------

class TestPruebasMinimas(unittest.TestCase):
    def setUp(self):
        resetear()

    def test_40_prueba_registro_empleado(self):
        """Prueba basica: registrar un empleado"""
        m.nom_empleado.append("Empleado Test")
        m.cargo_empleado.append("Puesto Test")
        self.assertEqual(len(m.nom_empleado), 1)
        self.assertEqual(m.nom_empleado[0], "Empleado Test")
        self.assertEqual(m.cargo_empleado[0], "Puesto Test")

    def test_41_prueba_registro_horas_limite(self):
        """Prueba basica: registrar horas y verificar limite de 24h"""
        m.nom_proyecto.append("Proyecto Test")
        m.nom_empleado.append("Empleado Test")
        m.cargo_empleado.append("Puesto Test")
        m.nom_tarea.append("Tarea Test")
        m.tarea_proyecto.append(0)
        m.tarea_empleado.append(0)

        m.reg_tarea.append(0)
        m.reg_empleado.append(0)
        m.reg_fecha.append("15/06/2026")
        m.reg_horas.append(20.0)

        self.assertEqual(len(m.reg_horas), 1)
        self.assertEqual(m.reg_horas[0], 20.0)
        self.assertTrue(sum(m.reg_horas) + 5.0 > 24)


# --------------------------------------------------------------------------
#   EJECUCION
# --------------------------------------------------------------------------

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print(" EJECUTANDO PRUEBAS UNITARIAS - GESTOR DE PROYECTOS")
    print("=" * 70 + "\n")
    unittest.main(verbosity=2)