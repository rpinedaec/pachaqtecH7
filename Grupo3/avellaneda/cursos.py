import utils
#clase cursos
class cursos:
  __log = utils.log("cursos")
  def __init__(self, idcursos, nombrecurso):
    self.idcursos = idcursos
    self.nombrecurso = nombrecurso
    
  def toDic(self):
    d = {
      "idcursos": self.idcursos,
      "nombrecurso": self.nombrecurso 
    }
    return d
    