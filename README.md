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

```
test_registrar_empleado_agrega_a_lista ... ok
test_lista_inicia_vacia ... ok
test_actualizar_nombre_empleado ... ok
...
Ran 18 tests in 0.002s
OK
```

---

##  Estructura del proyecto

```
gestor-proyectos/
│
├── main.py                  # Programa principal (menú CLI)
├── tests/
│   └── test_servicios.py    # Pruebas unitarias
├── .gitignore
└── README.md
```

---

##  Funcionalidades del menú

| Opción | Descripción |
|--------|-------------|
| 1 | Registrar empleado |
| 2 | Registrar proyecto |
| 3 | Registrar tarea (asignada a proyecto y empleado) |
| 4 | Registrar horas trabajadas (con validación de 24h/día) |
| 5 | Ver horas acumuladas por tarea |
| 6 | Ver horas acumuladas por proyecto |
| 7 | Actualizar datos de un empleado *(CRUD)* |
| 8 | Actualizar nombre de un proyecto *(CRUD)* |
| 9 | Eliminar una tarea *(CRUD)* |
| 0 | Salir |

---

##  Validaciones implementadas

- Nombres y campos no pueden estar vacíos.
- Los IDs de empleado, proyecto y tarea deben existir.
- Las horas deben ser un número mayor a 0 y no superar 24.
- Un empleado no puede acumular más de 24 horas en el mismo día.

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
| Entrega #2 | 18 – 24 Mayo | En progreso |
| Entrega #3 | 15 – 21 Junio |  Pendiente |
