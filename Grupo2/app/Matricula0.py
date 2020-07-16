class Matricula:
    def __init__(self, alumno, periodo, cursos):
        self.alumno = alumno
        self.periodo = periodo
        self.cursos = cursos

    def dictMatricula(self):
        e = {
            'alumnoMatricula': self.alumno,
            'periodoMatricula': self.periodo,
            'cursoMatricula':self.cursos
        }
        return e