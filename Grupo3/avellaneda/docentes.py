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
    
    
    