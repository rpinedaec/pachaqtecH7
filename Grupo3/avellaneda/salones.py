import utils
#clase salones
class salones:
  __log = utils.log("salones")
  def __init__(self, idsalones, nombresalon):
    self.idsalones = idsalones
    self.nombresalon = nombresalon
    