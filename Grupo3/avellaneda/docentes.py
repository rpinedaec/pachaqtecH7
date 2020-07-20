import utils
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
      "iddocentes": self.iddocentes,
      "nombredocente": self.nombredocente,
      "dnidocente": self.dnidocente,
      "correodocente": self.correodocente,
      "nacdocente": self.nacdocente
    }
    return d
    
    