import conn

class salones:
    def mantenimiento_salones():
    dicM_Salones = {"Ver todos los salones": 1, "Buscar por No. de Salón": 2, "Modificar Cliente por No. de Salón": 3, "Crear Salón": 4,"Borrar Salón": 5}
    # menuM_Salones = Menu("Mantenimiento de Salones", dicM_Salones)
    # resM_Salones = menuM_Salones.mostrarMenu()

    if(resM_Salones == 1):
        conn.Connection.obtenerRegistros.collection = self.db[salones]
        listar_salones = conn.Connection.obtenerRegistros()
        print("\tNo.\t\tNombre\t\t\tID Alumno\t\t\tID Profesor")
        print(listar_salones)
        print("")
        print ("-\t¿Desea volver al menu?"+
                "-\tVolver al menu: S-\t"+
                "-\tVolver a consultar: N")
        ver_salones = input("S/N: ")
        if (ver_salones=="S"):
        ver_salones =True
        while:
            #volver al menu
            else:
                ver_salones = False
                return listar_salones
    elif(resM_Salones == 2):
        conn.Connection.obtenerRegistro.collection = self.db[salones]
        conn.Connection.obtenerRegistro.condition = 
        listar_salones = conn.Connection.obtenerRegistros()
        print("\tNo.\t\tNombre\t\t\tID Alumno\t\t\tID Profesor")
        print(listar_salones)
        print("")
        print ("-\t¿Desea volver al menu?"+
                "-\tVolver al menu: S-\t"+
                "-\tVolver a consultar: N")
        ver_salones = input("S/N: ")
        if (ver_salones=="S"):
        ver_salones =True
        while:
            #volver al menu
            else:
                ver_salones = False
                return listar_salones
    elif(resMenuCliente == 3):
        log.debug("buscamos cliente")
        #Se abre la conexion con la base de datos
        conn = conexion.conexionBDD(1)
        #Se brinda la instruccion de la base de datos
        query = "select idClientes, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;"
        #Devuelve el resultado de la conexion
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del cliente que desea modificar")
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idcliente = input()
        print("Escriba el nuevo valor para Nombre")
        nombre = input()
        print("Escriba el nuevo valor para DNI")
        dni = input()
        print("Escriba el nuevo valor para Direccion")
        direccion = input()
        query = f"UPDATE clientes SET nombreCliente = '{nombre}', nroIdentificacionCliente = '{dni}',direccionCliente = '{direccion}' where idClientes = '{idcliente}';"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")

    elif(resMenuCliente == 4):
        print("##Creacion de un cliente##")
        print("Escriba el Nombre del Cliente")
        nombre = input()
        print("Escriba el DNI del Cliente")
        dni = input()
        print("Escriba el Direccion del Cliente")
        direccion = input()
        conn = conexion.conexionBDD(1)
        query = f"insert into clientes (nombreCliente, nroIdentificacionCliente,direccionCliente) values('{nombre}','{dni}','{direccion}');"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")


    elif(resMenuCliente == 5):
        log.debug("eliminamos cliente")
        conn = conexion.conexionBDD(1)
        query = "select idClientes, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;"
        resConn = conn.consultarBDD(query)
        print("Escoja el ID del cliente que desea eliminar")
        print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
        for row in resConn:
            print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")

        idcliente = input()
        
        query = f"delete from clientes where idCliente = {idcliente} ;"
        resConn = conn.ejecutarBDD(query)
        if(resConn):
            print("Se ejecuto correctamente")
        else:
            print("Hubo un error")
        
        input("desea continuar???")