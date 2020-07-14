from connection.conn import Connection

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
    def elliminarCurso(connection, condition):
        connection.eliminarRegistro(Cursos.collection, condition)
        print("Se eliminó Curso")

    @staticmethod
    def transformToObject(**kwargs):
        return kwargs
