from connection.conn import Connection
from bson.json_util import dumps
from bson import ObjectId
from tabulate import tabulate



def listarListaPromedioNotasAlumnos(desSemestre,idCurso,connection):
    # A falta de poblar la tabla con mas informacion se mostrara la lista promedio por semestreme y por cursos de mayor a menor 
    collection = connection.returnCollection('notas')
    data = collection.aggregate([
    {
        '$lookup': {
            'from': 'cursos', 
            'localField': 'idCurso', 
            'foreignField': '_id', 
            'as': 'curso'
        }
    }, {
        '$unwind': {
            'path': '$curso'
        }
    }, {
        '$lookup': {
            'from': 'semestres', 
            'localField': 'curso.idPeriodo', 
            'foreignField': '_id', 
            'as': 'idPeriodo'
        }
    }, {
        '$unwind': {
            'path': '$idPeriodo'
        }
    }, {
        '$group': {
            '_id': {
                'idAlumno': '$idAlumno', 
                'idCurso': '$idCurso', 
                'idPeriodo': '$idPeriodo.desSemestre'
            }, 
            'average': {
                '$avg': '$nota'
            }
        }
    }, {
        '$sort': {
            'average': -1
        }
    },
    {
        '$match': {
            '_id.idPeriodo': desSemestre,
            '_id.idCurso': idCurso
        }
    }
    ])

    data = list(data)
    getNameCursoById = connection.obtenerRegistro("cursos",{'_id': idCurso})
    lista = []
    for i in range(len(data)):
        getAlumnoNameById = connection.obtenerRegistro("alumnos",{'_id': data[i]['_id']['idAlumno']})
        lista.append([desSemestre,getNameCursoById,getAlumnoNameById,data[i]['average']])

    print(tabulate(lista, headers=[
          "Semestre", "Curso", "Alumno", "Promedio"], tablefmt='fancy_grid'))

    
def listarListaPromedioNotasAlumnos2(connection):
    # A falta de poblar la tabla con mas informacion se mostrara la lista promedio por semestreme y por cursos de mayor a menor 
    collection = connection.returnCollection('notas')
    data = collection.aggregate([
    {
        '$lookup': {
            'from': 'cursos', 
            'localField': 'idCurso', 
            'foreignField': '_id', 
            'as': 'curso'
        }
    }, {
        '$unwind': {
            'path': '$curso'
        }
    }, {
        '$lookup': {
            'from': 'semestres', 
            'localField': 'curso.idPeriodo', 
            'foreignField': '_id', 
            'as': 'idPeriodo'
        }
    }, {
        '$unwind': {
            'path': '$idPeriodo'
        }
    }, {
        '$group': {
            '_id': {
                'idAlumno': '$idAlumno', 
                'idCurso': '$idCurso', 
                'idPeriodo': '$idPeriodo.desSemestre'
            }, 
            'average': {
                '$avg': '$nota'
            }
        }
    }, {
        '$sort': {
            'average': -1
        }
    }

    ])

    data = list(data)
    
    lista = []
    for i in range(len(data)):
        getAlumnoNameById = connection.obtenerRegistro("alumnos",{'_id': data[i]['_id']['idAlumno']})
        getNameCursoById = connection.obtenerRegistro("cursos",{'_id': data[i]['_id']['idCurso']})

        if getAlumnoNameById != None or getAlumnoNameById != None:
              lista.append([data[i]['_id']['idPeriodo'],getNameCursoById['nombreCurso'],getAlumnoNameById['nombreAlumno'],data[i]['average']])

    print(tabulate(lista, headers=[
          "Semestre", "Curso", "Alumno", "Promedio"], tablefmt='fancy_grid'))

def listarProfesores(nombreProfesor, connection):
    collection = connection.returnCollection('profesores')
    # empezaremos a buscar por salones
    data = collection.aggregate(
        [
            {
                '$lookup': {
                    'from': 'salones',
                            'localField': '_id',
                            'foreignField': 'idProfesor',
                            'as': 'salones'
                }
            }, {
                '$lookup': {
                    'from': 'cursos',
                    'localField': 'idCurso',
                    'foreignField': '_id',
                    'as': 'curso'
                }
            },
            {
                '$match': {
                    'nombreProfesor': nombreProfesor
                }
            }

        ]
    )

    data = list(data)[0]

    # agregar alumnos a cada salon
    for i in range(len(data["salones"])):

        id_ = data["salones"][i]["_id"]
        alumnos = connection.obtenerRegistros('alumnos', {'idSalon': id_})

        # agregamos los alumnos que corresponden a cada salon
        data["salones"][i]["alumnos"] = alumnos

    _id, nombreProfesor, _, _, _, salones, curso = data.values()

    table = []
    for salon in salones:

        for alumno in salon['alumnos']:
            table.append([nombreProfesor, curso[0]["nombreCurso"],
                          salon['nombreSalon'], alumno['nombreAlumno'], alumno['correoAlumno']])

    print(tabulate(table, headers=[
          "Nombre Profesor", "Curso", "Nombre Salon", "Nombre Alumno", "Correo Alumno"], tablefmt='fancy_grid'))


def listarAlumnos(nombreAlumno, connection):

    collection = connection.returnCollection('alumnos')
    data = collection.aggregate([
        {
            '$lookup': {
                'from': 'salones',
                'localField': 'idSalon',
                'foreignField': '_id',
                'as': 'salones'
            }
        },
        {
            '$match': {
                'nombreAlumno': nombreAlumno
            }
        }
    ])

    data = list(data)[0]
    #print(data)
    # print(dumps(data,indent=2))
    # profesorId is ObjectId, para imprimirlo se debe from bson import ObjectId
    profesorId = data['salones'][0]['idProfesor']
    # print(dumps(profesorId,indent=2))
    objetoProfesor = (connection.obtenerRegistros(
        'profesores', {'_id': profesorId}))[0]
    obtenerCursoNombre = (connection.obtenerRegistros(
        'cursos', {'_id': objetoProfesor["idCurso"]}))[0]["nombreCurso"]
    table = [[data['nombreAlumno'], data['correoAlumno'], data['salones'][0]
              ['nombreSalon'], objetoProfesor['nombreProfesor'], obtenerCursoNombre]]
    print(tabulate(table, headers=["Nombre Alumno", "Correo Alumno",
                                   "Nombre Salon", "Nombre Profesor", "Nombre del Curso"], tablefmt='fancy_grid'))


def reporte2(nombreSalon, connection):
    dict = {}

    dataSalones = connection.obtenerRegistros(
        'salones', {'nombreSalon': nombreSalon})
    # print(dataSalones)
    try:
        dataAlumnos = connection.obtenerRegistros(
            'alumnos', {'idSalon': list(dataSalones)[0]['_id']})  # Lista
    except:
        print("Nombre de Salon no Valido")
        return None
    # print(dataAlumnos)
    # al especificar nuestro _id tendremos un solo resultado en la lista [0]
    dataSalones = list(dataSalones)[0]

    nombreSalon = dataSalones["nombreSalon"]
    # print(nombreSalon)

    dict[nombreSalon] = {}

    for dataAlumno in list(dataAlumnos):
        # Accediendo a las notas de cada alumno,
        # dataAlumnos son los alumnos que pertenecen al salon idsalon
        #print("Un Alumno")
        # print(dataAlumno)
        dataNotas = connection.obtenerRegistros(
            'notas', {'idAlumno': dataAlumno['_id']})
        # Al hacer list, casteamos del objeto cursor a un objeto lista
        dataNotas = list(dataNotas)
        # recordar que si hacemos un loop sobre o algo que recorra todo dataNotas, se eliminara toda la data . Por eso se agrega a otra
        # para mantenerla
        # dataNotas son todas las notas que pertenecen a los alumnos que pertencen al salon, es decir las notas que pertecen al salon
        listaNotas = []
        for nota in dataNotas:
            # Obtenemos nombre del curso para la nota
            curso = connection.obtenerRegistros(
                'cursos', {'_id': nota['idCurso']})
            curso = list(curso)[0]  # solo tenemos un curso por un id
            nombreCurso = curso['nombreCurso']
            # obtenemos el nombre del periodo
            periodo = connection.obtenerRegistros(
                'semestres', {'_id': curso['idPeriodo']})
            periodo = list(periodo)[0]
            # nuestro nombre del Periodo
            nombrePeriodo = periodo['desSemestre']
            # listaPeriodoSalonCursoNotas['Semestre'] = nombrePeriodo
            #print("Imprimir Nota")
            # print(nota)
            listaNotas.append(nota['nota'])  # Lista de notas por

            # Verificamos si el objeto nombrePeriodo tiene un valor inicial, sino agregarle uno.
            # Al agregar un valor inicial siempre sin try/except estamos sobrescribiendo con valor inicial
            try:
                a = dict[nombreSalon][nombrePeriodo]
            except:
                dict[nombreSalon][nombrePeriodo] = {}

            # dict[nombreSalon][nombrePeriodo][nombreCurso] = { status = True , notas =[]}
            try:
                a = dict[nombreSalon][nombrePeriodo][nombreCurso]
            except:
                # print("Except")
                dict[nombreSalon][nombrePeriodo][nombreCurso] = []

            dict[nombreSalon][nombrePeriodo][nombreCurso].append(
                nota['nota'])

    #print(dumps(dict, indent=2))
    table = []  # Preparamos la tabla para pretty table

    # average from the notes
    for clase in dict:
        # print(clase)
        for periodo in dict[clase]:
            # print(periodo)
            for curso in dict[clase][periodo]:
                # print(curso)
                suma = 0
                for nota in dict[clase][periodo][curso]:
                    suma = suma + nota

                average = float(suma / len(dict[clase][periodo][curso]))
                table.append([clase, periodo, curso, average])
                # print(average)
                dict[clase][periodo][curso].append(average)

    print(tabulate(table, headers=[
          "Nombre de la Clase", "Periodo", "Nombre Curso", "Promedio"], tablefmt='fancy_grid'))


#reporte2("4to Secundaria")
