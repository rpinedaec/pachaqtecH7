import conexion
import utils

log = utils.log("INIT")
log.info("inicio del programa")



class docente:
    def __init__(self, iddocente, nombredocente, apellidodocente):
        self.iddocente = iddocente
        self.nombredocente = nombredocente
        self.apellidodocente = apellidodocente
    def doDic(self):
        d = {
            "iddocente": self.iddocente,
            "nombredocente": self.nombredocente,
            "apellidodocente": self.apellidodocente
        }
        return d
    #Mantenimiento de la tabla alumno##

    def mantenimientodocente(self):
        if (self == 1):  # Si es uno ingresa a mysql
            dicMenuDocente = {"\t- Buscar Todos Los Docentes": 1,
                             "\t- Buscar Docente Por IDDocente": 2,
                             "\t- Modificar Docente Por Id": 3,
                             "\t- Crear Docente": 4,
                             "\t- Borrar Docente": 5}
            menuDocente = utils.Menu("Menu Docente", dicMenuDocente)
            resMenuDocente = menuDocente.mostrarMenu()
            if(resMenuDocente == 1):
                try:
                    log.debug("Obtenemos lista de docentes")
                    conn = conexion.conexionBDD(self)
                    query = "select iddocente as IdDocente,nombreDocente as Nombre,apellidosDocente as Apellido from docente;"
                    resConn = conn.consultarBDD(query)

                    print("\tID\t\tNombres\t\tApellidos")
                    for row in resConn:
                            print(
                                f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")
                    input("continuar???")
                    print(resConn)
                except Exception as error:
                    return False

            elif(resMenuDocente == 2):
                try:
                    log.debug("buscamos el docente por id")
                    print("Escribe el Id del docente a buscar:")
                    iddocente = input()
                    conn = conexion.conexionBDD(self)
                    query = f"select iddocente as IdDocente,nombreDocente as Nombre,apellidosDocente as Apellido from docente where IdDocente= '{iddocente}';"
                    resConn = conn.consultarBDD(query)

                    print("\tID\t\tNombres\t\tApellidos")
                    for row in resConn:
                        print(
                            f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

                    input("continuar???")
                    print(resConn)
                except Exception as error:
                    return False

            elif(resMenuDocente == 3):
                try:
                    log.debug("buscamos el docente")
                    conn = conexion.conexionBDD(self)
                    query = "select iddocente as IdDocente,nombreDocente as Nombre,apellidosDocente as Apellido from docente"
                    resConn = conn.consultarBDD(query)
                    print("Escoja el ID del docente que desea modificar:")
                    print("\tID\t\tNombres\t\tApellidos")
                    for row in resConn:
                        print(
                            f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

                    iddocente = input()
                    print("Escriba el Nuevo Nombre del docente:")
                    nombre = input()
                    print("Escriba el Nuevo Apelldio del docente")
                    apellido = input()
                    query = f"update docente set nombreDocente = '{nombre}', apellidosDocente = '{apellido}' where IdDocente = {iddocente};"
                    resConn = conn.ejecutarBDD(query)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif(resMenuDocente == 4):
                try:
                    print("## Creacion de un Docente ##")
                    print("Escriba el Nombre del Docente:")
                    nombre = input()
                    print("Escriba el Apellido del Docente:")
                    apellido = input()
                    conn = conexion.conexionBDD(self)
                    query = f"insert into docente (nombreDocente, apellidosDocente) values('{nombre}','{apellido}');"
                    resConn = conn.ejecutarBDD(query)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif(resMenuDocente == 5):
                try:
                    log.debug("eliminamos el docente")
                    conn = conexion.conexionBDD(self)
                    query = "select iddocente as IdDocente,nombreDocente as Nombre,apellidosDocente as Apellido from docente;"
                    resConn = conn.consultarBDD(query)
                    print("Escoja el ID del alumno que desea eliminar:")
                    print("\tID\t\tNombres\t\tApellidos")
                    for row in resConn:
                        print(
                            f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

                    iddocente = input()

                    query = f"delete from docente where IdDocente = {iddocente} ;"
                    resConn = conn.ejecutarBDD(query)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

        else:  # Si es dos entra a mongo
            print("Se ejecuto correctamente")
        

            dicMenuDocente = {"\t- Buscar Todos Los Docentes": 1,
                             "\t- Buscar Docente Por IDDocente": 2,
                             "\t- Modificar Docente Por Id": 3,
                             "\t- Crear Docente": 4,
                             "\t- Borrar Docente": 5}
            menuDocente = utils.Menu("Menu Docente", dicMenuDocente)
            resMenuDocente = menuDocente.mostrarMenu()
            if(resMenuDocente == 1):
                try:
                    log.debug("Obtenemos Lista de Docentes")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistros("docente",query)
                    print("Obteniendo Lista de Docentes...")
                  
                    print("\tID\t\tNombres\t\tApellidos")
                    for row in resConn:
                        print(f"\t{str(row['iddocente'])}\t\t{str(row['nombreDocente'])}\t\t{str(row['apellidosDocente'])}")
                    input("continuar???")
                    print(resConn)
                except Exception as error:
                    return False

            elif(resMenuDocente == 2):
                try:
                    log.debug("buscamos el docente por id")
                    print("Escribe el Id del docente a buscar:")
                    iddocente = input()
                    conn = conexion.conexionBDD(4)
                    resConn = conn.leerRegistro("docente",{'iddocente': iddocente})
                    #query = f"select iddocente as IdDocente,nombreDocente as Nombre,apellidosDocente as Apellido from docente where IdDocente= '{iddocente}';"
                    if resConn:
                        print("\tID\t\tNombres\t\tApellidos")
                        #print(f"\t{str(row['iddocente'])}\t\t{str(row['nombreDocente'])}\t\t{str(row['apellidosDocente'])}")
                        print(f"\t{str(resConn['iddocente'])}\t\t{str(resConn['nombreDocente'])}\t\t{str(resConn['apellidosDocente'])}")
                    else:
                        print("No existe resultado")
                    input("continuar???")
                    print(resConn)
                except Exception as error:
                    return False

            elif(resMenuDocente == 3):
                try:
                    log.debug("buscamos el docente")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistro("docente",query)
                    print("Escoja el ID del docente que desea modificar:")
                    print("\tID\t\tNombres\t\tApellidos")
                    for row in resConn:
                        print(f"\t{str(row['iddocente'])}\t\t{str(row['nombreDocente'])}\t\t{str(row['apellidosDocente'])}")
                        #print(f"\t{str(row['idcurso'])}\t\t{str(row['nombreCurso'])}\t\t{str(row['idsalon'])}\t\t{str(row['nombreSalon'])}")
                    iddocente = input()
                    print("Escriba el nuevo valor para el nombre del docente:")
                    nombre = input()
                    print("Escriba el nuevo valor para apellido del docente")
                    apellido = input()
                    nuevodocente = dict()
                    nuevodocente={'iddocente': (iddocente), 'nombreDocente': (nombre), 'apellidosDocente': (apellido)}
                    resConn =conn.actualizarRegistro('docente', {'iddocente': iddocente}, nuevodocente)
                    if(resConn):
                        print("Se actualizó correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif(resMenuDocente == 4):
                try:
                    print("## Creacion de un Docente ##")
                    print("Escriba codigo de Docente:")
                    iddocente = input()
                    print("Escriba el Nombre del Docente:")
                    nombre = input()
                    print("Escriba el Apellido del Docente:")
                    apellido = input()
                    conn = conexion.conexionBDD(4)
                    nuevodocente = dict()
                    nuevodocente={'iddocente': (iddocente), 'nombreDocente': (nombre), 'apellidosDocente': (apellido)}
                    resConn =conn.insertarRegistro('docente', nuevodocente)
                    if(resConn):
                        print("Se insertó correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif(resMenuDocente == 5):
                try:
                    log.debug("eliminamos el docente")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistros("docente", query)
                    print("Escoja el ID del docente que desea eliminar:")
                    print("\tID\t\tNombres\t\tApellidos")
                    for row in resConn:
                        print(
                            f"\t{str(row['iddocente'])}\t\t{str(row['nombreDocente'])}\t\t{str(row['apellidosDocente'])}")
                        #rint(f"\t{str(row['idalumno'])}\t\t{str(row['nombreAlumno'])}\t\t{str(row['apellidoAlumno'])}")
                    iddocente = input()
                    conn = conexion.conexionBDD(4)
                    eliminardocente = dict()
                    eliminardocente = {'iddocente': (iddocente)}
                    resConn = conn.eliminarRegistro('docente', eliminardocente)
                    if(resConn):
                        print("Se eliminó correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False