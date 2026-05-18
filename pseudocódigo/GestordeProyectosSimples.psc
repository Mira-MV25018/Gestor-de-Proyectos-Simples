// ============================================================
//   GESTOR DE PROYECTOS SIMPLE

// ============================================================

Algoritmo GestorDeProyectos
	
	Definir nomEmpleado    Como Caracter
	Definir cargoEmpleado  Como Caracter
	Definir nomProyecto    Como Caracter
	Definir nomTarea       Como Caracter
	Definir tareaProyecto  Como Entero
	Definir tareaEmpleado  Como Entero
	Definir regTarea       Como Entero
	Definir regEmpleado    Como Entero
	Definir regFecha       Como Caracter
	Definir regHoras       Como Real
	
	Dimension nomEmpleado[50]
	Dimension cargoEmpleado[50]
	Dimension nomProyecto[50]
	Dimension nomTarea[50]
	Dimension tareaProyecto[50]
	Dimension tareaEmpleado[50]
	Dimension regTarea[50]
	Dimension regEmpleado[50]
	Dimension regFecha[50]
	Dimension regHoras[50]
	
	Definir totalEmpleados Como Entero
	Definir totalProyectos Como Entero
	Definir totalTareas    Como Entero
	Definir totalRegistros Como Entero
	Definir opcion         Como Entero
	Definir i              Como Entero
	Definir j              Como Entero
	Definir idAux          Como Entero
	Definir idAux2         Como Entero
	Definir textoAux       Como Caracter
	Definir realAux        Como Real
	Definir acumDia        Como Real
	Definir totalH         Como Real
	Definir granTotal      Como Real
	
	totalEmpleados <- 0
	totalProyectos <- 0
	totalTareas    <- 0
	totalRegistros <- 0
	
	Repetir
		Escribir ""
		Escribir "====================================="
		Escribir "     GESTOR DE PROYECTOS SIMPLE      "
		Escribir "====================================="
		Escribir "  1. Registrar empleado"
		Escribir "  2. Registrar proyecto"
		Escribir "  3. Registrar tarea"
		Escribir "  4. Registrar horas trabajadas"
		Escribir "  5. Ver horas por tarea"
		Escribir "  6. Ver horas por proyecto"
		Escribir "  0. Salir"
		Escribir "====================================="
		Escribir "Elige una opcion: "
		Leer opcion
		
		Segun opcion Hacer
			
			1:
				Escribir ""
				Escribir "--- REGISTRAR EMPLEADO ---"
				Si totalEmpleados >= 50 Entonces
					Escribir "ERROR: Limite maximo de empleados alcanzado."
				SiNo
					Escribir "Nombre del empleado: "
					Leer textoAux
					totalEmpleados <- totalEmpleados + 1
					nomEmpleado[totalEmpleados] <- textoAux
					Escribir "Cargo: "
					Leer textoAux
					cargoEmpleado[totalEmpleados] <- textoAux
					Escribir "Empleado registrado. ID: ", totalEmpleados
					Escribir "Nombre: ", nomEmpleado[totalEmpleados], " | Cargo: ", cargoEmpleado[totalEmpleados]
				FinSi
			
			2:
				Escribir ""
				Escribir "--- REGISTRAR PROYECTO ---"
				Si totalProyectos >= 50 Entonces
					Escribir "ERROR: Limite maximo de proyectos alcanzado."
				SiNo
					Escribir "Nombre del proyecto: "
					Leer textoAux
					totalProyectos <- totalProyectos + 1
					nomProyecto[totalProyectos] <- textoAux
					Escribir "Proyecto registrado. ID: ", totalProyectos
					Escribir "Nombre: ", nomProyecto[totalProyectos]
				FinSi
			
			3:
				Escribir ""
				Escribir "--- REGISTRAR TAREA ---"
				Si totalTareas >= 50 Entonces
					Escribir "ERROR: Limite maximo de tareas alcanzado."
				SiNo
					Si totalProyectos = 0 Entonces
						Escribir "ERROR: No hay proyectos. Registra un proyecto primero."
					SiNo
						Si totalEmpleados = 0 Entonces
							Escribir "ERROR: No hay empleados. Registra un empleado primero."
						SiNo
							Escribir "Proyectos disponibles:"
							Para i <- 1 Hasta totalProyectos Hacer
								Escribir "  [", i, "] ", nomProyecto[i]
							FinPara
							Escribir "ID del proyecto: "
							Leer idAux
							Si idAux < 1 O idAux > totalProyectos Entonces
								Escribir "ERROR: ID de proyecto no valido."
							SiNo
								Escribir "Empleados disponibles:"
								Para i <- 1 Hasta totalEmpleados Hacer
									Escribir "  [", i, "] ", nomEmpleado[i]
								FinPara
								Escribir "ID del empleado asignado: "
								Leer idAux2
								Si idAux2 < 1 O idAux2 > totalEmpleados Entonces
									Escribir "ERROR: ID de empleado no valido."
								SiNo
									Escribir "Nombre de la tarea: "
									Leer textoAux
									totalTareas <- totalTareas + 1
									nomTarea[totalTareas]      <- textoAux
									tareaProyecto[totalTareas] <- idAux
									tareaEmpleado[totalTareas] <- idAux2
									Escribir "Tarea registrada. ID: ", totalTareas
									Escribir "Tarea: ", nomTarea[totalTareas]
									Escribir "Proyecto: ", nomProyecto[idAux]
									Escribir "Empleado: ", nomEmpleado[idAux2]
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			
			4:
				Escribir ""
				Escribir "--- REGISTRAR HORAS TRABAJADAS ---"
				Si totalTareas = 0 Entonces
					Escribir "ERROR: No hay tareas registradas."
				SiNo
					Si totalEmpleados = 0 Entonces
						Escribir "ERROR: No hay empleados registrados."
					SiNo
						Escribir "Tareas disponibles:"
						Para i <- 1 Hasta totalTareas Hacer
							Escribir "  [", i, "] ", nomTarea[i]
						FinPara
						Escribir "ID de la tarea: "
						Leer idAux
						Si idAux < 1 O idAux > totalTareas Entonces
							Escribir "ERROR: ID de tarea no valido."
						SiNo
							Escribir "Empleados disponibles:"
							Para i <- 1 Hasta totalEmpleados Hacer
								Escribir "  [", i, "] ", nomEmpleado[i]
							FinPara
							Escribir "ID del empleado: "
							Leer idAux2
							Si idAux2 < 1 O idAux2 > totalEmpleados Entonces
								Escribir "ERROR: ID de empleado no valido."
							SiNo
								Escribir "Fecha (DD/MM/AAAA): "
								Leer textoAux
								Escribir "Horas trabajadas: "
								Leer realAux
								Si realAux <= 0 O realAux > 24 Entonces
									Escribir "ERROR: Las horas deben ser entre 0.5 y 24."
								SiNo
									acumDia <- 0
									Para i <- 1 Hasta totalRegistros Hacer
										Si regEmpleado[i] = idAux2 Y regFecha[i] = textoAux Entonces
											acumDia <- acumDia + regHoras[i]
										FinSi
									FinPara
									Si acumDia + realAux > 24 Entonces
										Escribir "ERROR: ", nomEmpleado[idAux2], " ya tiene ", acumDia, "h ese dia."
										Escribir "Puede registrar hasta ", 24 - acumDia, " hora(s) mas."
									SiNo
										totalRegistros <- totalRegistros + 1
										regTarea[totalRegistros]    <- idAux
										regEmpleado[totalRegistros] <- idAux2
										regFecha[totalRegistros]    <- textoAux
										regHoras[totalRegistros]    <- realAux
										Escribir "Horas registradas correctamente."
										Escribir "Empleado: ", nomEmpleado[idAux2], " | Tarea: ", nomTarea[idAux]
										Escribir "Fecha: ", textoAux, " | Horas: ", realAux
										Escribir "Total acumulado ese dia: ", acumDia + realAux, "h"
									FinSi
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			
			5:
				Escribir ""
				Escribir "--- HORAS POR TAREA ---"
				Si totalTareas = 0 Entonces
					Escribir "No hay tareas registradas."
				SiNo
					Para i <- 1 Hasta totalTareas Hacer
						totalH <- 0
						Para j <- 1 Hasta totalRegistros Hacer
							Si regTarea[j] = i Entonces
								totalH <- totalH + regHoras[j]
							FinSi
						FinPara
						Escribir "  [", i, "] ", nomTarea[i], " -> ", totalH, " hora(s)"
					FinPara
				FinSi
			
			6:
				Escribir ""
				Escribir "--- HORAS POR PROYECTO ---"
				Si totalProyectos = 0 Entonces
					Escribir "No hay proyectos registrados."
				SiNo
					granTotal <- 0
					Para i <- 1 Hasta totalProyectos Hacer
						totalH <- 0
						Para j <- 1 Hasta totalRegistros Hacer
							Si tareaProyecto[regTarea[j]] = i Entonces
								totalH <- totalH + regHoras[j]
							FinSi
						FinPara
						granTotal <- granTotal + totalH
						Escribir "  [", i, "] ", nomProyecto[i], " -> ", totalH, " hora(s)"
					FinPara
					Escribir "-------------------------------"
					Escribir "  TOTAL GENERAL: ", granTotal, " hora(s)"
				FinSi
			
			0:
				Escribir "Hasta luego!"
			
			De Otro Modo:
				Escribir "Opcion no valida."
		FinSegun
		
	Hasta Que opcion = 0

FinAlgoritmo
