from connection.conn import Connection
import PySimpleGUI as sg
from Semestres import Semestres
from tabulate import tabulate
import sys
from termcolor import colored, cprint
# connection = Connection(
#    'mongodb+srv://reyner:pachaqtec@pachaqtec.sdvq7.mongodb.net/pachaqtec?retryWrites=true&w=majority', 'pachacteq')
#print = sg.Print


class Cursos:
    collection = "cursos"

    def __init__(self, nombreCurso, idSemestre):
        self.nombreCurso = nombreCurso
        self.idSemestre = idSemestre

    def ingresarCurso(self, connection):
        connection.insertRegistro(Cursos.collection, {
            'nombreCurso': self.nombreCurso,
            'idPeriodo': self.idSemestre
        })
        print("Se ingresó Curso")

    @staticmethod
    def mostrarCursos(connection, condition=None):
        data = connection.obtenerRegistros(Cursos.collection, condition)
        print("Se mostró Cursos")
        return data

    @staticmethod
    def mostrarCurso(connection, condition=None):
        data = connection.obtenerRegistro(Cursos.collection, condition)
        print("Se mostro Curso")
        return data

    @staticmethod
    def mostrarCursoTabla(connection):
        table = []
        # Primero mostramos la tabla Semestre para que el usuario escriba el semestre al que va a ingresar el Curso
        data = Cursos.mostrarCursos(connection)
        for i in range(len(data)):
            table.append([data[i]["_id"], data[i]["nombreCurso"]])

        print(colored('Tabla de Cursos', 'yellow',
                      attrs=['reverse', 'blink']))
        print(tabulate(table, headers=[
            "ID Curso", "Nombre Curso"], tablefmt='fancy_grid'))
        input("Presione alguna tecla para Continuar")

    @staticmethod
    def updateCurso(connection, condition, change):
        connection.actualizarRegistro(Cursos.collection, condition, change)
        print("Se actualizó Curso")

    @staticmethod
    def eliminarCurso(connection, condition):
        connection.eliminarRegistro(Cursos.collection, condition)
        print("Se eliminó Curso")

    @staticmethod
    def transformToObject(**kwargs):
        return kwargs

    @staticmethod
    def ingresarCursoMenu(connection):
        ingreso = True
        while(ingreso):
            table = []
            # Primero mostramos la tabla Semestre para que el usuario escriba el semestre al que va a ingresar el Curso
            data = Semestres.mostrarSemestres(connection)
            for i in range(len(data)):
                table.append([data[i]["_id"], data[i]["desSemestre"]])

            print(colored('Tabla de Semestres', 'yellow',
                          attrs=['reverse', 'blink']))
            print(tabulate(table, headers=[
                  "Id Semestre", "Nombre Semestre"], tablefmt='fancy_grid'))

            # Generamos un simple GUI para ingresar la data

            layout = [
                [sg.Text('Ingrese Curso')],
                [sg.Text('Nombre del Curso', size=(15, 1)), sg.InputText()],
                [sg.Text('Nombre del Semestre', size=(15, 1)), sg.InputText()],
                [sg.Submit()]
            ]
            window = sg.Window("Ingreso de Curso", layout)
            event, values = window.read()
            window.close()

            # Nombre del Semestre a su valor id
            checkExist = Semestres.mostrarSemestre(
                connection, {'desSemestre': values[1]})

            if not checkExist:
                print(colored('Ingrese de nuevo. Nombre de Semestre no encontrado', 'red',
                              attrs=['reverse', 'blink']))
            else:
                values[2] = checkExist["_id"]  # actualizamos el _id
                return values

    @staticmethod
    def borraCursoMenu(connection):
        ingreso = True
        while(ingreso):
            table = []
            # Primero mostramos la tabla Cursos para que el usuario seleccione lo que va a borrar
            data = Cursos.mostrarCursos(connection)
            for i in range(len(data)):
                table.append([data[i]["_id"], data[i]["nombreCurso"]])

            print(colored('Tabla de Cursos. ¿Cual va a borrar?', 'yellow',
                          attrs=['reverse', 'blink']))
            print(tabulate(table, headers=[
                  "Id Curso", "Nombre de Curso"], tablefmt='fancy_grid'))

            # Generamos un simple GUI para ingresar la data

            layout = [
                [sg.Text('Ingrese Curso a Eliminar')],
                [sg.Text('Nombre del Curso', size=(15, 1)), sg.InputText()],
                [sg.Submit()]
            ]
            window = sg.Window("Eliminar Curso", layout)
            event, values = window.read()
            window.close()

            idCurso = connection.obtenerRegistro(
                "cursos", {'nombreCurso': values[0]})

            if idCurso == None:
                print("Intente de nuevo. Nombre de Curso no existe")

            else:
                id_ = idCurso['_id']
                connection.eliminarRegistro("cursos", {'_id': id_})
                print("Registro Eliminado")
                ingreso = False
