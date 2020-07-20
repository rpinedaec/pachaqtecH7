class Salon:
    def __init__(self, nombre):
        self.nombreSalon = nombre

    def dictSalon(self):
        e = {
            'nombreSalon': self.nombreSalon,
        }
        return e