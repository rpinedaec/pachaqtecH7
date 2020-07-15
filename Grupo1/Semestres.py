from connection.conn import Connection
import PySimpleGUI as sg


class Semestres:
    collection = "semestres"

    def __init__(self, descSemestre):
        self.descSemestre = descSemestre

    def ingresarSemestre(self, connection):
        connection.insertRegistro(Semestres.collection, {
            'descSemestre': self.descSemestre
        })
        #print("Se ingresó Semestre")

    @staticmethod
    def mostrarSemestres(connection, condition=None):
        data = connection.obtenerRegistros(Semestres.collection, condition)
        #print("Se mostró Semestre")
        return data

    @staticmethod
    def mostrarSemestre(connection, condition=None):
        data = connection.obtenerRegistro(Semestres.collection, condition)
        #print("Se mostro Semestre")
        return data

    @staticmethod
    def updateSemestre(connection, condition, change):
        connection.actualizarRegistro(Semestres.collection, condition, change)
        #print("Se actualizó Semestre")

    @staticmethod
    def eliminarSemestre(connection, condition):
        connection.eliminarRegistro(Semestres.collection, condition)
        #print("Se eliminó Semestre")

    @staticmethod
    def transformToObject(**kwargs):
        return kwargs
