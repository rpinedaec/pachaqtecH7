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

    ####INICIO CRUD DOCENTE####
    #Query Ingresar Nuevo Docente
    def InsertDocente (self, Nombre, Dni, Correo, Fechanac):
        query = "INSERT INTO docentes (nombredocente, dnidocente, correodocente, nacdocente) VALUES ('"+Nombre+"','"+Dni+"','"+Correo+"','"+Fechanac+"');"
        return query
    
    #Query Listar Todos los docentes Registrados
    def ListarAllDocentes(self):
        query = "SELECT * FROM docentes;"
        return query
    
    #Query Actualizar Docentes
    def ModificarDocente (self,  Nombre, Dni, Correo, Fechanac, IdDocente):
        query = "UPDATE docentes SET nombredocente = '"+Nombre+"', dnidocente = '"+Dni+"', correodocente = '"+Correo+"', nacdocente = '"+str(Fechanac)+"' WHERE iddocentes = '"+str(IdDocente)+"';"
        return query
    
    #Query Busca Docente por ID
    def BuscarDocente(self, Id):
        query = f"SELECT * FROM docentes where iddocentes = '{Id}'"
        return query

    #Query Elimnia Docente Seleccionando el ID del Docente
    def EliminarDocente(self, IdDocente):
        query = "DELETE FROM docentes WHERE iddocentes = '"+str(IdDocente)+"';"
        return query
    ####FIN CRUD DOCENTE####