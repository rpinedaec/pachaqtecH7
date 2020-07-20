class Nota:
    def __init__(self, alumno, periodo, curso, nota):
        self.alumno = alumno
        self.periodo = periodo
        self.curso = curso
        self.nota = nota

    def dictNota(self):
        e = {
            'alumnoNota': self.alumno,
            'periodoNota': self.periodo,
            'cursoNota':self.curso,
            'nota': self.nota
        }
        return e