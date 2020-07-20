class profesor:
    collection = "profesor"

    def __init__(self, nombreProfesor, edadProfesor, correoProfesor, idCurso):
        self.nombreProfesor = nombreProfesor
        self.edadProfesor = edadProfesor
        self.correoProfesor = correoProfesor
        self.idCurso = idCurso
        
    def toDic(self):
        dic={}
        dic= {"nombreProfesor" :self.nombreProfesor,
              "edadProfesor" : self.edadProfesor,
              "correoProfesor": self.correoProfesor,
              "idCurso" : self.idCurso}
        return dic
    
    def ingresarProfesor(self, connection,collection, data):
        connection.insertRegistro(collection,data)
        print("Se ingresó el profesor")

    @staticmethod
    def mostrarProfesores(connection, collection, condition=None):
        data = connection.obtenerRegistros(collection, condition)
        print("Se mostró profesor")
        return data

    @staticmethod
    def mostrarProfesor(connection,collection, condition=None):
        data = connection.obtenerRegistro(collection, condition)
        print("Se mostro profesor")
        return data

    @staticmethod
    def updateProfesor(connection, collection, condition, change):
        connection.actualizarRegistro(collection, condition, change)
        print("Se actualizó Profesor")

    @staticmethod
    def eliminarProfesor(connection, collection, condition):
        connection.eliminarRegistro(collection, condition)
        print("Se eliminó Profesor")

    @staticmethod
    def transformToObject(**kwargs):
        return kwargs
