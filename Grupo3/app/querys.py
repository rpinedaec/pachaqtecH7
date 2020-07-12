class Querys:

    #Alumno
    def ListarAllAlumno(self):
        query = "SELECT * FROM alumnos;"
        return query

    def ListarIdAlumno(self, Id):
        query = "SELECT * FROM alumnos where idalumnos = '"+Id+"'"
        return query

    def InsertAlumno (self, Nombre, Apellido, Correo, Fechanac):
        query = "INSERT INTO alumnos (nombrealumno, apellidoalumno, correoalumno, nacalumno) VALUES ('"+Nombre+"', '"+Apellido+"', '"+Correo+"', '"+Fechanac+"');"
        return query