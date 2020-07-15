#clase docentes
class docentes:
  __log = utils.log("docentes")
  def __init__(self, iddocentes, nombredocente, dnidocente, correodocente, nacdocente):
    self.iddocentes = iddocentes
    self.nombredocente = nombredocente
    self.dnidocente = dnidocente
    self.correodocente = correodocente
    self.nacdocente = nacdocente
    
  def toDic(self):
    d = {
      "idAlumno": self.idalumnos,
      "nombrealumno": self.nombrealumno,
      "apellidoalumno": self.apellidoalumno,
      "correoalumno": self.correoalumno,
      "nacalumno": self.nacalumno
    }
    return d
    
    