from connection.conn import Connection
import menu

connection = Connection('mongodb+srv://paola:pachaqtec@pachaqtec.sdvq7.mongodb.net/test', 'pachacteq')

lstSalon=[]

class salones:

    collection = 'salones'

    def __init__(self, nombreSalon, idAlumno, idProfesor):
        self.nombreSalon = self.Salon
        self.idAlumno = self.Alumno
        self.idProfesor = self.Profesor
    
def mantenimiento_salones():
        dicM_Salones = {"Ver todos los salones": 1, "Buscar por No. de Salón": 2, "Modificar Salón por No. de Salón": 3, "Crear Salón": 4,"Borrar Salón": 5}
        menuM_Salones = menu.Menu("Mantenimiento de Salones", dicM_Salones)
        resM_Salones = menuM_Salones.mostrarMenu()
        if (resM_Salones == 1):
            listar_salones = Connection.obtenerRegistros(salones.collection)
            print(listar_salones)
            print("")
            print ("-\t¿Desea volver al menu?"+
                        "-\tVolver al menu: S-\t"+
                        "-\tVolver a consultar: N")
            ver_salones = input("S/N: ")
            if (ver_salones=="S"):
                mantenimiento_salones()
            else:
                return listar_salones

        elif (resM_Salones == 2):
            buscador_numero = input("Escribe el No. de salón a ubicar: ")
            listar_porsalon = Connection.obtenerRegistro(salones.collection, f'{buscador_numero}')
            print(listar_porsalon)
            print("")
            print ("-\t¿Desea volver al menu?"+
                        "-\tVolver al menu: S-\t"+
                        "-\tVolver a consultar: N")
            ver_salones = input("S/N: ")
            if (ver_salones=="S"):
                mantenimiento_salones()
            else:
                return buscador_numero

        elif (resM_Salones == 3):
            listar_salones = Connection.obtenerRegistros(salones.collection)
            print("Escoja el ID del cliente que desea modificar")
            print(listar_salones)
            print("")
            print("Ahora escriba el nuevo valor el No. de Salón")
            salones.Salon = input()
            salones.idAlumno = None
            salones.idProfesor = None
            resM_Cambio = Connection.actualizarRegistro(salones.collection, {
                                        'nombreSalon': salones.Salon,
                                        'idAlumno': salones.Alumno,
                                        'idProfesor': salones.Profesor
                                        })
            while(resM_Cambio):
                print("Éxito. Se actualizó el contacto")
                print ("-\t¿Desea volver al menu?"+
                        "-\tVolver al menu: S-\t"+
                        "-\tVolver a consultar: N")
                modificar_salones = input("S/N: ")
                if (modificar_salones=="S"):
                    mantenimiento_salones()
                elif (modificar_salones != "S"):
                    return listar_salones
                else:
                    print("Hubo un error. Intente nuevamente.")
                    return listar_salones
            
        elif (resM_Salones == 4):
            nuevoingreso = True
            while (nuevoingreso):
                print("Para crear un nuevo registro, ingrese los siguientes datos:")
                salones.Salon = input("Nombre del salón: ")
                salones.Alumno = None
                salones.Profesor = None
                resM_NuevoSalon = Connection.insertRegistro(salones.collection, {
                                            'nombreSalon': salones.Salon,
                                            'idAlumno': salones.Alumno,
                                            'idProfesor': salones.Profesor
                                            })
                print("Exito. Se creo el nuevo resgitro")
                print("")
                print ("-\t¿Desea volver al menu?"+
                            "-\tVolver al menu: S-\t"+
                            "-\tIngresar nuevo registro: N")
                opcion_nuevosalon = input("S/N: ")
                if (opcion_nuevosalon=="S"):
                    mantenimiento_salones()
                elif (opcion_nuevosalon !="S"):
                    return nuevoingreso
                else:
                    nuevoingreso = False
                    print("Hubo un error. Intente nuevamente")
                    return nuevoingreso
                    
        elif (resM_Salones == 5):
            eliminarsalon = True
            while (eliminarsalon):
                print("Escoja el ID del cliente que desea eliminar")
                listar_salones = Connection.obtenerRegistros(salones.collection)
                print(listar_salones)
                print("")
                print("Ahora scriba el No. Salon que desea eliminar")
                salones.Salon = input("Escribe el No.: ")
                resM_Borrar = connection.eliminarRegistro(salones.collection, {
                                        'nombreSalon': salones.Salon,
                                        })
                if(resM_Borrar):
                    print("Éxito. Se borró el salón")
                    print("")
                    print ("-\t¿Desea volver al menu?"+
                            "-\tVolver al menu: S-\t"+
                            "-\tIngresar nuevo registro: N")
                    opcion_borrar = input("S/N: ")
                    if (opcion_borrar=="S"):
                        mantenimiento_salones()
                    elif (opcion_nuevosalon !="S"):
                        return eliminarsalon
                else:
                    print("Hubo un error. Intente nuevamente")
                    return eliminarsalon

mantenimiento_salones()