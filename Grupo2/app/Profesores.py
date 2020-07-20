class Profesores:
    def __init__(self, dni, nombre, apellido, correo):
        self.dniProfesor = dni
        self.nombreProfesor = nombre
        self.apellidoProfesor = apellido
        self.correoProfesor = correo

    def dictProfesor(self):
        e = {
            'dniProfesor': self.dniProfesor,
            'nombreProfesor': self.nombreProfesor,
            'apellidoProfesor': self.apellidoProfesor,
            'correoProfesor': self.correoProfesor
        }
        return e