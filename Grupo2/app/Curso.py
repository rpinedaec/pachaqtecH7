class Curso:
    def __init__(self, nombre):
        self.nombreCurso = nombre

    def dictCurso(self):
        e = {
            'nombreCurso': self.nombreCurso,
        }
        return e