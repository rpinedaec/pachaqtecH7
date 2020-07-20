import utils
#Clase matricula
class matricula:
  __log = utils.log("matricula")    
  def __init__(self, idmatricula, alumno, periodo):
    self.idmatricula = idmatricula
    self.alumno = alumno
    self.periodo = periodo

  def toDic(self):
    d = {
      "idmatricula": self.idmatricula,
      "alumno": self.alumno,
      "periodo": self.periodo      
    }
    return d
    