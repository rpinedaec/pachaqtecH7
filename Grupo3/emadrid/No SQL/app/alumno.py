class alumno:
    def __init__(self, idAlumno , codigoAlumno, nombreAlumno, apellidoAlumno, direccionAlumno):
        self.idAlumno = idAlumno
        self.codigoAlumno = codigoAlumno
        self.nombreAlumno = nombreAlumno
        self.apellidoAlumno = apellidoAlumno
        self.direccionAlumno = direccionAlumno

    def toDic(self):
        d = {
            "idAlumno": self.idAlumno,
            "nombreAlumno": self.nombreAlumno,
            "apellidoAlumno": self.apellidoAlumno,
            "direccionAlumno": self.direccionAlumno
        }
        return d



        
      