class Alumnos:
    def __init__(self, dni, nombre, apellido, correo):
        self.dniAlumno = dni
        self.nombreAlumno = nombre
        self.apellidoAlumno = apellido
        self.correoAlumno = correo

    def dictAlumno(self):
        e = {
            'dniAlumno': self.dniAlumno,
            'nombreAlumno': self.nombreAlumno,
            'apellidoAlumno': self.apellidoAlumno,
            'correoAlumno': self.correoAlumno
        }
        return e