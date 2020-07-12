from connection.conn import Connection

# Nivel avanzado
# Listar a los profesores con su respectiva curso, salon y alumnos

connection = Connection(
    'mongodb+srv://reyner:pachaqtec@pachaqtec.sdvq7.mongodb.net/pachaqtec?retryWrites=true&w=majority', 'pachacteq')


def listarProfesores():

    # empezaremos a buscar por cursos
    collection = connection.db["cursos"]
    data = collection.find(
        [
            {
                '$lookup': {
                    'from': 'alumnos',
                    'localField': 'idAlumno',
                    'foreignField': '_id',
                    'as': 'Alumnos'
                }
            }, {
                '$lookup': {
                    'from': 'profesores',
                    'localField': 'idProfesor',
                    'foreignField': '_id',
                    'as': 'Profesores'
                }
            }
        ]
    )
