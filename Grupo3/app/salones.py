import utils
#clase salones
class salones:
  __log = utils.log("salones")
  def __init__(self, idsalones, nombresalon):
    self.idsalones = idsalones
    self.nombresalon = nombresalon
  
  def toDic(self):
    d = {
      "idsalones": self.idsalones,
      "nombresalon": self.nombresalon   
    }
    return d
    