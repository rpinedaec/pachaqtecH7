import conexion
import utils
import alumno
#from bson.objectid import ObjectId # Para crear ObjectId, porque _id como cadena no funciona

log = utils.log("INIT")
log.info("inicio del programa")



class notas:
    def __init__(self, idnotas, descNotas, idalumno,idperiodo,iddocente,idcurso):
        self.idnotas = idnotas
        self.descNotas = descNotas
        self.idalumno = idalumno
        self.idperiodo = idperiodo
        self.iddocente = iddocente
        self.idcurso = idcurso

   
    #Mantenimiento de la tabla notas##

    def mantenimientonotas(self):
        if (self == 1):  # Si es uno ingresa a mysql
            dicMenuNota = {"\t- Buscar Todas Los Notas": 1,
                             "\t- Buscar Notas Por ID Alumno": 2,
                             "\t- Modificar Notas Por Id Alumno": 3,
                             "\t- Registrar Notas": 4,
                             "\t- Borrar Nota": 5}
            menuNota = utils.Menu("Menu Nota", dicMenuNota)
            resMenuNotas = menuNota.mostrarMenu()
            if(resMenuNotas == 1):
                try:
                    log.debug("Obtenemos los Promedios de los ALumnos")
                    conn = conexion.conexionBDD(self)
                    query = "select idnotas as idnotas,descNotas as Nota,idalumno as idalumno,idperiodo as idperiodo,iddocente as iddocente,idcurso as idcurso from notas;"
                    resConn = conn.consultarBDD(query)

                    print("\tID\t\tNota\t\tCodigoAlumno\t\tCodigoPeriodo\t\tCodigoDocente\tCodigoCurso")
                    for row in resConn:
                            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}\t\t{str(row[5])}")

                    input("continuar???")
                    print(resConn)
                except Exception as error:
                    return False

            elif(resMenuNotas == 2):
                try:
                    log.debug("Buscamos la Nota por id del ALumno y del Curso")
                    print("Escribe el Id del Alumno:")
                    idalumno = input()
                    print("Escribe el Id del Curso:")
                    idcurso = input()
                    conn = conexion.conexionBDD(self)
                    query = f"select a.idnotas as idnotas,a.descNotas as Nota,a.idalumno as idalumno,a.idcurso as idcurso, b.nombreAlumno as nombreAlumno,c.nombreCurso as nombreCurso from notas  a  left join alumno b on a.idalumno = b.idalumnno left join curso c on a.idcurso = c.idcurso  where a.idalumno= '{idalumno}' and a.idcurso= '{idcurso}';"
                    resConn = conn.consultarBDD(query)

                    print("\tID\t\tNota\t\tCodigoAlumno\t\tCodigoCurso\t\tNombeAlumno\t\tNombreCurso")
                    for row in resConn:
                        print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}\t\t{str(row[5])}")

                    input("continuar???")
                    print(resConn)
                except Exception as error:
                    return False

            elif(resMenuNotas == 3):
                try:
                    log.debug("buscamos la Nota")
                    conn = conexion.conexionBDD(self)
                    query = "select idnotas as idnotas,descNotas as Nota,idalumno as idalumno,idperiodo as idperiodo,iddocente as iddocente,idcurso as idcurso from notas;"
                    resConn = conn.consultarBDD(query)
                    print("Escoja el ID del Alumno:")
                    print("\tID\t\tNota\t\tCodigoAlumno\t\tCodigoPeriodo\t\tCodigoDocente\tCodigoCurso")
                    for row in resConn:
                      print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}\t\t{str(row[5])}")

                    idalumno = input()
                    print("Escoja el ID del Curso:")
                    print("\tID\t\tNota\t\tCodigoAlumno\t\tCodigoPeriodo\t\tCodigoDocente\tCodigoCurso")
                    for row in resConn:
                        print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}\t\t{str(row[5])}")

                    idcurso = input()
                    print("Escriba la Nueva Nota para el Alumno:")
                    nota = input()
                  
                    query = f"update notas set descNotas = '{nota}' where idalumno = {idalumno} and idcurso = {idcurso};"
                    resConn = conn.ejecutarBDD(query)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif(resMenuNotas == 4):
                try:
                    print("## Registro Nota ##")
                    print("Escriba la Nota:")
                    promedio = input()
                    print("Escriba el codigo del ALumno:")
                    idalumno = input()
                    print("Escriba el codigo del Periodo:")
                    idperiodo = input()
                    print("Escriba el codigo del Docente:")
                    iddocente = input()
                    print("Escriba el codigo del Curso:")
                    idcurso = input()
                    conn = conexion.conexionBDD(self)
                    query = f"insert into notas (desNotas,idalumno,idperiodo,iddocente,idcurso) values('{promedio}','{idalumno}','{idperiodo}','{iddocente}','{idcurso}');"
                    resConn = conn.ejecutarBDD(query)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif(resMenuNotas == 5):
                try:
                    log.debug("eliminamos la Nota del Alumno")
                    conn = conexion.conexionBDD(self)
                    query = "select idnotas as idnotas,descNotas as Nota,idalumno as idalumno,idperiodo as idperiodo,iddocente as iddocente,idcurso as idcurso from notas;"
                    resConn = conn.consultarBDD(query)
                    print("Escoja el ID del Alumno de la Nota a Borrar:")
                    print("\tID\t\tPromedio\t\tCodigoAlumno\t\tCodigoCurso")
                    for row in resConn:
                        print(
                            f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}\t\t{str(row[5])}")

                    idalumno = input()

                    query = f"delete from notas where idalumno = {idalumno} ;"
                    resConn = conn.ejecutarBDD(query)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False
#######################################
        else:  # Si es dos entra a mongo
            print("Se ejecuto correctamente")
        

            dicMenuNotas = {"\t- Buscar Todos Las Notas": 1,
                             "\t- Buscar Notas Por Idalumno": 2,
                             "\t- Modificar Notas Por Idcurso": 3,
                             "\t- Crear Notas": 4,
                             "\t- Borrar Notas": 5}
            menuNota = utils.Menu("Menu Notas", dicMenuNotas)
            resMenuNotas = menuNota.mostrarMenu()
            if(resMenuNotas == 1):
                try:
                    log.debug("Lista de Notas")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistros("notas", query)

                    print("\tID\t\tNota\t\tCodigoAlumno\t\tCodigoPeriodo\t\tCodigoDocente\t\tCodigoCurso")
                    for row in resConn:
                       print(f"\t{str(resConn['idnotas'])}\t\t{str(resConn['descNotas'])}\t\t{str(resConn['idalumno'])}\t\t{str(resConn['idperiodo'])}\t\t{str(resConn['iddocente'])}\t\t{str(resConn['idcurso'])}")

                    input("continuar???")
                    print(resConn)
                except Exception as error:
                    return False
            elif(resMenuNotas == 2):
                try:
                    log.debug("buscamos el Notas por id del ALumno")
                    print("Escribe el Id del Alumno para Ver su Nota:")
                    idalumno = input()
                    conn = conexion.conexionBDD(4)
                    resConn = conn.leerRegistro("notas",{'idalumno': idalumno})
                    if resConn:
                        print("\tID\t\tNota\t\tCodigoAlumno\t\tCodigoPeriodo\t\tCodigoDocente\tCodigoCurso")
                        print(f"\t{str(resConn['idnotas'])}\t\t{str(resConn['descNotas'])}\t\t{str(resConn['idalumno'])}\t\t{str(resConn['idperiodo'])}\t\t{str(resConn['iddocente'])}\t\t{str(resConn['idcurso'])}")
                    else:
                        print("No existe resultado")
                    input("continuar???")
                    print(resConn)
                except Exception as error:
                    return False

            elif(resMenuNotas== 3):
                try:
                    log.debug("buscamos La Nota")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistro("notas",query)
                    print("Escoja el ID del Alumno que desea modificar su Nota:")
                    print("\tID\t\tNota\t\tCodigoAlumno\t\tCodigoPeriodo\t\tCodigoDocente\tCodigoCurso")
                    for row in resConn:
                        print(
                            f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}\t\t{str(row[5])}")
                    idalumno = input()
                    print("Escriba la Nueva Nota:")
                    nota = input()
                    print("Escriba el codigo del periodo")
                    periodo = input()
                    print("Escriba el codigo del curso")
                    curso = input()
                    nuevanota = dict()
                    nuevanota={'idalumno': (idalumno), 'descNotas': (nota), 'idperiodo': (periodo), 'idcurso': (curso)}
                    resConn =conn.actualizarRegistro('docente', {'idalumno': idalumno}, nuevanota)
                    if(resConn):
                        print("Se actualizó correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif(resMenuNotas == 4):
                try:
                    print("## Inserción de Nota ##")
                    print("Escriba codigo de Nota:")
                    idnotas = input()
                    print("Escriba la Nota para el Alumno:")
                    nota = input()
                    print("Escriba el Código del Alumno:")
                    idalumno = input()
                    print("Escriba el codigo del periodo")
                    periodo = input()
                    print("Escriba el codigo del docente")
                    iddocente = input()
                    print("Escriba el codigo del curso")
                    idcurso = input()
                    conn = conexion.conexionBDD(4)
                    nuevanota = dict()
                    nuevanota={'idnotas': (idnotas), 'descNotas': (nota), 'idalumno': (idalumno), 'idperiodo': (periodo), 'iddocente': (iddocente), 'idcurso': (idcurso)}
                    resConn =conn.insertarRegistro('notas', nuevanota)
                    if(resConn):
                        print("Se insertó correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif(resMenuNotas == 5):
                try:
                    log.debug("eliminamos la Nota")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistros("notas", query)
                    print("Escoja el ID de la Nota que desea eliminar:")
                    print("\tID\t\tNota\t\tCodigoAlumno\t\tCodigoPeriodo\t\tCodigoDocente\t\tCodigoCurso")
                    for row in resConn:
                        print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}\t\t{str(row[4])}")

                    idnotas = input()
                    conn = conexion.conexionBDD(4)
                    eliminarnota = dict()
                    eliminarnota = {'idnotas': (idnotas)}
                    resConn = conn.eliminarRegistro('notas', eliminarnota)
                    if(resConn):
                        print("Se eliminó correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False