from connection.conn import Connection
import PySimpleGUI as sg
from Semestres import Semestres
from tabulate import tabulate
import sys
from termcolor import colored, cprint
# connection = Connection(
#    'mongodb+srv://reyner:pachaqtec@pachaqtec.sdvq7.mongodb.net/pachaqtec?retryWrites=true&w=majority', 'pachacteq')
#print = sg.Print


class Alumnos:
    collection = "alumnos"

    def __init__(self, nombreAlumno, edad, correoAlumno, idSalon):
        self.nombreAlumno = nombreAlumno
        self.edad = edad
        self.correoAlumno = correoAlumno
        self.idSalon = idSalon

    def ingresarAlumno(self, connection):
        connection.insertRegistro(Alumnos.collection, {
            'nombreAlumno': self.nombreAlumno,
            'edad': self.edad,
            'correoAlumno': self.correoAlumno
        })
        print("Se ingresó Alumno")

    @staticmethod
    def mostrarAlumnos(connection, condition=None):
        data = connection.obtenerRegistros("alumnos", condition)
        print("Se mostró Alumnos")
        return data

    @staticmethod
    def mostrarAlumno(connection, condition=None):
        data = connection.obtenerRegistro(Alumnos.collection, condition)
        print("Se mostro Alumno")
        return data

    @staticmethod
    def mostrarAlumnoTabla(connection):
        table = []
        # Primero mostramos la tabla Semestre para que el usuario escriba el semestre al que va a ingresar el Curso
        data = Alumnos.mostrarAlumnos(connection)

        for i in range(len(list(data))):
            table.append([data[i]["_id"], data[i]["nombreAlumno"],
                          data[i]["edad"], data[i]["correoAlumno"]])

        print(colored('Tabla de Cursos', 'yellow',
                      attrs=['reverse', 'blink']))
        print(tabulate(table, headers=[
            "ID Curso", "Nombre Curso"], tablefmt='fancy_grid'))
        input("Presione alguna tecla para Continuar")

    @staticmethod
    def updateAlumno(connection, condition, change):
        connection.actualizarRegistro(Alumnos.collection, condition, change)
        print("Se actualizó Alumno")

    @staticmethod
    def eliminarALumno(connection, condition):
        connection.eliminarRegistro(Alumnos.collection, condition)
        print("Se eliminó Alumno")

    @staticmethod
    def transformToObject(**kwargs):
        return kwargs

    @staticmethod
    def ingresarCursoMenu(connection):
        ingreso = True
        while(ingreso):
            table = []
            # Primero mostramos la tabla Semestre para que el usuario escriba el semestre al que va a ingresar el Curso
            data = connection.obtenerRegistros('salones')
            for i in range(len(data)):
                table.append([data[i]["_id"], data[i]["nombreSalon"]])

            print(colored('Tabla de Salones. Escoger a que salón pertenecerá el Alumno', 'yellow',
                          attrs=['reverse', 'blink']))
            print(tabulate(table, headers=[
                  "ID salon", "Nombre Salon"], tablefmt='fancy_grid'))

            # Generamos un simple GUI para ingresar la data

            layout = [
                [sg.Text('Ingrese Alumno')],
                [sg.Text('Nombre del Alumno', size=(15, 1)), sg.InputText()],
                [sg.Text('Edad Alumno', size=(15, 1)), sg.InputText()],
                [sg.Text('Correo Alumno', size=(15, 1)), sg.InputText()],
                [sg.Text('Nombre del Salón', size=(15, 1)), sg.InputText()],
                [sg.Submit()]
            ]
            window = sg.Window("Ingreso del Alumno", layout)
            event, values = window.read()
            window.close()

            # Comprobamos si el nombre de salon existe
            checkExist = connection.obtenerRegistro(
                "salones", {'nombreSalon': values[3]})

            if checkExist == None:
                print(colored('Ingrese de nuevo. Nombre de Salon no encontrado', 'red',
                              attrs=['reverse', 'blink']))
            else:
                values[4] = checkExist["_id"]  # actualizamos el _id
                return values

    @staticmethod
    def borraAlumnoMenu(connection):
        ingreso = True
        while(ingreso):
            table = []
            # Primero mostramos la tabla Cursos para que el usuario seleccione lo que va a borrar
            data = Alumnos.mostrarAlumnos(connection)
            for i in range(len(data)):
                table.append([data[i]["_id"], data[i]["nombreAlumno"]])

            print(colored('Tabla de Cursos. ¿Cual va a borra?', 'yellow',
                          attrs=['reverse', 'blink']))
            print(tabulate(table, headers=[
                  "Id Alumno", "Nombre de Alumno"], tablefmt='fancy_grid'))

            # Generamos un simple GUI para ingresar la data

            layout = [
                [sg.Text('Ingrese nombre Alumno a Eliminar')],
                [sg.Text('Nombre del Alumno', size=(15, 1)), sg.InputText()],
                [sg.Submit()]
            ]
            window = sg.Window("Eliminar Alumno", layout)
            event, values = window.read()
            window.close()

            idCurso = connection.obtenerRegistro(
                "alumnos", {'nombreAlumno': values[0]})

            if idCurso == None:
                print("Intente de nuevo. Nombre de Curso no existe")

            else:
                id_ = idCurso['_id']
                connection.eliminarRegistro("alumnos", {'_id': id_})
                print("Registro Eliminado")
                ingreso = False
