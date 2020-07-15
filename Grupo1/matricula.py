from Cursos import Cursos
from pymongo import MongoClient, errors
from pprint import PrettyPrinter
from connection.conn import Connection


connection = Connection(
    'mongodb+srv://reyner:pachaqtec@pachaqtec.sdvq7.mongodb.net/pachaqtec?retryWrites=true&w=majority', 'pachacteq')

values = Cursos.ingresarCursoMenu(connection)
curso = Cursos(values[0], values[2])
curso.ingresarCurso(connection)  # Ingresa hacia la mongodb
