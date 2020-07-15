import utils
#clase alumno cursos
class alumnoCurso:
    __log = utils.log("AlumnoCursos")
    def __init__(self, IdAlumnoCurso, Matricula, Curso):
        self.IdAlumnoCurso = IdAlumnoCurso
        self.Matricula = Matricula
        self.Curso = Curso

    def toDic(self):
        d = {
            "IdAlumnoCurso": self.IdAlumnoCurso,
            "Matricula": self.Matricula, 
            "Curso": self.Curso
        }
        return d

