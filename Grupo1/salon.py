import conn

class salones:
    def mantenimiento_salones():
    dicM_Salones = {"Ver todos los salones": 1, "Buscar por No. de Salón": 2, "Modificar Salón por No. de Salón": 3, "Crear Salón": 4,"Borrar Salón": 5}
    menuM_Salones = Menu("Mantenimiento de Salones", dicM_Salones)
    resM_Salones = menuM_Salones.mostrarMenu()

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
        buscador_numero = input("Escribe el No. de salón a ubicar: ")
        conn.Connection.obtenerRegistro.collection = self.db[salones]
        conn.Connection.obtenerRegistro.condition = buscador_numero
        listar_salon = conn.Connection.obtenerRegistro()
        print("\tNo.\t\tNombre\t\t\tID Alumno\t\t\tID Profesor")
        print(listar_salon)
        print("")
        print ("-\t¿Desea volver al menu?"+
                "-\tVolver al menu: S-\t"+
                "-\tVolver a consultar: N")
        ver_salon = input("S/N: ")
        if (ver_salon=="S"):
        ver_salon =True
        while:
            #volver al menu
            else:
                ver_salon = False
                return buscador_numero
    elif(resM_Salones == 3):
        modificarsalon = True
        while:
            print("Escoja el ID del cliente que desea modificar")
            conn.Connection.obtenerRegistros.collection = self.db[salones]
            listar_salones = conn.Connection.obtenerRegistros()
            print("\tNo.\t\tNombre\t\t\tID Alumno\t\t\tID Profesor")
            for row in listar_salones:
                print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
            print("")
            print("Escriba el nuevo valor para No. Salon")
            id_salon = input()
            print("Escriba el nuevo valor para Nombre")
            nombre = input()
            conn.Connection.actualizarRegistro.collection = self.db[salones]
            post = {"_id"= '{id_salon}', "nombreSalon" = '{nombre}'}
            resM_Cambio = conn.Connection.actualizarRegistro()
            if(resM_Cambio):
                print("Éxito. Se actualizó el contacto")
            else:
                print("Hubo un error. Intente nuevamente.")
                return modificarsalon
    elif(resM_Salones == 4):
        nuevoingreso = True
        while:
            print("Para crear un nuevo registro, ingrese los siguientes datos:")
            id_salon = input("No. Salon: ")
            nombre = input("Nombre del salón: ")
            id_alumno = None
            id_profesor = None
            conn.Connection.insertRegistro(collection=self.db[salones])
            data = {'_id:'{id_salon}', nombreSalon: '{nombre}', idAlumno: '{id_alumno}', idProfesor: '{id_profesor}'}
            resM_NuevoSalon = conn.Connection.insertRegistro()
            if(resM_NuevoSalon):
                print("Exito. Se creo el nuevo resgitro")
                print("")
                print ("-\t¿Desea volver al menu?"+
                "-\tVolver al menu: S-\t"+
                "-\tIngresar nuevo registro: N")
                opcion_nuevosalon = input("S/N: ")
                if (opcion_nuevosalon=="S"):
                    opcion_nuevosalon =True
                else:
                    opcion_nuevosalon = False
                    return nuevoingreso
            else:
                nuevoingreso = False
                print("Hubo un error. Intente nuevamente")
                return nuevoingreso
    elif(resMenuCliente == 5):
        eliminarsalon = True
        while:
            print("Escoja el ID del cliente que desea eliminar")
            conn.Connection.obtenerRegistros.collection = self.db[salones]
            listar_salones = conn.Connection.obtenerRegistros()
            print("\tNo.\t\tNombre\t\t\tID Alumno\t\t\tID Profesor")
            for row in listar_salones:
                print(f"\t{str(row[0])}\t\t{str(row[1])}\t\t{str(row[2])}\t\t{str(row[3])}")
            print("")
            print("Escriba el No. Salon que desea eliminar")
            id_salon = input("Escribe el No.: ")
            conn.Connection.eliminarRegistro.condition = {"_id"= '{id_salon}'}
            resM_Borrar = conn.Connection.eliminarRegistro()
            if(resM_Borrar):
                print("Éxito. Se actualizó el contacto")
            else:
                print("Hubo un error. Intente nuevamente.")
                return eliminarsalon