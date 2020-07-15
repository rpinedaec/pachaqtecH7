class docente:
    def __init__(self, idDocente , codigoDocente, nombreDocente, apellidoDocente, direccionDocente):
        self.idDocente = idDocente
        self.codigoDocente = codigoDocente
        self.nombreDocente = nombreDocente
        self.apellidoDocente = apellidoDocente
        self.direccionDocente = direccionDocente

    def toDic(self):
        d = {
            "idDocente": self.idDocente,
            "codigo"
            "nombreDocente": self.nombreDocente,
            "apellidoDocente": self.apellidoDocente,
            "direccionDocente": self.direccionDocente
        }
        return d