# Gestor de Proyectos Simple 

Aplicación de línea de comandos (CLI) desarrollada en Python como proyecto de ciclo para la asignatura **Lógica de Programación Orientada a Objetos** — Ciclo I/2026, Universidad de El Salvador.

---

##  Integrantes

| # | Nombre                             | Carné     |
|---|------------------------------------|-----------|
| 1 | [José Amilcar Mira Vásquez]        | [MV25018] |
| 2 | [Kenia Yamileth Murillo Gutiérrez] | [MG25049] |

---

##  Descripción del proyecto

Sistema que permite gestionar proyectos empresariales, sus tareas y el registro de horas trabajadas por empleado. Incluye validaciones de lógica de negocio como evitar jornadas irreales (más de 24 horas en un día).

### Lógica de negocio implementada
- Un proyecto tiene varias tareas asignadas a empleados.
- Los empleados pueden registrar las horas que trabajan en cada tarea.
- Se calcula el total de horas por tarea y por proyecto.
- Se evita que un empleado registre más de 24 horas en un mismo día.

---

##  Cómo ejecutar el programa
    Desde la raíz del proyecto:

    python main.py

    Ejemplo:

    ===== GESTOR DE PROYECTOS =====

    [1] Registrar empleado
    [2] Registrar proyecto
    [3] Registrar tarea
    [4] Registrar horas trabajadas
    ...
    [0] Salir

    Seleccione una opción:

### Versión Gráfica
    python "Interfaz del Sistema/main.py"

    La interfaz gráfica permite administrar empleados, proyectos, tareas y horas trabajadas de forma visual mediante Tkinter.

### Requisitos previos
- Python 3.8 o superior instalado
- No requiere librerías externas

### Pasos

1. Clona el repositorio:
```bash
git clone https://github.com/[usuario]/[nombre-repo].git
cd [nombre-repo]
```

2. Ejecuta el programa principal:
```bash
python main.py
```

3. Navega por el menú con los números correspondientes a cada opción.

---

## Cómo ejecutar las pruebas unitarias

Las pruebas se encuentran en la carpeta `tests/`.

```bash
# Desde la raíz del proyecto
python -m pytest tests/test_servicios.py -v
```

O con unittest directamente:
```bash
python -m unittest tests/test_servicios.py -v
```

### Ejemplo de salida esperada

test_01_validar_fecha_formato_correcto ... ok test_02_validar_fecha_formato_incorrecto ... ok test_03_validar_fecha_dias_mes_correcto ... ok ... test_41_prueba_registro_horas_limite ... ok ---------------------------------------------------------------------- Ran 41 tests 

OK

---

##  Estructura del proyecto

```
Gestor-de-Proyectos-Simples/ 
│ 
├── main.py 
├── test_servicios.py 
├── README.md 
├── .gitignore 
│
├── Interfaz del Sistema/ 
│ └── main.py 
│ 
└── pseudocódigo/
```

---

##  Funcionalidades del menú

| Opción | Descripción |
|--------|-------------|
[1] Registrar empleado
[2] Registrar proyecto
[3] Registrar tarea
[4] Registrar horas trabajadas

[5] Ver horas por tarea
[6] Ver horas por proyecto
[7] Ver horas por empleado

[8] Actualizar empleado
[9] Actualizar proyecto
[10] Eliminar tarea
[11] Eliminar empleado
[12] Eliminar proyecto
[13] Buscar empleado

[0] Salir

---

##  Validaciones implementadas

- Validación de datos
    -Los nombres no pueden estar vacíos.
    -Los IDs deben existir antes de realizar operaciones.
    -No pueden registrarse tareas sin empleados y proyectos válidos.
- Validación de horas
    -Las horas deben ser mayores que cero.
    -No se permiten registros mayores a 24 horas.
    -Un empleado no puede acumular más de 24 horas en una misma fecha.
- Validación de fechas
    -Formato obligatorio: DD/MM/AAAA.
    -Validación de días según el mes.
    -Soporte para años bisiestos.
    -Rango permitido entre 2000 y 2100.

---

## Tecnologías usadas

- **Python 3** — lenguaje principal
- **unittest** — pruebas unitarias
- **Git / GitHub** — control de versiones

---

## Estado del proyecto

| Entrega | Fecha | Estado |
|---------|-------|--------|
| Entrega #1 | 13 – 19 Abril |  Completada |
| Entrega #2 | 18 – 24 Mayo | Completada |
| Entrega #3 | 15 – 21 Junio |  en proceso |
