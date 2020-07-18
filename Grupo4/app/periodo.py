import conexion
import utils
log = utils.log("INIT")
log.info("inicio del programa")

class periodo:
    def __init__(self, idperiodo, descperiodo):
        self.idperiodo = idperiodo
        self.descperiodo = descperiodo

          #Mantenimiento de la tabla periodo##
    def mantenimientoperiodo(self):
        if (self == 1):  # Si es uno ingresa a mysql
            dicMenuSalon = {"\t- Buscar Todos Los periodos ": 1,
                             "\t- Buscar periodo por ID": 2,
                             "\t- Modificar periodo de Clase Por Id": 3,
                             "\t- Crear periodo ": 4,
                             "\t- Borrar periodo": 5}
            menuSalon = utils.Menu("Menu Periodo ", dicMenuSalon)
            resMenuSalon = menuSalon.mostrarMenu()
           




        else:  # Si es dos entra a mongo
            dicMenuSalon = {"\t- Buscar Todos Los periodos en mongodb": 1,
                            "\t- Buscar periodo por ID en mongodb": 2,
                            "\t- Modificar periodo por Id en mongodb": 3,
                            "\t- Crear periodo en mongodb": 4,
                            "\t- Borrar periodo en mongodb": 5}
            menuSalon = utils.Menu("Menu Periodo ", dicMenuSalon)
            resMenuSalon = menuSalon.mostrarMenu()

            if(resMenuSalon == 1):
                try:
                    log.debug("buscamos el periodo")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistros("periodo",query)
                    
                    print("\tIDPeriodo\t\tPeriodo")
                    for row in resConn:
                       print(f"\t{str(row['idperiodo'])}\t\t{str(row['descperiodo'])}")
                    input("continuar???")
                    print(resConn)
                except Exception as error:
                    return False    

            elif(resMenuSalon == 2):
                try:
                    log.debug("buscamos el periodo por id")

                    print("Escribe el Id del periodo a buscar:")
                    codigo = input()
                    conn = conexion.conexionBDD(4)
                    #query = {}
                    resConn = conn.leerRegistro("periodo",{'idperiodo': codigo})
                    #resConn = conn.consultarBDD(query)
                    if resConn:
                        print("\tIDPeriodo\t\tPeriodo")
                        print(f"\t{str(resConn['idperiodo'])}\t\t{str(resConn['descperiodo'])}")
                    else:
                        print("No existe resultado")
                    input("continuar???")
                except Exception as error:
                    return False

            elif(resMenuSalon == 3):
                try:
                    log.debug("buscamos el periodo")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistros("periodo",query)
                    print("Escoja el ID del periodo que desea modificar:")
                    print("\tIDPeriodo\t\tPeriodo")

                    for row in resConn:
                        print(f"\t{str(row['idperiodo'])}\t\t{str(row['descperiodo'])}")
                    codigo = input()
                    print("Escriba el nuevo valor para el nombre del periodo:")
                    nombre = input()
                    nuevoperiodo = dict()
                    nuevoperiodo = {'descperiodo': (nombre)}
                    resConn = conn.actualizarRegistro('periodo', {'idperiodo': codigo}, nuevoperiodo)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False    

            elif(resMenuSalon == 4):
                try:
                    print("## Creacion de un Perido ##")
                    print ("Escriba el codigo de periodo")
                    codigo = input()
                    print("Escriba el Nombre del Periodo:")
                    nombre = input()
                    conn = conexion.conexionBDD(4)
                    nuevoperiodo = dict()
                    nuevoperiodo = {'idperiodo': (codigo), 'descperiodo': (nombre)}
                    resConn = conn.insertarRegistro("periodo",nuevoperiodo)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False

            elif(resMenuSalon == 5):
                try:
                    log.debug("eliminamos el periodo")
                    conn = conexion.conexionBDD(4)
                    query = {}
                    resConn = conn.leerRegistros("periodo",query)
                    print("\tIDPeriodo\t\tPeriodo")
                    for row in resConn:
                        print(f"\t{str(row['idperiodo'])}\t\t{str(row['descperiodo'])}")
                        
                    print("Escoja el ID del periodo que desea eliminar:")
                    codigo = input()
                    #conn = conexion.conexionBDD(4)
                    eliminarperiodo = dict()
                    eliminarperiodo = {'idperiodo': (codigo)}
                    resConn = conn.eliminarRegistro('periodo',eliminarperiodo)
                    if(resConn):
                        print("Se ejecuto correctamente")
                    else:
                        print("Hubo un error")

                    input("desea continuar???")
                except Exception as error:
                    return False                 
      