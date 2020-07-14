from connection.conn import Connection

connection = Connection(
    'mongodb+srv://reyner:pachaqtec@pachaqtec.sdvq7.mongodb.net/pachaqtec?retryWrites=true&w=majority', 'pachacteq')


class Cursos:
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
        data = connection.obtenerRegistros(Cursos.collection, condition)
        print("Se mostró Nota")
        return data

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
