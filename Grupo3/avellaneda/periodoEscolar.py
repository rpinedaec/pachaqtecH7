import utils
#Clase Periodo Escolar
class periodoEscolar:
  __log = utils.log("periodo escolar")
  def __init__(self, idperiodoEscolar, desperiodo):
    self.idperiodoEscolar = idperiodoEscolar
    self.desperiodo = desperiodo

  def toDic(self):
    d = {
      "idperiodoEscolar": self.idperiodoEscolar,
      "desperiodo": self.desperiodo
    }
    return d
   