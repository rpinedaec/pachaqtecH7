import conexion
import utils

log = utils.log("INIT")
log.info("inicio del programa")



class promedio:
    def __init__(self, idpromedio, descPromedio, idalumno,idcurso):
        self.idpromedio = idpromedio
        self.descPromedio = descPromedio
        self.idalumno = idalumno
        self.idcurso = idcurso





  #Mantenimiento de la tabla promedio##

    def mantenimientopromedio(self):
        if (self == 1):  # Si es uno ingresa a mysql
            dicMenuPromedio = {"\t- Buscar Todos Los Promedios": 1,
                             "\t- Buscar Promedio Por ID Alumno": 2,
                             "\t- Modificar Promedio Por Id Alumno": 3,
                             "\t- Registrar Promedio": 4,
                             "\t- Borrar Promedio": 5}
            menuPromedio = utils.Menu("Menu Promedio", dicMenuPromedio)
            resMenuPromedio = menuPromedio.mostrarMenu()
            if(resMenuPromedio == 1):
                try:
                    log.debug("Obtenemos los Promedios de los ALumnos")
                    conn = conexion.conexionBDD(self)
                    query = "select idpromedio as idpromedio,descPromedio as Promedio,idalumno as idalumno,idcurso as idcurso from promedio;"
                    resConn = conn.consultarBDD(query)

                    print("\tID\t\tPromedio\t\tCodigoAlumno\t\tCodigoCurso")
                    for row in resConn:
                            print(
                                f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

                    input("continuar???")
                    print(resConn)
                except Exception as error:
                    return False

            elif(resMenuPromedio == 2):
                try:
                    log.debug("Buscamos el Promedio por id del ALumno y del Curso")
                    print("Escribe el Id del Alumno:")
                    idalumno = input()
                    print("Escribe el Id del Curso:")
                    idcurso = input()
                    conn = conexion.conexionBDD(self)
                    query = f"select a.idpromedio as idpromedio,a.descPromedio as Promedio,a.idalumno as idalumno,a.idcurso as idcurso, b.nombreAlumno as nombreAlumno,c.nombreCurso as nombreCurso from promedio  a  left join alumno b on a.idalumno = b.idalumnno left join curso c on a.idcurso = c.idcurso  where a.idalumno= '{idalumno}' and a.idcurso= '{idcurso}';"
                    resConn = conn.consultarBDD(query)

                    print("\tID\t\tPromedio\t\tCodigoAlumno\t\tCodigoCurso\t\tNombreAlumno\t\tNombreCurso")
                    for row in resConn:
                        print(
                           f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}\t\t{str(row[4])}\t\t{str(row[5])}\t\t{str(row[6])}")

                    input("continuar???")
                    print(resConn)
                except Exception as error:
                    return False

            elif(resMenuPromedio == 3):
                try:
                    log.debug("buscamos el Promedio")
                    conn = conexion.conexionBDD(self)
                    query = "select idpromedio as idpromedio,descPromedio as Promedio,idalumno as idalumno,idcurso as idcurso from promedio;"
                    resConn = conn.consultarBDD(query)
                    print("Escoja el ID del Alumno:")
                    print("\tID\t\tPromedio\t\tCodigoAlumno\t\tCodigoCurso")
                    for row in resConn:
                        print(
                             f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

                    idalumno = input()
                    print("Escoja el ID del Curso:")
                    print("\tID\t\tPromedio\t\tCodigoAlumno\t\tCodigoCurso")
                    for row in resConn:
                        print(
                             f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

                    idcurso = input()
                    print("Escriba el nuevo valor del Promedio para el Alumno:")
                    promedio = input()
                  
                    query = f"update promedio set descPromedio = '{promedio}' where idalumno = {idalumno} and idcurso = {idcurso};"
                    resConn = conn.ejecutarBDD(query)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif(resMenuPromedio == 4):
                try:
                    print("## Registro Promedio ##")
                    print("Escriba el Promedio:")
                    promedio = input()
                    print("Escriba el codigo del ALumno:")
                    idalumno = input()
                    print("Escriba el codigo del Curso:")
                    idcurso = input()
                    conn = conexion.conexionBDD(self)
                    query = f"insert into promedio (desPromedio,idalumno,idcurso) values('{promedio}','{idalumno}','{idcurso}');"
                    resConn = conn.ejecutarBDD(query)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif(resMenuPromedio == 5):
                try:
                    log.debug("eliminamos el Promedio del Alumno")
                    conn = conexion.conexionBDD(self)
                    query = "select idpromedio as idpromedio,descPromedio as Promedio,idalumno as idalumno,idcurso as idcurso from promedio;"
                    resConn = conn.consultarBDD(query)
                    print("Escoja el ID del Promedio que desea eliminar:")
                    print("\tID\t\tPromedio\t\tCodigoAlumno\t\tCodigoCurso")
                    for row in resConn:
                        print(
                            f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

                    idpromedio = input()

                    query = f"delete from promedio where idpromedio = {idpromedio} ;"
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
        

            dicMenuPromedio = {"\t- Buscar Todos Los Promedios": 1,
                             "\t- Buscar Promedio Por IdPromedio": 2,
                             "\t- Modificar Promedio Por IdAlumno": 3,
                             "\t- Insertar Promedio": 4,
                             "\t- Borrar Promedio": 5}
            menuPromedio = utils.Menu("Menu Notas", dicMenuPromedio)
            resMenuPromedio = menuPromedio.mostrarMenu()
            if(resMenuPromedio == 1):
                try:
                    log.debug("Lista Promedios")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistros("promedio", query)
                    print("\tID\t\tPromedio\t\tCodigoAlumno\t\tCodigoCurso")
                    for row in resConn:
                       print(f"\t{str(resConn['idpromedio'])}\t\t{str(resConn['descPromedio'])}\t\t{str(resConn['idalumno'])}\t\t{str(resConn['idcurso'])}")

                    input("continuar???")
                    print(resConn)
                except Exception as error:
                    return False

            elif(resMenuPromedio == 2):
                try:
                    log.debug("buscamos Promedio por id del ALumno")
                    print("Escribe el Id del Alumno para Ver su Promedio:")
                    idpromedio = input()
                    conn = conexion.conexionBDD(4)
                    resConn = conn.leerRegistro("promedio",{'idpromedio': idpromedio})
                    
                    if resConn:
                        print("\tID\t\tPromedio\t\tCodigoAlumno\t\tCodigoCurso")
                        print(f"\t{str(resConn['idpromedio'])}\t\t{str(resConn['descPromedio'])}\t\t{str(resConn['idalumno'])}\t\t{str(resConn['idcurso'])}")
                    else:
                        print("No existe resultado")
                    input("continuar???")
                   # print(resConn)
                except Exception as error:
                    return False

            elif(resMenuPromedio== 3):
                try:
                    log.debug("buscamos La Nota")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistro("notas",query)
                    print("Escoja el ID del Alumno que desea modificar su Promedio:")
                    print("\tID\t\tPromedio\t\tCodigoAlumno\t\tCodigoCurso")
                    for row in resConn:
                        print(
                            f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
                    idalumno= input()
                    print("Escriba Nuevo Promedio:")
                    promedio = input()
                    print("Escriba el codigo del curso")
                    curso = input()
                    nuevopromedio = dict()
                    nuevopromedio={'idpromedio': (idpromedio), 'descPromedio': (promedio), 'idalumno': (idalumno), 'idcurso': (curso)}
                    resConn =conn.actualizarRegistro('promedio', {'idalumno': idalumno}, nuevopromedio)
                    if(resConn):
                        print("Se actualizó correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif(resMenuPromedio == 4):
                try:
                    print("## Inserción de Promedio ##")
                    print("Escriba codigo del Alumno:")
                    idalumno = input()
                    print("Escriba El Promedio para el Alumno:")
                    promedio = input()
                    print("Escriba el Código del Curso:")
                    idcurso = input()
                 
                    conn = conexion.conexionBDD(4)
                    nuevopromedio = dict()
                    nuevopromedio={'descPromedio': (promedio), 'idalumno': (idalumno), 'idcurso': (idcurso)}
                    resConn =conn.insertarRegistro('promedio', nuevopromedio)
                    if(resConn):
                        print("Se insertó correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif(resMenuPromedio == 5):
                try:
                    log.debug("eliminamos el Promedio")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistros("promedio", query)
                    print("Escoja el ID del Promedio que desea eliminar:")
                    print("\tID\t\tPromedio\t\tCodigoAlumno\t\tCodigoCurso")
                    for row in resConn:
                        print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

                    idpromedio = input()
                    conn = conexion.conexionBDD(4)
                    eliminarpromedio = dict()
                    eliminarpromedio = {'idpromedio': (idpromedio)}
                    resConn = conn.eliminarRegistro('promedio', eliminarpromedio)
                    if(resConn):
                        print("Se eliminó correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

