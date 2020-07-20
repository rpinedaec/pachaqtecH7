import utils
#clase alumno cursos
class notasAlumno:
    __log = utils.log("AlumnoNotas")
    def __init__(self, IdAlumnoCurso, Matricula, Curso, Nota):
        self.IdAlumnoCurso = IdAlumnoCurso
        self.Matricula = Matricula
        self.Curso = Curso
        self.Nota = Nota

    def toDic(self):
        d = {
            "IdAlumnoCurso": self.IdAlumnoCurso,
            "Matricula": self.Matricula, 
            "Curso": self.Curso,
            "Nota": self.Nota
        }
        return d