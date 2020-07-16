from Cursos import Cursos
import sys
from Alumnos import Alumnos
from Notas import Notas
from pymongo import MongoClient, errors
from pprint import PrettyPrinter
from connection.conn import Connection
import PySimpleGUI as sg
from termcolor import colored, cprint
import colorama
from salon import *
from logica import *
from connection.conn import Connection
from Profesores_ import Profesores
import gc

import subprocess
subprocess.call('', shell=True)

connection = Connection(
    'mongodb+srv://reyner:pachaqtec@pachaqtec.sdvq7.mongodb.net/pachaqtec?retryWrites=true&w=majority', 'pachacteq')

program = True


def cprintInfo(toPrint):
    return print(colored(toPrint, 'yellow',
                          attrs=['reverse', 'blink']))


while(program):

    layout = [
        [sg.Text('Ingrese Opcion')],
        [sg.Text('1. Ingresar a Menu Alumnos')],
        [sg.Text('2. Ingresar a Menu Salones')],
        [sg.Text('3. Ingresar al Menu Profesores')],
        [sg.Text('4. Ingresar al Menu Cursos')],
        [sg.Text('5. Ingresar al Menu Notas')],
        [sg.Text('6. Listar Alumnos')],
        [sg.Text('7. Avanzado 1: Listar a los Profesor ..')],
        [sg.Text('8. Avanzado 2: Enlistar Alumnos ...')],
        [sg.Text('9. Avanzado 3: Enviar Reporte ...')],
        [sg.Text('10. Terminar Programa')],
        [sg.Text('Ingrese opcion',
                 size=(15, 1)), sg.InputText()],
        [sg.Submit()]
    ]

    window = sg.Window("Ingreso de Curso", layout)
    event, values = window.read()
    window.close()
    layout = None
    window = None
    gc.collect()
    value = int(values[0])
    if value == 1:  # Menu Alumnos
        entered = True
        while(entered):
            cprintInfo("1. Crear Alumno")
            cprintInfo("2. Eliminar Alumno")
            cprintInfo("3. Mostrar Alumno")
            cprintInfo("4. Salir Alumno")
            value = int(input("Ingrese una opción : "))
            if value == 1:
                values = Alumnos.ingresarCursoMenu(connection)
                alumno = Alumnos(values[0], values[1], values[2], values[4])
                alumno.ingresarAlumno(connection)  # Ingresa hacia la mongodb
            elif value == 2:
                Alumnos.borraAlumnoMenu(connection)
            elif value == 3:
                Alumnos.mostrarAlumnoTabla(connection)
            elif value == 4:
                entered = False
            else:
                pass

    elif value == 2:  # Menu Salones
        mantenimiento_salones()
    elif value == 3:  # Menu Profesores
        entered = True
        while(entered):
            cprintInfo("1. Crear Profesor")
            cprintInfo("2. Eliminar Profesor")
            cprintInfo("3. Mostrar Profesores")
            cprintInfo("4. Salir Menu")
            value = int(input("Ingrese una opción : "))
            if value == 1:
                values = Profesores.ingresarProfesorMenu(connection)
                profesor = Profesores(
                    values[0], values[1], values[2], values[4])
                # Ingresa hacia la mongodb
                profesor.ingresarProfesor(connection)
            elif value == 2:
                Profesores.borrarProfesorMenu(connection)
            elif value == 3:
                Profesores.mostrarProfesoresTabla(connection)
            elif value == 4:
                entered = False
            else:
                pass

    elif value == 4:  # Menu Cursos
        entered = True
        while(entered):
            cprintInfo("1. Crear Curso")
            cprintInfo("2. Eliminar Curso")
            cprintInfo("3. Mostrar Cursos")
            cprintInfo("4. Salir Menu")
            value = int(input("Ingrese una opción : "))
            if value == 1:
                values = Cursos.ingresarCursoMenu(connection)
                curso = Cursos(values[0], values[2])
                curso.ingresarCurso(connection)  # Ingresa hacia la mongodb
            elif value == 2:
                Cursos.borraCursoMenu(connection)
            elif value == 3:
                Cursos.mostrarCursoTabla(connection)
            elif value == 4:
                entered = False
            else:
                pass

    elif value == 5:  # Menu Notas
        entered = True
        while(entered):
            cprintInfo("1. Insertar Nota")
            cprintInfo("2. Eliminar Nota")
            cprintInfo("3. Mostrar Notas")
            cprintInfo("4. Salir Menu")
            value = int(input("Ingrese una opción : "))
            if value == 1:
                values = Notas.ingresarNotaMenu(connection)
                nota = Notas(values[0], values[5], values[4],int(values[3]))
                nota.ingresarNota(connection)  # Ingresa hacia la mongodb
                cprint("Se ingreso la Nota")
            elif value == 2:
                Notas.borrarNotaMenu(connection)
            elif value == 3:
                Notas.mostrarNotaTabla(connection)
            elif value == 4:
                entered = False
            else:
                pass

    elif value == 6:  # Listar Alumnos
        pass
    elif value == 7:  # Avanzado 1
        entered = True
        while(entered):
            cprintInfo("Listar Profesores ....")
            cprintInfo("Ingresar nombre de Profesor para listar")
            table = []
            data = Profesores.mostrarProfesores(connection)
            for i in range(len(data)):
                table.append([data[i]["_id"], data[i]["nombreProfesor"]])

            print(colored('Tabla de Profesores', 'yellow',
                          attrs=['reverse', 'blink']))
            print(tabulate(table, headers=[
                "Id Curso", "Nombre Profesor"], tablefmt='fancy_grid'))
            print(colored('Ingresar un Profesor:', 'yellow',
                          attrs=['reverse', 'blink']))
            nombreProfesor = input()
            checkProfesor = connection.obtenerRegistro(
                "profesores", {'nombreProfesor': nombreProfesor})
            if not checkProfesor:
                cprintInfo("Profesor no encontrado. Intente de nuevo")

            else:
                listarProfesores(nombreProfesor, connection)
                input("Presione una tecla para continuar")
                entered = False

    elif value == 8:  # Avanzado 2
        entered = True
        while(entered):
            cprintInfo("Listar Alumnos ....")
            cprintInfo("Ingresar Alumno de Profesor para listar")
            input("Presione una tecla para continuar")
            table = []
            data = Alumnos.mostrarAlumnos(connection)
            for i in range(len(data)):
                table.append([data[i]["_id"], data[i]["nombreAlumno"]])

            print(colored('Tabla de Alumnos', 'yellow',
                          attrs=['reverse', 'blink']))
            print(tabulate(table, headers=[
                "Id Curso", "Nombre Alumno"], tablefmt='fancy_grid'))
            print(colored('Ingresar un nombre:', 'yellow',
                          attrs=['reverse', 'blink']))
            nombreAlumno = input()
            checkAlumno = connection.obtenerRegistro(
                "alumnos", {'nombreAlumno': nombreAlumno})
            if not checkAlumno:
                cprintInfo("Alumno no encontrado. Intente de nuevo")

            else:
                listarAlumnos(nombreAlumno, connection)
                input("Presione una tecla para continuar")
                entered = False
    elif value == 9:  # Avanzado 3
        entered = True
        while(entered):
            cprintInfo("Listar Salones , promedio por curso etc ....")
            cprintInfo("Ingresar nombre de Salon para listar")
            table = []
            data = connection.obtenerRegistros("salones")
            for i in range(len(data)):

                table.append([data[i]["_id"], data[i]["nombreSalon"]])

            print(colored('Tabla de Salones', 'yellow',
                          attrs=['reverse', 'blink']))
            print(tabulate(table, headers=[
                "Id Salon", "Nombre Salon"], tablefmt='fancy_grid'))
            print(colored('Ingresar un nombre del Salon para mostrar su promedio:', 'yellow',
                          attrs=['reverse', 'blink']))
            nombreSalon = input()
            checkSalon = connection.obtenerRegistro(
                "salones", {'nombreSalon': nombreSalon})
            if not checkSalon:
                cprintInfo("Salon no encontrado. Intente de nuevo")

            else:
                reporte2(nombreSalon, connection)
                input("Presione una tecla para continuar")
                entered = False
        pass

    elif value == 10:
        connection.cerrarConexion()
        sys.exit()
    else:
        pass
