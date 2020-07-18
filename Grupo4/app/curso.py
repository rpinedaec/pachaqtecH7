import conexion
import utils
from time import sleep
log = utils.log("INIT")
log.info("inicio del programa")


class curso:
    def __init__(self, idsalon, nombresalon):
        self.idsalon = idsalon
        self.nombresalon = nombresalon

    #Mantenimiento de la tabla salon##
    def mantenimientosalon(self):
        if (self == 1):  # Si es uno ingresa a mysql
            dicMenuSalon = {"\t- Buscar Todos Los Cursos": 1,
                            "\t- Buscar Curso por ID": 2,
                            "\t- Modificar Curso Por Id": 3,
                            "\t- Crear Curso": 4,
                            "\t- Borrar Curso": 5}
            menuSalon = utils.Menu("Menu Salones de Clases", dicMenuSalon)
            resMenuSalon = menuSalon.mostrarMenu()
            
            if(resMenuSalon == 1):
                try:
                    log.debug("buscamos el salon")
                    conn = conexion.conexionBDD(self)
                    query = "select idcurso as IdCurso,nombreCurso Nombre,salon_idsalon as Salon from curso;"
                    resConn = conn.consultarBDD(query)

                    print("\tID\t\tDescripción")
                    for row in resConn:
                        print(
                            f"\t{str(row[0])}\t\t{str(row[1])}")
                    input("continuar???")
                    print(resConn)
                except Exception as error:
                    return False

            elif(resMenuSalon == 2):
                try:
                    log.debug("buscamos el salon por id")
                    print("Escribe el Id del salon de clases a buscar:")
                    idsalon = input()
                    conn = conexion.conexionBDD(self)
                    query = f"select idsalon as IdSalon, nombreSalon as Descripcion from salon where IdSalon= '{idsalon}';"
                    resConn = conn.consultarBDD(query)

                    print("\tID\t\tDescripción")
                    for row in resConn:
                        print(
                            f"\t{str(row[0])}\t\t{str(row[1])}")
                    input("continuar???")
                    print(resConn)
                except Exception as error:
                    return False

            elif(resMenuSalon == 3):
                try:
                    log.debug("buscamos el salon")
                    conn = conexion.conexionBDD(self)
                    query = "select idsalon as IdSalon, nombreSalon as Descripcion from salon;"
                    resConn = conn.consultarBDD(query)
                    print("Escoja el ID del salon de clases que desea modificar:")
                    print("\tID\t\tDescripción")
                    for row in resConn:
                        print(
                            f"\t{str(row[0])}\t\t{str(row[1])}")
                    idsalon = input()
                    print("Escriba el nuevo valor para el nombre del salon de clases:")
                    nombre = input()
                    query = f"update salon set nombreSalon = '{nombre}' where IdSalon = {idsalon};"
                    resConn = conn.ejecutarBDD(query)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif(resMenuSalon == 4):
                try:
                    print("## Creacion de un salon de clases ##")
                    print("Escriba el Nombre del Salon de Clases:")
                    nombre = input()
                    conn = conexion.conexionBDD(self)
                    query = f"insert into salon (nombreSalon) values('{nombre}');"
                    resConn = conn.ejecutarBDD(query)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif(resMenuSalon == 5):
                try:
                    log.debug("eliminamos el alumno")
                    conn = conexion.conexionBDD(self)
                    query = "select idsalon as IdSalon, nombreSalon as Descripcion from salon;"
                    resConn = conn.consultarBDD(query)
                    print("Escoja el ID del salon de clases que desea eliminar:")
                    print("\tID\t\tDescripción")
                    for row in resConn:
                        print(
                            f"\t{str(row[0])}\t\t{str(row[1])}")

                    idsalon = input()

                    query = f"delete from salon where IdSalon = {idsalon} ;"
                    resConn = conn.ejecutarBDD(query)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

        else:  # Si es dos entra a mongo

            dicMenuSalon = {"\t- Buscar Todos Los Cursos en mongodb": 1,
                            "\t- Buscar Curso por ID en mongodb": 2,
                            "\t- Modificar Curso Por Id en mongodb": 3,
                            "\t- Crear Curso en mongodb": 4,
                            "\t- Borrar Curso en mongodb": 5}
            menuSalon = utils.Menu("Menu Salones de Clases", dicMenuSalon)
            resMenuSalon = menuSalon.mostrarMenu()

            if(resMenuSalon == 1):
                try:
                    log.debug("buscamos el curso")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistros("curso",query)
                    
                    print("\tIDSalon\t\tCurso\t\tIDSalon\t\tnombreSalon")
                    for row in resConn:
                       print(f"\t{str(row['idcurso'])}\t\t{str(row['nombreCurso'])}\t\t{str(row['idsalon'])}\t\t{str(row['nombreSalon'])}")
                    input("continuar???")
                    print(resConn)
                except Exception as error:
                    return False

            elif(resMenuSalon == 2):            
                try:
                    log.debug("buscamos el curso por id")

                    print("Escribe el Id del curso a buscar:")
                    codigo = input()
                    conn = conexion.conexionBDD(4)
                    #query = {}
                    resConn = conn.leerRegistro("curso",{'idcurso': codigo})
                    #resConn = conn.consultarBDD(query)
                    if resConn:
                        print("\tIDSalon\t\tCurso\t\tIDSalon\t\tnombreSalon")
                        print(f"\t{str(resConn['idcurso'])}\t\t{str(resConn['nombreCurso'])}\t\t{str(resConn['idsalon'])}\t\t{str(resConn['nombreSalon'])}")
                    else:
                        print("No existe resultado")
                    input("continuar???")
                except Exception as error:
                    return False

            elif(resMenuSalon == 3):
                try:
                    log.debug("buscamos el curso")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistros("curso",query)
                    print("Escoja el ID del curso que desea modificar:")
                    print("\tIDSalon\t\tCurso\t\tIDSalon\t\tnombreSalon")

                    for row in resConn:
                        print(f"\t{str(row['idcurso'])}\t\t{str(row['nombreCurso'])}\t\t{str(row['idsalon'])}\t\t{str(row['nombreSalon'])}")
                    codigo = input()
                    print("Escriba el nuevo valor para el nombre del curso:")
                    nombre = input()
                    nuevocurso = dict()
                    nuevocurso = {'nombreCurso': (nombre)}
                    resConn = conn.actualizarRegistro('curso', {'idcurso': codigo}, nuevocurso)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False
            elif (resMenuSalon == 4):
                try:
                    print("## Creacion de un curso ##")
                    print ("Escriba el codigo del curso")
                    codigo = input()
                    print("Escriba el Nombre del curso:")
                    nombre = input()
                    print("Escriba el codigo del salon:")
                    codigosalon = input()
                    print("Escriba el codigo del docente:")
                    codigodocente = input()
                    conn = conexion.conexionBDD(4)

                    #Buscar nombre de salon
                    resConn = conn.leerRegistro("salon",{'idsalon': codigosalon})
                    if resConn:
                        nombresalon = resConn['nombreSalon']
                    else:
                        print("No existe salon")
                        sleep(5)
                    
                    #Buscar nombre de docente
                    resConn = conn.leerRegistro("docente",{'iddocente': codigosalon})
                    if resConn:
                        nombredocente = resConn['nombreDocente'] + ', ' + resConn['apellidosDocente']
                    else:
                        print("No existe docente")
                        sleep(5)
                    
                    if  nombresalon and nombredocente:
                        nuevocurso = dict()
                        nuevocurso = {'idcurso': (codigo), 'nombreCurso': (nombre), 'idsalon': (codigosalon), 'nombreSalon': (nombresalon), 
                            'iddocente': (codigodocente), 'nombreDocente': (nombredocente)}
                        resConn = conn.insertarRegistro("curso",nuevocurso)
                        if(resConn):
                            print("Se ejecuto correctamente")
                        else:
                            print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif (resMenuSalon == 5):
                try:
                    log.debug("eliminamos el curso")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistros("curso",query)
                    print("\tIDSalon\t\tCurso\t\tIDSalon\t\tnombreSalon")
                    for row in resConn:
                        print(f"\t{str(row['idcurso'])}\t\t{str(row['nombreCurso'])}\t\t{str(row['idsalon'])}\t\t{str(row['nombreSalon'])}")
                    print("Escoja el ID del curso que desea eliminar:")
                    codigo = input()
                    #conn = conexion.conexionBDD(4)
                    eliminarcurso = dict()
                    eliminarcurso = {'idcurso': (codigo)}
                    resConn = conn.eliminarRegistro('curso',eliminarcurso)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False 
        
                
