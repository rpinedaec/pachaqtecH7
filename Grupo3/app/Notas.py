import utils
class Notas:
    __log = utils.log("Notas")
    def __init__ (self, IdAlumnoCurso, Notas):
        self.IdAlumnoCurso = IdAlumnoCurso
        self.Notas = Notas

    def toDic(self):
        d = {
            "IdAlumnoCurso": self.IdAlumnoCurso,
            "Notas": self.Notas 
        }
        return d