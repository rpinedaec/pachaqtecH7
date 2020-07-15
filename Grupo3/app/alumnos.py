import utils
#Clase alumnos
class alumnos:
  __log = utils.log("alumnos")
  def __init__(self, idalumnos, nombrealumno, apellidoalumno, correoalumno, nacalumno):
    self.idalumnos = idalumnos
    self.nombrealumno = nombrealumno
    self.apellidoalumno = apellidoalumno
    self.correoalumno = correoalumno
    self.nacalumno = nacalumno

  def toDic(self):
    d = {
      "idAlumno": self.idalumnos,
      "nombrealumno": self.nombrealumno,
      "apellidoalumno": self.apellidoalumno,
      "correoalumno": self.correoalumno,
      "nacalumno": self.nacalumno
    }
    return d
