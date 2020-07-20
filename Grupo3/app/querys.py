class Querys:

#  █████  ██      ██    ██ ███    ███ ███    ██  ██████  
# ██   ██ ██      ██    ██ ████  ████ ████   ██ ██    ██ 
# ███████ ██      ██    ██ ██ ████ ██ ██ ██  ██ ██    ██ 
# ██   ██ ██      ██    ██ ██  ██  ██ ██  ██ ██ ██    ██ 
# ██   ██ ███████  ██████  ██      ██ ██   ████  ██████ 

    def ListarAllAlumno(self):
        query = "SELECT * FROM alumnos;"
        return query

    def BuscarAlumno(self, Id):
        query = f"SELECT * FROM alumnos where idalumnos = '{Id}'"
        return query

    def InsertAlumno(self, Nombre, Apellido, Correo, Fechanac):
        query = "INSERT INTO alumnos (nombrealumno, apellidoalumno, correoalumno, nacalumno) VALUES ('"+Nombre+"', '"+Apellido+"', '"+Correo+"', '"+Fechanac+"');"
        return query

    def ModificarAlumno(self, Nombre, Apellido, Correo, FechaNac, IdAlumno):
        query = "UPDATE alumnos SET nombrealumno = '"+Nombre+"', apellidoalumno = '"+Apellido+"', correoalumno = '"+Correo+"', nacalumno = '"+str(FechaNac)+"' WHERE idalumnos = '"+str(IdAlumno)+"';"
        return query

    def EliminarAlumno(self, Id):
        query = "DELETE FROM alumnos WHERE idalumnos = '"+str(Id)+"'"
        return query



# ██████   ██████   ██████ ███████ ███    ██ ████████ ███████ ███████ 
# ██   ██ ██    ██ ██      ██      ████   ██    ██    ██      ██      
# ██   ██ ██    ██ ██      █████   ██ ██  ██    ██    █████   ███████ 
# ██   ██ ██    ██ ██      ██      ██  ██ ██    ██    ██           ██ 
# ██████   ██████   ██████ ███████ ██   ████    ██    ███████ ███████ 
    
    def ListarAllDocente(self):
        query = "SELECT * FROM docentes;"
        return query

    def BuscarDocente(self, Id):
        query = f"SELECT * FROM docentes where iddocentes = '{Id}'"
        return query

    def InsertDocente(self, Nombre, Dni, Correo, Fechanac):
        query = "INSERT INTO docentes (nombredocente, dnidocente, correodocente, nacdocente) VALUES ('"+Nombre+"', '"+Dni+"', '"+Correo+"', '"+Fechanac+"');"
        return query

    def ModificarDocente(self, Nombre, Dni, Correo, FechaNac, IdDocente):
        query = "UPDATE docentes SET nombredocente = '"+Nombre+"', dnidocente = '"+Dni+"', correodocente = '"+Correo+"', nacdocente = '"+str(FechaNac)+"' WHERE iddocentes = '"+str(IdDocente)+"';"
        return query

    def EliminarDocente(self, Id):
        query = "DELETE FROM docentes WHERE iddocentes = '"+str(Id)+"'"
        return query



# ███████  █████  ██       ██████   ██████  ███    ██ ███████ ███████ 
# ██      ██   ██ ██      ██    ██ ██    ██ ████   ██ ██      ██      
# ███████ ███████ ██      ██    ██ ██    ██ ██ ██  ██ █████   ███████ 
#      ██ ██   ██ ██      ██    ██ ██    ██ ██  ██ ██ ██           ██ 
# ███████ ██   ██ ███████  ██████   ██████  ██   ████ ███████ ███████

    def ListarAllSalones(self):
        query = "SELECT * FROM salones;"
        return query

    def BuscarSalon(self, Id):
        query = f"SELECT * FROM salones where idsalones = '{Id}'"
        return query

    def InsertSalon(self, Nombre):
        query = "INSERT INTO salones (nombresalon) VALUES ('"+Nombre+"');"
        return query

    def ModificarSalon(self, Nombre, IdSalon):
        query = "UPDATE salones SET nombresalon = '"+Nombre+"' WHERE idsalones = '"+str(IdSalon)+"';"
        return query

    def EliminarSalon(self, Id):
        query = "DELETE FROM salones WHERE idsalones = '"+str(Id)+"'"
        return query



#  ██████ ██    ██ ██████  ███████  ██████  ███████ 
# ██      ██    ██ ██   ██ ██      ██    ██ ██      
# ██      ██    ██ ██████  ███████ ██    ██ ███████ 
# ██      ██    ██ ██   ██      ██ ██    ██      ██ 
#  ██████  ██████  ██   ██ ███████  ██████  ███████

    def ListarAllCursos(self):
        query = "SELECT * FROM cursos;"
        return query

    def BuscarCurso(self, Id):
        query = f"SELECT * FROM cursos where idcursos = '{Id}'"
        return query

    def InsertCurso(self, Nombre):
        query = "INSERT INTO cursos (nombrecurso) VALUES ('"+Nombre+"');"
        return query

    def ModificarCurso(self, Nombre, IdCurso):
        query = "UPDATE cursos SET nombrecurso = '"+Nombre+"' WHERE idcursos = '"+str(IdCurso)+"';"
        return query

    def EliminarCurso(self, Id):
        query = "DELETE FROM cursos WHERE idcursos = '"+str(Id)+"'"
        return query



# ██████  ███████ ██████  ██  ██████  ██████   ██████      ███████ ███████  ██████  ██████  ██       █████  ██████  
# ██   ██ ██      ██   ██ ██ ██    ██ ██   ██ ██    ██     ██      ██      ██      ██    ██ ██      ██   ██ ██   ██ 
# ██████  █████   ██████  ██ ██    ██ ██   ██ ██    ██     █████   ███████ ██      ██    ██ ██      ███████ ██████  
# ██      ██      ██   ██ ██ ██    ██ ██   ██ ██    ██     ██           ██ ██      ██    ██ ██      ██   ██ ██   ██ 
# ██      ███████ ██   ██ ██  ██████  ██████   ██████      ███████ ███████  ██████  ██████  ███████ ██   ██ ██   ██ 

    def ListarAllPeriodos(self):
        query = "SELECT * FROM periodoEscolar;"
        return query

    def BuscarPeriodo(self, Id):
        query = f"SELECT * FROM periodoEscolar where idperiodoEscolar = '{Id}'"
        return query

    def InsertPeriodo(self, Nombre):
        query = "INSERT INTO periodoEscolar (desperiodo) VALUES ('"+Nombre+"');"
        return query

    def ModificarPeriodo(self, Nombre, IdPeriodo):
        query = "UPDATE periodoEscolar SET desperiodo = '"+Nombre+"' WHERE idperiodoEscolar = '"+str(IdPeriodo)+"';"
        return query

    def EliminarPeriodo(self, Id):
        query = "DELETE FROM periodoEscolar WHERE idperiodoEscolar = '"+str(Id)+"'"
        return query



# ███    ██  ██████  ████████  █████  ███████ 
# ████   ██ ██    ██    ██    ██   ██ ██      
# ██ ██  ██ ██    ██    ██    ███████ ███████ 
# ██  ██ ██ ██    ██    ██    ██   ██      ██ 
# ██   ████  ██████     ██    ██   ██ ███████ 

    def ListarAllNotas(self):
        query = "SELECT * FROM docentes_has_cursos;"
        return query

    def BuscarNota(self, Nota):
        query = f"SELECT * FROM docentes_has_cursos where nota = '{Nota}'"
        return query

    def InsertNota(self, Nota):
        query = "INSERT INTO docentes_has_cursos (nota) VALUES ('"+Nota+"');"
        return query

    def ModificarNota(self, Nota):
        query = "UPDATE docentes_has_cursos SET nota = '"+Nota+"' WHERE nota = '"+str(Nota)+"';"
        return query

    def EliminarNota(self):
        query = ""
        return query

    #Matricula

    def InsertMatricula(self, IdAlumno, IdPeriodo):
        query = "INSERT INTO matricula (alumnos_idalumnos, periodoEscolar_idperiodoEscolar) VALUES ('"+str(IdAlumno)+"', '"+str(IdPeriodo)+"')"
        return query

    def ListarAllMatricula(self):
        query = "SELECT m.idmatricula, a.nombrealumno, a.apellidoalumno, pe.desperiodo FROM matricula m INNER JOIN alumnos a ON m.alumnos_idalumnos = a.idalumnos INNER JOIN periodoescolar pe ON pe.idperiodoEscolar = m.periodoescolar_idperiodoEscolar"
        return query   

    def BuscarMatricula(self, IdMatricula):
        query = "SELECT m.idmatricula, a.nombrealumno, a.apellidoalumno, pe.desperiodo FROM matricula m INNER JOIN alumnos a ON m.alumnos_idalumnos = a.idalumnos INNER JOIN periodoescolar pe ON pe.idperiodoEscolar = m.periodoescolar_idperiodoEscolar WHERE m.idmatricula = '"+str(IdMatricula)+"'"
        return query
    
    def InsertDocenteCurso(self, IdDocente, IdCurso, IdSalon):
        query = "INSERT INTO docentes_has_cursos (docentes_iddocentes, cursos_idcursos, salones_idsalones) VALUES ('"+str(IdDocente)+"', '"+str(IdCurso)+"', '"+str(IdSalon)+"')"
        return query

    def InsertAlumnoCurso(self, IdMatricula, IdCurso):
        query = "INSERT INTO cursos_has_matricula (cursos_idcursos, matricula_idmatricula) VALUES ('"+str(IdCurso)+"', '"+str(IdMatricula)+"')"
        return query

    def ListarDocenteCurso(self):
        query = "SELECT d.iddocentes, d.nombredocente, c.nombrecurso, s.nombresalon FROM docentes_has_cursos dc INNER JOIN cursos c ON dc.cursos_idcursos = c.idcursos INNER JOIN docentes d ON d.iddocentes = dc.docentes_iddocentes INNER JOIN salones s ON s.idsalones = dc.salones_idsalones"
        return query

    def BuscarDocenteCurso(self, IdDocenteCurso):
        query = "SELECT d.nombredocente, c.nombrecurso, s.nombresalon, a.nombrealumno, a.apellidoalumno, cm.nota FROM docentes_has_cursos dc INNER JOIN cursos c ON dc.cursos_idcursos = c.idcursos INNER JOIN docentes d ON d.iddocentes = dc.docentes_iddocentes INNER JOIN salones s ON s.idsalones = dc.salones_idsalones INNER JOIN cursos_has_matricula cm ON cm.cursos_idcursos = c.idcursos INNER JOIN matricula m ON m.idmatricula = cm.matricula_idmatricula INNER JOIN alumnos a ON a.idalumnos = m.alumnos_idalumnos WHERE d.iddocentes = '"+str(IdDocenteCurso)+"';"
        return query

    def ListarAllAlumnoCurso(self):
        query = "SELECT cm.IdCursoMatriculaa, d.nombredocente, c.nombrecurso, s.nombresalon, a.nombrealumno, a.apellidoalumno, cm.nota FROM docentes_has_cursos dc INNER JOIN cursos c ON dc.cursos_idcursos = c.idcursos INNER JOIN docentes d ON d.iddocentes = dc.docentes_iddocentes INNER JOIN salones s ON s.idsalones = dc.salones_idsalones INNER JOIN cursos_has_matricula cm ON cm.cursos_idcursos = c.idcursos INNER JOIN matricula m ON m.idmatricula = cm.matricula_idmatricula INNER JOIN alumnos a ON a.idalumnos = m.alumnos_idalumnos "
        return query

    def BuscarAlumnoCursoNota(self, ID):
        query = "SELECT cm.IdCursoMatriculaa, d.nombredocente, c.nombrecurso, s.nombresalon, a.nombrealumno, a.apellidoalumno, cm.nota FROM docentes_has_cursos dc INNER JOIN cursos c ON dc.cursos_idcursos = c.idcursos INNER JOIN docentes d ON d.iddocentes = dc.docentes_iddocentes INNER JOIN salones s ON s.idsalones = dc.salones_idsalones INNER JOIN cursos_has_matricula cm ON cm.cursos_idcursos = c.idcursos INNER JOIN matricula m ON m.idmatricula = cm.matricula_idmatricula INNER JOIN alumnos a ON a.idalumnos = m.alumnos_idalumnos WHERE cm.idcursomatriculaa = '"+str(ID)+"'"
        return query
        
    def AsignarNota(self, Nota, Id):
        query = "UPDATE cursos_has_matricula SET nota = '"+str(Nota)+"' WHERE IdCursoMatriculaa = '"+str(Id)+"'"
        return query