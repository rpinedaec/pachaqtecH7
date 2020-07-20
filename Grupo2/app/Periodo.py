class Periodo:
    def __init__(self, nombre):
        self.nombrePeriodo = nombre

    def dictPeriodo(self):
        e = {
            'nombrePeriodo': self.nombrePeriodo
        }
        return e