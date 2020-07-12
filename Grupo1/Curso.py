from connection.conn import Connection


connection = Connection('', 'pachacteq')

print(connection.obtenerRegistro('profesores'))
