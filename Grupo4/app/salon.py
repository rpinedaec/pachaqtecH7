import conexion
import utils
log = utils.log("INIT")
log.info("inicio del programa")
class salon:
    def __init__(self, idsalon, nombresalon):
        self.idsalon = idsalon
        self.nombresalon = nombresalon
        
    #Mantenimiento de la tabla salon##
    def mantenimientosalon(self):
        if (self == 1):  # Si es uno ingresa a mysql
            dicMenuSalon = {"\t- Buscar Todos Los Salones de Clases": 1,
                             "\t- Buscar Salon de Clase por ID": 2,
                             "\t- Modificar Salon de Clase Por Id": 3,
                             "\t- Crear Salon de Clase": 4,
                             "\t- Borrar Salon de Clase": 5}
            menuSalon = utils.Menu("Menu Salones de Clases", dicMenuSalon)
            resMenuSalon = menuSalon.mostrarMenu()
            if(resMenuSalon == 1):
                try:
                    log.debug("buscamos el salon")
                    conn = conexion.conexionBDD(self)
                    query = "select idsalon as IdSalon, nombreSalon as Descripcion from salon;"
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
            print("Se ejecuto correctamente")
