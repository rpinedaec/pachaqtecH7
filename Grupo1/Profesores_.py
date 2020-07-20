from connection.conn import Connection
import PySimpleGUI as sg
from tabulate import tabulate
import sys
from Alumnos import Alumnos
from Cursos import Cursos
from termcolor import colored, cprint
import gc

class Profesores:
    collection = "profesores"

    def __init__(self, nombreProfesor, edadProfesor, correoProfesor, idCurso):
        self.nombreProfesor = nombreProfesor
        self.edadProfesor = edadProfesor
        self.correoProfesor = correoProfesor
        self.idCurso = idCurso

    def ingresarProfesor(self, connection):
        connection.insertRegistro(Profesores.collection, {
            'nombreProfesor': self.nombreProfesor,
            'edadProfesor': self.edadProfesor,
            'correoProfesor': self.correoProfesor,
            'idCurso': self.idCurso
        })
        print("Se ingresó Profesor")

    @staticmethod
    def mostrarProfesores(connection, condition=None):
        data = connection.obtenerRegistros(Profesores.collection, condition)
        print("Se mostró Profesores")
        return data

    @staticmethod
    def mostrarProfesoresTabla(connection):
        table = []
        # Primero mostramos la tabla Semestre para que el usuario escriba el semestre al que va a ingresar el Curso
        data = Profesores.mostrarProfesores(connection)
        for i in range(len(data)):
            table.append(
                [data[i]["_id"], data[i]["nombreProfesor"], data[i]["edadProfesor"], data[i]["correoProfesor"], data[i]["idCurso"]])

        print(colored('Tabla de Profesores', 'yellow',
                      attrs=['reverse', 'blink']))
        print(tabulate(table, headers=[
            "ID Profesores", "Nombre Profesores", "Edad Profesores", "Correo Profesor", "ID Curso"], tablefmt='fancy_grid'))
        input("Presione alguna tecla para Continuar")

    @staticmethod
    def mostrarProfesor(connection, condition=None):
        data = connection.obtenerRegistro(Profesores.collection, condition)
        print("Se mostro Profesor")
        return data

    @staticmethod
    def updateProfesor(connection, condition, change):
        connection.actualizarRegistro(Profesores.collection, condition, change)
        print("Se actualizó Profesor")

    @staticmethod
    def elliminarProfesor(connection, condition):
        connection.eliminarRegistro(Profesores.collection, condition)
        print("Se eliminó Profesor")

    @staticmethod
    def transformToObject(**kwargs):
        return kwargs

    @staticmethod
    def ingresarProfesorMenu(connection):
        ingreso = True
        while(ingreso):
            print(colored('Se mostrará las tablas de Cursos para ingresar un Profesor', 'yellow',
                          attrs=['reverse', 'blink']))

            input("Presione una tecla para continuar")

            # Mostramos tabla de Cursos
            table = []
            data = Cursos.mostrarCursos(connection)
            #print(data)
            for i in range(len(data)):
                table.append([data[i]["_id"], data[i]["nombreCurso"]])

            print(colored('Tabla de Cursos', 'yellow',
                          attrs=['reverse', 'blink']))
            print(tabulate(table, headers=[
                "Id Curso", "Nombre Curso"], tablefmt='fancy_grid'))

            # Generamos un simple GUI para ingresar la data

            layout = [
                [sg.Text('Ingrese Profesor:')],
                [sg.Text('Nombre Profesor', size=(15, 1)),
                 sg.InputText()],
                [sg.Text('Edad Profesor', size=(15, 1)), sg.InputText()],
                [sg.Text('Correo Profesor', size=(15, 1)), sg.InputText()],
                [sg.Text('Curso', size=(15, 1)), sg.InputText()],
                [sg.Submit()]
            ]
            window = sg.Window("Ingreso de Profesor", layout)
            event, values = window.read()
            window.close()
            layout = None
            window = None
            gc.collect()

            # Verificamos si existe el Curso ingresado
            checkExist = Cursos.mostrarCurso(
                connection, {'nombreCurso': values[3]})

            if not checkExist:
                print(colored('Ingrese de nuevo. Nombre del curso no encontrado', 'red',
                              attrs=['reverse', 'blink']))
            else:

                values[4] = checkExist["_id"]
                return values

    @staticmethod
    def borrarProfesorMenu(connection):

        ingreso = True
        while(ingreso):
            print(colored('Se mostrará las tablas de Profesores para escoger cual se va a eliminar', 'yellow',
                          attrs=['reverse', 'blink']))

            input("Presione una tecla para continuar")
            table = []
            # Primero mostramos la tabla Cursos para que el usuario seleccione lo que va a borrar

            data = Profesores.mostrarProfesores(connection)
            for i in range(len(data)):
                table.append([data[i]["_id"], data[i]["nombreProfesor"], data[i]
                              ["edadProfesor"], data[i]["correoProfesor"], data[i]["idCurso"]])

            print(colored('Tabla de Profesores', 'yellow',
                          attrs=['reverse', 'blink']))
            print(tabulate(table, headers=[
                "ID Profesores", "Nombre Profesores", "Edad Profesores", "Correo Profesor", "ID Curso"], tablefmt='fancy_grid'))

            # Generamos un simple GUI para ingresar la data

            layout = [
                [sg.Text('Ingrese Profesor a Eliminar')],
                [sg.Text('Nombre Profesor', size=(15, 1)), sg.InputText()],
                [sg.Submit()]
            ]
            window = sg.Window("Eliminar Profesor", layout)
            event, values = window.read()
            window.close()           
            layout = None
            window = None
            gc.collect()

            idCurso = connection.obtenerRegistro(
                "profesores", {'nombreProfesor': values[0]})

            if idCurso == None:
                print("Intente de nuevo. Nombre de Profesor no existe")
                print("Se reinicia la solicitud")
                input("Presione alguna tecla para contiunar")

            else:
                id_ = idCurso['_id']
                connection.eliminarRegistro("profesores", {'_id': id_})
                print("Registro Eliminado")
                ingreso = False
