from connection.conn import Connection
import PySimpleGUI as sg
from Semestres import Semestres
from tabulate import tabulate
connection = Connection(
    'mongodb+srv://reyner:pachaqtec@pachaqtec.sdvq7.mongodb.net/pachaqtec?retryWrites=true&w=majority', 'pachacteq')


class Cursos:
    collection = "cursos"

    def __init__(self, nombreCurso, idProfesor, idSemestre):
        self.nombreCurso = nombreCurso
        self.idProfesor = idProfesor
        self.idSemestre = idSemestre

    def ingresarCurso(self, connection):
        connection.insertRegistro(Cursos.collection, {
            'nombreCurso': self.nombreCurso,
            'idProfesor': self.idProfesor,
            'idSemestre': self.idSemestre
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
    def ingresarCursoMain(connection):
        table = []
        # Primero mostramos la tabla Semestre para que el usuario escriba el semestre al que va a ingresar el Curso
        data = Semestres.mostrarSemestres(connection)
        for i in range(data):
            table.append([data[i]["_id"], data[i]["desSemestre"]])

        print(tabulate(table, headers=["Id Semestre", "Nombre Semestre"]))

        # Generamos un simple GUI para ingresar la data

        layout = [
            [sg.Text('Ingrese Curso')],
            [sg.Text('Nombre del Curso', size=(15, 1)), sg.InputText()],
            [sg.Text('Nombre del Semestre', size=(15, 1)), sg.InputText()],
            [sg.Submit()]
        ]
        window = sg.Window("Ingreso de Curso", layout)
        event, values = window.read()

        # Nombre del Semestre a su valor id
        checkExist = Semestres.mostrarSemestre(
            connection, {'desSemestre': values[2]})
        window.close()
        if not checkExist:
            return False
        else:
            values[2] = checkExist["_id"]  # actualizamos el _id
            return values
