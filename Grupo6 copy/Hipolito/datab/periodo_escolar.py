from connection.conn import Conexion

class Periodo_escolar:
    def __init__(self, nombre):
        self.nombre = nombre
    
conn = Conexion('mongodb://localhost:27017', 'ProyectoGrupo6')

# print(conn.obtener_registro('periodo_escolar'))

periodo_escolar = Periodo_escolar ('Primer Semestre')
conn.insertar_registro('periodo escolar', {
    'Nombre': periodo_escolar.nombre,
})