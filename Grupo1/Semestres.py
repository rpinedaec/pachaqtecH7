from connection.conn import Connection
import PySimpleGUI as sg
import sys
from termcolor import colored, cprint


class Semestres:
    collection = "semestres"

    def __init__(self, descSemestre):
        self.descSemestre = descSemestre

    def ingresarSemestre(self, connection):
        connection.insertRegistro(Semestres.collection, {
            'descSemestre': self.descSemestre
        })
        # print("Se ingresó Semestre")

    @staticmethod
    def mostrarSemestres(connection, condition=None):
        data = connection.obtenerRegistros(Semestres.collection, condition)
        # print("Se mostró Semestre")
        return data

    @staticmethod
    def mostrarSemestre(connection, condition=None):
        data = connection.obtenerRegistro(Semestres.collection, condition)
        # print("Se mostro Semestre")
        return data

    @staticmethod
    def updateSemestre(connection, condition, change):
        connection.actualizarRegistro(Semestres.collection, condition, change)
        # print("Se actualizó Semestre")

    @staticmethod
    def eliminarSemestre(connection, condition):
        connection.eliminarRegistro(Semestres.collection, condition)
        # print("Se eliminó Semestre")

    @staticmethod
    def transformToObject(**kwargs):
        return kwargs

    @staticmethod
    def ingresarSemestreMenu(connection):
        ingreso = True
        while(ingreso):
            table = []
            # Primero mostramos la tabla Semestre para que el usuario escriba el semestre al que va a ingresar el Curso
            # data = Semestres.mostrarSemestres(connection)
            # for i in range(len(data)):
            #     table.append([data[i]["_id"], data[i]["desSemestre"]])

            # print(colored('Tabla de Semestres', 'yellow',
            #               attrs=['reverse', 'blink']))
            # print(tabulate(table, headers=[
            #       "Id Semestre", "Nombre Semestre"], tablefmt='fancy_grid'))

            # Generamos un simple GUI para ingresar la data

            layout = [
                [sg.Text('Ingrese Periodo')],
                [sg.Text('Descripción de Semestre',
                         size=(15, 1)), sg.InputText()],
                [sg.Submit()]
            ]
            window = sg.Window("Ingreso de Periodo", layout)
            event, values = window.read()
            window.close()
            print(colored('Se ingreso Periodo',
                          'yellow', attrs=['reverse', 'blink']))

            print(colored('Tabla de Semestres',
                          'yellow', attrs=['reverse', 'blink']))

            data = Semestres.mostrarSemestres(connection)
            for i in range(len(data)):
                table.append([data[i]["_id"], data[i]["desSemestre"]])

            return values
            # # Nombre del Semestre a su valor id
            # checkExist = Semestres.mostrarSemestre(
            #     connection, {'desSemestre': values[1]})

            # if not checkExist:
            #     print(colored('Ingrese de nuevo. Nombre de Semestre no encontrado', 'red',
            #                   attrs=['reverse', 'blink']))
            # else:
            #     values[2] = checkExist["_id"]  # actualizamos el _id
            #     return values
