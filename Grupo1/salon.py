from connection.conn import Connection
import menu
from bson.json_util import dumps
from pymongo import MongoClient, errors
from tabulate import tabulate

Connection = Connection(
    'mongodb+srv://paola:pachaqtec@pachaqtec.sdvq7.mongodb.net/test', 'pachacteq')

lstSalon = []


class salones:

    collection = 'salones'

    def __init__(self, nombreSalon, idAlumno, idProfesor):
        self.nombreSalon = nombreSalon
        self.idAlumno = idAlumno
        self.idProfesor = idProfesor


def mantenimiento_salones():
    dicM_Salones = {"Ver todos los salones": 1,
                    "Modificar Salón por No. de Salón": 2, "Crear Salón": 3, "Borrar Salón": 4, "Salir Menu": 5}
    menuM_Salones = menu.Menu("Mantenimiento de Salones", dicM_Salones)
    resM_Salones = menuM_Salones.mostrarMenu()
    if (resM_Salones == 1):
        listar_salones = Connection.obtenerRegistros(salones.collection)
        table = []
        listar_salones = list(listar_salones)
        for i in range(len(listar_salones)):
            table.append([listar_salones[i]['_id'],
                          listar_salones[i]['nombreSalon']])

        print(tabulate(table, headers=[
              "Id Salon", "Nombre Salon"], tablefmt='fancy_grid'))
        print("-\t¿Desea volver al menu?" +
              "-\tVolver al menu: S-\t" +
              "-\tVolver a consultar: N")
        ver_salones = input("S/N: ")
        if (ver_salones == "S"):
            mantenimiento_salones()
        else:
            return listar_salones

    elif (resM_Salones == 2):
        ingresado = True
        while ingresado:
            listar_salones = Connection.obtenerRegistros(salones.collection)
            table = []
            listar_salones = list(listar_salones)
            for i in range(len(listar_salones)):
                table.append([listar_salones[i]['_id'],
                              listar_salones[i]['nombreSalon']])
            print(tabulate(table, headers=[
                  "Id Salon", "Nombre Salon"], tablefmt='fancy_grid'))
            print("Seleccion Nombre de Salon a modificar")
            nombreSalon = input()
            idSalon = Connection.obtenerRegistro(
                "salones", {'nombreSalon': nombreSalon})

            if idSalon == None:
                print("Intente de nuevo. Nombre Salon no existe oye")

            else:
                id_ = idSalon['_id']
                print("Con que valor desea cambiar el nombre")
                valorActualizar = input()
                Connection.actualizarRegistro("salones", {'_id': id_}, {
                                              'nombreSalon': valorActualizar})
                print("Valor actualizado")
                ingresado = False

    elif (resM_Salones == 3):

        # print(dumps(listar_salones,indent=2))
        print("Tabla Profesores")
        mostrar_profesor = Connection.obtenerRegistros('profesores')
        mostrar_profesor = list(mostrar_profesor)
        table = []

        for i in range(len(mostrar_profesor)):
            table.append([mostrar_profesor[i]["_id"],
                          mostrar_profesor[i]["nombreProfesor"]])

        ingresar = True
        while ingresar:
            print(tabulate(table, headers=[
                  "Id Profesor", "Nombre Profesor"], tablefmt='fancy_grid'))
            print("Ahora escriba el nombre del Profesor")

            nombreProfesor = input()

            idProfesor = Connection.obtenerRegistro(
                'profesores', {'nombreProfesor': nombreProfesor})

            print(type(idProfesor))
            # print(idProfesor)

            if idProfesor == None:
                print(idProfesor)
                print("Intente de nuevo oye")
            else:
                ingresar = False

        print("Ingrese el nombre del Salon")
        nombreSalon = input()
        Connection.insertRegistro('salones', {
            'nombreSalon': nombreSalon,
            'idProfesor': idProfesor['_id']
        })
        print("Ingresado")

    elif (resM_Salones == 4):
        ingresado = True
        while ingresado:
            listar_salones = Connection.obtenerRegistros(salones.collection)
            table = []
            listar_salones = list(listar_salones)
            for i in range(len(listar_salones)):
                table.append([listar_salones[i]['_id'],
                              listar_salones[i]['nombreSalon']])
            print(tabulate(table, headers=[
                  "Id Salon", "Nombre Salon"], tablefmt='fancy_grid'))
            print("Seleccion Nombre de Salon a borrar")
            nombreSalon = input()
            idSalon = Connection.obtenerRegistro(
                "salones", {'nombreSalon': nombreSalon})

            if idSalon == None:
                print("Intente de nuevo. Nombre Salon no existe oye")

            else:
                id_ = idSalon['_id']
                Connection.eliminarRegistro("salones", {'_id': id_})
                print("Registro Eliminado")
                ingresado = False

    elif resM_Salones == 5:
        Connection.cerrarConexion()
