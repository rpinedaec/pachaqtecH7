class nota:
    def __init__(self, idNota, descripcionNota, idCurso, idAlumno):
        self.idNota = idNota
        self.descripcionNota = descripcionNota
        self.idCurso = idCurso
        self.idAlumno = idAlumno


class notaDescripcion:
    def __init__(self, idNota, descripcionNota, Curso, Alumno):
        self.idNota = idNota
        self.descripcionNota = descripcionNota
        self.idCurso = Curso
        self.idAlumno = Alumno
