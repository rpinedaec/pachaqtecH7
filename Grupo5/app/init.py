#imports
from conn import Conexion
from functions import *
import time
# Definición de todos los menus:
menuPrincipal = Menu({1: "Crear Matricula", 2: "Listar Docentes", 3: "Listar Alumnos", 4: "Mantenimiento"},
                     "Colegio Perez de Cuellar", "Menú Principal")                     
menuMantenimiento = Menu({1: "Alumnos",    2: "Docentes", 3: "Salones", 4: "Cursos", 5: "Notas", 6: "Periodo escolar", 7: "Grados"},
                   "Colegio Perez de Cuellar", "Menú Mantenimiento")
menuMantAlumnos = Menu({1: "Crear Alumno",    2: "Modificar Alumno", 3: "Eliminar Alumno"},
                   "Colegio Perez de Cuellar", "Menú mantenimiento Alumno")
menuMantDocentes = Menu({1: "Crear Docente",    2: "Modificar Docente", 3: "Eliminar Docente"},
                   "Colegio Perez de Cuellar", "Menú mantenimiento Docente")
menuMantSalones = Menu({1: "Crear Salón",    2: "Modificar Salón", 3: "Eliminar Salón"},
                   "Colegio Perez de Cuellar", "Menú mantenimiento Salon")
menuMantCursos = Menu({1: "Crear Curso",    2: "Modificar Curso", 3: "Eliminar Curso"},
                   "Colegio Perez de Cuellar", "Menú mantenimiento Curso")
menuMantNotas = Menu({1: "Crear Notas",    2: "Modificar Nota", 3: "Eliminar Nota"},
                   "Colegio Perez de Cuellar", "Menú mantenimiento Nota")
menuMantPeriodo = Menu({1: "Crear Periodo",    2: "Modificar Periodo", 3: "Eliminar Periodo"},
                   "Colegio Perez de Cuellar", "Menú mantenimiento Periodo")
menuMantGrados = Menu({1: "Crear Grados",    2: "Modificar Grados", 3: "Eliminar Grados"},
                   "Colegio Perez de Cuellar", "Menú mantenimiento Grados")
# Menu de navegación
while True:
    intOptionSelect = menuPrincipal.show()
    if intOptionSelect == 1:  # Menu Cuadro de merito
        crearMatricula()
    elif intOptionSelect == 2:  # Menu Listar Docente
        listarDocentes()
    elif intOptionSelect == 3:  # Menu Listar Alumnos
        listarAlumnos()
    elif intOptionSelect == 4:  # Menu Mantenimiento
        while True:
            intOptionSelect = menuMantenimiento.show()
            if intOptionSelect == 1:  # Mantenimiento Alumno
                while True:
                    intOptionSelect = menuMantAlumnos.show()
                    if intOptionSelect == 1: #Crear alumno
                        crearAlumno()
                    elif intOptionSelect == 2: #modificar alumno
                        modificarAlumno()
                    elif intOptionSelect == 3: #Eliminar alumno
                        eliminarAlumno()
                    else:
                        break
            elif intOptionSelect == 2:  # Mantenimiento Docente 
                while True:
                    intOptionSelect = menuMantDocentes.show()
                    if intOptionSelect == 1: #Crear Docente99
                        crearProfesor()
                    elif intOptionSelect == 2: #Modificar Docente
                        modificarProfesor()
                    elif intOptionSelect == 3: #Eliminar Docente
                        eliminarProfesor()
                    else:
                        break
            elif intOptionSelect == 3:  # Mantenimiento Salones
                while True:
                    intOptionSelect = menuMantSalones.show()
                    if intOptionSelect == 1: #Crear Salon
                        crearSalon()
                    elif intOptionSelect == 2: #Modificar Salon
                        modificarSalon()
                    elif intOptionSelect == 3: #Eliminar Salon
                        eliminarSalon()
                    else:
                        break
            elif intOptionSelect == 4:  # Mantenimiento Cursos
                while True:
                    intOptionSelect = menuMantCursos.show()
                    if intOptionSelect == 1: #Crear curso
                        crearCurso()
                    elif intOptionSelect == 2: #Modificar curso
                        modificarCursos()
                    elif intOptionSelect == 3: #Eliminar curso
                        eliminarCursos()
                    else:
                        break
            elif intOptionSelect == 5:  # Mantenimiento Notas
                while True:
                    intOptionSelect = menuMantNotas.show()
                    if intOptionSelect == 1: #Crear nota
                        crearNota()
                    elif intOptionSelect == 2: #Modificar nota
                        modificarNota()
                    elif intOptionSelect == 3: #Eliminar nota
                        eliminarNota()
                    else:
                        break
            elif intOptionSelect == 6:  # Mantenimiento Periodo Escolar
                while True:
                    intOptionSelect = menuMantPeriodo.show()
                    if intOptionSelect == 1: #Crear periodo
                        crearPeriodo()
                    elif intOptionSelect == 2: #Modificar periodo
                        modificarPeriodo()
                    elif intOptionSelect == 3: #Eliminar periodo
                        eliminarPeriodo()
                    else:
                        break
            elif intOptionSelect == 7:  # Mantenimiento Grados
                while True:
                    intOptionSelect = menuMantGrados.show()
                    if intOptionSelect == 1: #Crear Grados
                        crearGrados()
                    elif intOptionSelect == 2: #Modificar Grados
                        modificarGrados()
                    elif intOptionSelect == 3: #Eliminar Grados
                        eliminarGrados()
                    else:
                        break
            else:
                break
    else:
        break

