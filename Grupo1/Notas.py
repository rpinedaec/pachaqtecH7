from connection.conn import Connection
import PySimpleGUI as sg
from tabulate import tabulate
import sys
from Alumnos import Alumnos
from Cursos import Cursos
from termcolor import colored, cprint


class Notas:
    collection = "notas"

    def __init__(self, descNota, idAlumno, idCurso):
        self.descNota = descNota
        self.idAlumno = idAlumno
        self.idCurso = idCurso

    def ingresarNota(self, connection):
        connection.insertRegistro(Cursos.collection, {
            'descNota': self.descNota,
            'idAlumno': self.idAlumno,
            'idCurso': self.idCurso
        })
        print("Se ingresó Nota")

    @staticmethod
    def mostrarNotas(connection, condition=None):
        data = connection.obtenerRegistros(Notas.collection, condition)
        print("Se mostró Nota")
        return data

    @staticmethod
    def mostrarNotaTabla(connection):
        table = []
        # Primero mostramos la tabla Semestre para que el usuario escriba el semestre al que va a ingresar el Curso
        data = Notas.mostrarNotas(connection)
        for i in range(len(data)):
            table.append(
                [data[i]["_id"], data[i]["descNota"], data[i]["nota"]])

        print(colored('Tabla de Notas', 'yellow',
                      attrs=['reverse', 'blink']))
        print(tabulate(table, headers=[
            "ID Curso", "Nombre Notas", "Nota"], tablefmt='fancy_grid'))
        input("Presione alguna tecla para Continuar")

    @staticmethod
    def mostrarNota(connection, condition=None):
        data = connection.obtenerRegistro(Cursos.collection, condition)
        print("Se mostro Nota")
        return data

    @staticmethod
    def updateNota(connection, condition, change):
        connection.actualizarRegistro(Cursos.collection, condition, change)
        print("Se actualizó Nota")

    @staticmethod
    def elliminarNota(connection, condition):
        connection.eliminarRegistro(Cursos.collection, condition)
        print("Se eliminó Nota")

    @staticmethod
    def transformToObject(**kwargs):
        return kwargs

    @staticmethod
    def ingresarNotaMenu(connection):
        ingreso = True
        while(ingreso):
            print(colored('Se mostrará las tablas de Cursos Y Alumnos para ingresar correctamente la nota', 'yellow',
                          attrs=['reverse', 'blink']))

            input("Presione una tecla para continuar")

            # Mostramos tabla de Cursos
            table = []
            data = Cursos.mostrarCursos(connection)
            for i in range(len(data)):
                table.append([data[i]["_id"], data[i]["nombreCurso"]])

            print(colored('Tabla de Cursos', 'yellow',
                          attrs=['reverse', 'blink']))
            print(tabulate(table, headers=[
                "Id Curso", "Nombre Curso"], tablefmt='fancy_grid'))

            # Mostramos tabla Alumnos
            table = []
            data = Alumnos.mostrarAlumnos(connection)
            for i in range(len(data)):
                table.append([data[i]["_id"], data[i]["nombreAlumno"]])

            print(colored('Tabla de Alumnos', 'yellow',
                          attrs=['reverse', 'blink']))
            print(tabulate(table, headers=[
                "Id Alumno", "Nombre Alumno"], tablefmt='fancy_grid'))

            # Generamos un simple GUI para ingresar la data

            layout = [
                [sg.Text('Ingrese Alumno')],
                [sg.Text('Descripcion de la Nota', size=(15, 1)),
                 sg.InputText()],
                [sg.Text('Nombre del Curso', size=(15, 1)), sg.InputText()],
                [sg.Text('Nombre del Alumno', size=(15, 1)), sg.InputText()],
                [sg.Text('Nota', size=(15, 1)), sg.InputText()],
                [sg.Submit()]
            ]
            window = sg.Window("Ingreso de Alumno", layout)
            event, values = window.read()
            window.close()

            # Verificamos si existe el Curso ingresado
            checkExist = Cursos.mostrarCurso(
                connection, {'nombreCurso': values[1]})

            if not checkExist:
                print(colored('Ingrese de nuevo. Nombre del curso no encontrado', 'red',
                              attrs=['reverse', 'blink']))
            else:
                # Ahora el values[3] tendra el id nuestro curso
                values[4] = checkExist["_id"]
                # Verificamos el ingreso del Alumno
                checkExist = Alumnos.mostrarAlumno(
                    connection, {'nombreAlumno': values[2]})

                if not checkExist:
                    print(colored('Ingrese de nuevo. Nombre del Alumno no encontrado', 'red', attrs=[
                          'reverse', 'blink']))
                else:
                    values[5] = checkExist["_id"]
                    return values

    @staticmethod
    def borrarNotaMenu(connection):

        ingreso = True
        while(ingreso):
            print(colored('Se mostrará las tablas de Notas para escoger cual se va a eliminar', 'yellow',
                          attrs=['reverse', 'blink']))

            input("Presione una tecla para continuar")
            table = []
            # Primero mostramos la tabla Cursos para que el usuario seleccione lo que va a borrar
            data = Notas.mostrarNotas(connection)
            for i in range(len(data)):
                table.append([data[i]["_id"], data[i]["descNota"]])

            print(colored('Tabla de Notas. ¿Cual va a borrar?', 'yellow',
                          attrs=['reverse', 'blink']))
            print(tabulate(table, headers=[
                  "Id Curso", "Desc de Notas"], tablefmt='fancy_grid'))

            # Generamos un simple GUI para ingresar la data

            layout = [
                [sg.Text('Ingrese Nota a Eliminar')],
                [sg.Text('Desc Nota', size=(15, 1)), sg.InputText()],
                [sg.Submit()]
            ]
            window = sg.Window("Eliminar Nota", layout)
            event, values = window.read()
            window.close()

            idCurso = connection.obtenerRegistro(
                "notas", {'descNota': values[0]})

            if idCurso == None:
                print("Intente de nuevo. Nombre de Curso no existe")

            else:
                id_ = idCurso['_id']
                connection.eliminarRegistro("notas", {'_id': id_})
                print("Registro Eliminado")
                ingreso = False
