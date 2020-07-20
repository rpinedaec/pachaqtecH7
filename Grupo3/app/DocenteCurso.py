import utils
#clase docente cursos
class docenteCurso:
    __log = utils.log("DocenteCursos")
    def __init__(self, IdDocenteCurso, Docente, Curso, Salon):
        self.IdDocenteCurso = IdDocenteCurso
        self.Docente = Docente
        self.Curso = Curso
        self.Salon = Salon

    def toDic(self):
        d = {
            "IdDocenteCurso": self.IdDocenteCurso,
            "Docente": self.Docente, 
            "Curso": self.Curso,
            "Salon": self.Salon 
        }
        return d

