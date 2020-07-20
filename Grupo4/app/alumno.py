import conexion
import utils
from time import sleep

log = utils.log("INIT")
log.info("inicio del programa")
class alumno:
    def __init__(self, idalumno, nombrealumno, apellidoalumno):
        self.idalumno = idalumno
        self.nombrealumno = nombrealumno
        self.apellidoalumno = apellidoalumno
    
    # def toDic(self):
    #     d = {
    #         "idalumno": self.idalumno,
    #         "nombrealumno": self.nombrealumno,
    #         "apellidoalumno": self.apellidoalumno
    #     }
    #    return d

    #Mantenimiento de la tabla alumno##
    def mantenimientoalumno(self):
        if (self == 1):  # Si es uno ingresa a mysql
            dicMenuAlumno = {"\t- Buscar Todos Los Alumnos": 1,
                            "\t- Buscar Alumno Por IDAlumno": 2,
                            "\t- Modificar Alumno Por Id": 3,
                            "\t- Crear Alumno": 4,
                            "\t- Borrar Alumno": 5}
            menuAlumno = utils.Menu("Menu Alumno", dicMenuAlumno)
            resMenuAlumno = menuAlumno.mostrarMenu()
            if(resMenuAlumno == 1):
                try:
                        log.debug("buscamos el alumno")
                        conn = conexion.conexionBDD(1)
                        query = "select idalumno as ID,nombreAlumno as Nombres ,apellidoAlumno as Apellidos from alumno;"
                        resConn = conn.consultarBDD(query)

                        print("\tID\t\tNombres\t\tApellidos")
                        for row in resConn:
                            print(
                                    f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")
                        input("continuar???")
                        #print(resConn)     
                except Exception as error:
                        return False
                
            elif(resMenuAlumno == 2):
                try:
                    log.debug("buscamos el alumno por id")
                    print("Escribe el Id del alumno a buscar:")
                    idalumno = input()
                    conn = conexion.conexionBDD(1)
                    query = f"select idalumno as ID,nombreAlumno as Nombres ,apellidoAlumno as Apellidos from alumno where idalumno= '{idalumno}';"
                    resConn = conn.consultarBDD(query)

                    print("\tID\t\tNombres\t\tApellidos")
                    for row in resConn:
                        print(
                            f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

                    input("continuar???")
                    print(resConn)
                except Exception as error:
                    return False
                
            elif(resMenuAlumno == 3):
                try:
                    log.debug("buscamos el alumno")
                    conn = conexion.conexionBDD(1)
                    query = "select idalumno as ID,nombreAlumno as Nombres ,apellidoAlumno as Apellidos from alumno;"
                    resConn = conn.consultarBDD(query)
                    print("Escoja el ID del alumno que desea modificar:")
                    print("\tID\t\tNombres\t\tApellidos")
                    for row in resConn:
                        print(
                            f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

                    idalumno = input()
                    print("Escriba el nuevo valor para el nombre del alumno:")
                    nombre = input()
                    print("Escriba el nuevo valor para apellido del alumno")
                    apellido = input()
                    query = f"update alumno set nombreAlumno = '{nombre}', apellidoAlumno = '{apellido}' where idalumno = {idalumno};"
                    resConn = conn.ejecutarBDD(query)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False
                
            elif(resMenuAlumno == 4):
                try:
                    print("## Creacion de un Alumno ##")
                    print("Escriba el Nombre del Alumno:")
                    nombre = input()
                    print("Escriba el Apellido del Alumno:")
                    apellido = input()
                    conn = conexion.conexionBDD(1)
                    query = f"insert into alumno (nombreAlumno, apellidoAlumno) values('{nombre}','{apellido}');"
                    resConn = conn.ejecutarBDD(query)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False
                
            elif(resMenuAlumno == 5):
                try:
                    log.debug("eliminamos el alumno")
                    conn = conexion.conexionBDD(1)
                    query = "select idalumno as ID,nombreAlumno as Nombres ,apellidoAlumno as Apellidos from alumno;"
                    resConn = conn.consultarBDD(query)
                    print("Escoja el ID del alumno que desea eliminar:")
                    print("\tID\t\tNombres\t\tApellidos")
                    for row in resConn:
                        print(
                            f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}")

                    idalumno = input()

                    query = f"delete from alumno where idCliente = {idalumno} ;"
                    resConn = conn.ejecutarBDD(query)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False
                
        else: #Si es dos entra a mongo
            print("Se ejecuto correctamente")
            dicMenuAlumno = {"\t- Buscar Todos Los Alumnos en mongodb": 1,
                            "\t- Buscar Alumno Por IDAlumno en mongodb": 2,
                            "\t- Modificar Alumno Por Id en mongodb": 3,
                            "\t- Crear Alumno en mongodb": 4,
                            "\t- Borrar Alumno en mongodb": 5}
            menuAlumno = utils.Menu("Menu Alumno", dicMenuAlumno)
            resMenuAlumno = menuAlumno.mostrarMenu()    
            
            if(resMenuAlumno == 1):
                try:
                    log.debug("buscamos el alumno")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistros("alumno",query)
                    print("\tID\t\tNombres\t\tApellidos")
                    for row in resConn:
                        print(f"\t{str(row['idalumno'])}\t\t{str(row['nombreAlumno'])}\t\t{str(row['apellidoAlumno'])}")
                    input("continuar???")
                    print(resConn)  
                    #sleep(10)

                except Exception as error:
                        return False

            elif(resMenuAlumno == 2):            
                try:
                    log.debug("buscamos el alumno por id")

                    print("Escribe el Id del alumno a buscar:")
                    codigo = input()
                    conn = conexion.conexionBDD(4)
                    #query = {}
                    resConn = conn.leerRegistro("alumno",{'idalumno': codigo})
                    #resConn = conn.consultarBDD(query)
                    if resConn:
                        print("\tID\t\tNombres\t\tApellidos")
                        print(f"\t{str(resConn['idalumno'])}\t\t{str(resConn['nombreAlumno'])}\t\t{str(resConn['apellidoAlumno'])}")
                    else:
                        print("No existe resultado")                        
                    input("continuar???")
                    #print(resConn)
                except Exception as error:
                    return False

            elif(resMenuAlumno == 3):
                try:
                    log.debug("buscamos el alumno")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistros("alumno",query)
                    print("Escoja el ID del alumno que desea modificar:")
                    print("\tID\t\tNombres\t\tApellidos")
                    for row in resConn:
                        print(f"\t{str(row['idalumno'])}\t\t{str(row['nombreAlumno'])}\t\t{str(row['apellidoAlumno'])}")

                    codigo = input()
                    print("Escriba el nuevo valor para el nombre del alumno:")
                    nombre = input()
                    print("Escriba el nuevo valor para apellido del alumno")
                    apellido = input()
                    nuevoalumno = dict()
                    nuevoalumno = {'idalumno': (codigo), 'nombreAlumno': (nombre), 'apellidoAlumno': (apellido)}
                    resConn = conn.actualizarRegistro('alumno', {'idalumno': codigo}, nuevoalumno)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False
            elif (resMenuAlumno == 4):
                try:
                    print("## Creacion de un Alumno ##")
                    print ("Escriba el codigo de alumno")
                    codigo = input()
                    print("Escriba el Nombre del Alumno:")
                    nombre = input()
                    print("Escriba el Apellido del Alumno:")
                    apellido = input()
                    conn = conexion.conexionBDD(4)
                    nuevoalumno = dict()
                    nuevoalumno = {'idalumno': (codigo), 'nombreAlumno': (nombre), 'apellidoAlumno': (apellido)}
                    resConn = conn.insertarRegistro("alumno",nuevoalumno)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif (resMenuAlumno == 5):
                try:
                    log.debug("eliminamos el alumno")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistros("alumno",query)
                    print("\tID\t\tNombres\t\tApellidos")
                    for row in resConn:
                        print(f"\t{str(row['idalumno'])}\t\t{str(row['nombreAlumno'])}\t\t{str(row['apellidoAlumno'])}")
                    print("Escoja el ID del alumno que desea eliminar:")
                    codigo = input()
                    #conn = conexion.conexionBDD(4)
                    eliminaralumno = dict()
                    eliminaralumno = {'idalumno': (codigo)}
                    resConn = conn.eliminarRegistro('alumno',eliminaralumno)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False 
                    