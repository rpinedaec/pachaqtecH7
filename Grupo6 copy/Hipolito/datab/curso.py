from connection.conn import Conexion

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre

conn = Conexion('mongodb://localhost:27017', 'ProyectoGrupo6')

# print(conn.obtener_registro('mobilecurso'))
# conn.acutalizar_registro{'curso', {'nombre': 'Matematica'} {'nombre': 'Quimica'}}
# conn.eliminar_registro{'curso', {'nombre': 'Quimica'}}

curso = Curso ('Literatura')
conn.insertar_registro('curso', {
    'Nombre': curso.nombre
})