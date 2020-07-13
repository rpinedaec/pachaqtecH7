#imports
import os
import pymongo
import time
# Definicion de clases
class Menu:
    def __init__(self, lstOpciones, strTitulo, strMenuDescr):
        self.lstOpciones = lstOpciones
        self.strTitulo = strTitulo
        self.strMenuDescr = strMenuDescr
        self.OptionSelect = 0
    def show(self):
        os.system("cls")
        print(f"\033[1;32;40m")
        print(20*":" + f"{self.strTitulo:^20}" + 20*":")
        print(20*":" + f"{self.strMenuDescr:^20}" + 20*":")
        for k, v in self.lstOpciones.items():
            print(k, "::", v)
        print("9 :: Salir")
        while True:
            try:
                self.OptionSelect = int(input("Ingrese su opción: "))
                if self.OptionSelect > 0 and self.OptionSelect < len(self.lstOpciones)+1:
                    return self.OptionSelect
                elif self.OptionSelect == 9:
                    break
                else:
                    print("Ingrese alguna de las opciones mostradas")
            except ValueError:
                print("Ingresa un número entero")

class Salon:
    def __init__(self, cod_salon, desc, cod_grado):
        self.cod_salon = cod_salon
        self.desc = desc
        self.cod_grado = cod_grado


# Definición de todos los menus:
menuPrincipal = Menu({1: "Cuadro de merito", 2: "Listar Docentes", 3: "Listar Alumnos", 4: "Crear Reporte", 5: "Mantenimiento"},
                     "Colegio Perez de Cuellas", "Menú Principal")                     
menuMantenimiento = Menu({1: "Alumnos",    2: "Docentes", 3: "Salones", 4: "Cursos", 5: "Notas", 6: "Periodo escolar"},
                   "Colegio Perez de Cuellas", "Menú Mantenimiento")
menuMantAlumnos = Menu({1: "Crear Alumno",    2: "Modificar Alumno", 3: "Eliminar Alumno"},
                   "Colegio Perez de Cuellas", "Menú mantenimiento Alumno")
menuMantDocentes = Menu({1: "Crear Docente",    2: "Modificar Docente", 3: "Eliminar Docente"},
                   "Colegio Perez de Cuellas", "Menú mantenimiento Docente")
menuMantSalones = Menu({1: "Crear Salón",    2: "Modificar Salón", 3: "Eliminar Salón"},
                   "Colegio Perez de Cuellas", "Menú mantenimiento Salon")
menuMantCursos = Menu({1: "Crear Curso",    2: "Modificar Curso", 3: "Eliminar Curso"},
                   "Colegio Perez de Cuellas", "Menú mantenimiento Curso")
menuMantNotas = Menu({1: "Crear Notas",    2: "Modificar Nota", 3: "Eliminar Nota"},
                   "Colegio Perez de Cuellas", "Menú mantenimiento Nota")
menuMantPeriodo = Menu({1: "Crear Periodo",    2: "Modificar Periodo", 3: "Eliminar Periodo"},
                   "Colegio Perez de Cuellas", "Menú mantenimiento Periodo")



    # elif(resMenuCliente == 3):
    #     log.debug("buscamos cliente")
    #     conn = conexion.conexionBDD(4)
    #     query = {}
    #     resConn = conn.leerRegistros("clientes",query)
    #     print("Escoja el ID del cliente que desea modificar")
    #     print("\tID\t\tNombre\t\t\tDNI\t\t\tDireccion")
    #     for row in resConn:
    #         print(f"\t{str(row['idCliente'])}\t\t{str(row['nombreCliente'])}\t\t{str(row['identificacionCliente'])}\t\t{str(row['direccionCliente'])}")

    #     idcliente = input()
    #     print("Escriba el nuevo valor para Nombre")
    #     nombre = input()
    #     print("Escriba el nuevo valor para DNI")
    #     dni = input()
    #     print("Escriba el nuevo valor para Direccion")
    #     direccion = input()
    #     nuevocliente = clientes.clientes('',nombre,dni,direccion)
    #     #query = f"update clientes set nombreCliente = '{nombre}', nroIdentidicacionCliente = '{dni}',direccionCliente = '{direccion}' where idCliente = {idcliente};"
    #     resConn = conn.insertarRegistro("clientes",nuevocliente)

    # def insertarRegistros(self, collection, data):
    #     conexion = self.conexion()
    #     doc = conexion[str(f"{collection}")]
    #     res = doc.insert_many(data).inserted_ids
    #     return res



def crearSalon():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["Salones"]
        for x in colec.find({},{"cod_salon": 1, "desc": 1, "cod_grado": 1}):
            print(x)
        codSalon = str(input("Crea un código para el  salón: "))
        codGrado = str(input("Ingresa el código del grado para el salón: "))
        desc = "SALON - " + codSalon
        dicSalon = {"cod_salon": codSalon,"desc": desc,"cod_grado": codGrado}
        resConn = colec.insert_one(dicSalon)
        os.system("cls")
        for x in colec.find({},{"cod_salon": 1, "desc": 1, "cod_grado": 1}):
            print(x)
        print("Se agregó correctamente")
        time.sleep(3)
        break

def modificarSalon():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["Salones"]
        for x in colec.find({},{"cod_salon": 1, "desc": 1, "cod_grado": 1}):
            print(x)
        codSalon= str(input("Ingresa el codigo del SALON que desea modificar: "))
        nuevCodGrad = str(input("Ingresa el nuevo codigo del grado para el SALON: "))
        salonMod = {"cod_salon": codSalon}
    
        colec.find_and_modify(salonMod, {"$set":{"cod_grado":nuevCodGrad}})
        os.system("cls")
        for x in colec.find({},{"cod_salon": 1, "desc": 1, "cod_grado": 1}):
            print(x)
        print("Se modifico correctamente")
        time.sleep(3)
        break


def eliminarSalon():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["Salones"]
        for x in colec.find({},{"cod_salon": 1, "desc": 1, "cod_grado": 1}):
            print(x)
        codSalon= str(input("Ingresa el codigo del SALON que desea eliminar: "))
        salonDel = {"cod_salon": codSalon}
        resConn = colec.delete_one(salonDel)
        os.system("cls")
        for x in colec.find({},{"cod_salon": 1, "desc": 1, "cod_grado": 1}):
            print(x)
        print("Se eliminó correctamente")
        time.sleep(3)
        break



# Menu de navegación
while True:
    intOptionSelect = menuPrincipal.show()
    if intOptionSelect == 1:  # Menu Cuadro de merito
        pass
    elif intOptionSelect == 2:  # Menu Listar Docente
        pass
    elif intOptionSelect == 3:  # Menu Listar Alumnos
        pass
    elif intOptionSelect == 4:  # Menu Crear Reporte
        pass
    elif intOptionSelect == 5:  # Menu Mantenimiento
        while True:
            intOptionSelect = menuMantenimiento.show()
            if intOptionSelect == 1:  # Mantenimiento Alumno
                while True:
                    intOptionSelect = menuMantAlumnos.show()
                    if intOptionSelect == 1: #Crear alumno
                        pass
                    elif intOptionSelect == 2: #modificar alumno
                        pass
                    elif intOptionSelect == 3: #Eliminar alumno
                        pass
                    else:
                        break
            elif intOptionSelect == 2:  # Mantenimiento Docente 
                while True:
                    intOptionSelect = menuMantDocentes.show()
                    if intOptionSelect == 1: #Crear Docente
                        pass
                    elif intOptionSelect == 2: #Modificar Docente
                        pass
                    elif intOptionSelect == 3: #Eliminar Docente
                        pass
                    else:
                        break
            elif intOptionSelect == 3:  # Mantenimiento Salones
                while True:
                    intOptionSelect = menuMantSalones.show()
                    if intOptionSelect == 1: #Crear Salon
                        crearSalon()
                    elif intOptionSelect == 2: #Modificar Salon
                        modificarSalon()
                    elif intOptionSelect == 3: #Eliminar Salon
                        eliminarSalon()
                    else:
                        break
            elif intOptionSelect == 4:  # Mantenimiento Cursos
                while True:
                    intOptionSelect = menuMantCursos.show()
                    if intOptionSelect == 1: #Crear curso
                        pass
                    elif intOptionSelect == 2: #Modificar curso
                        pass
                    elif intOptionSelect == 3: #Eliminar curso
                        pass
                    else:
                        break
            elif intOptionSelect == 5:  # Mantenimiento Notas
                while True:
                    intOptionSelect = menuMantNotas.show()
                    if intOptionSelect == 1: #Crear nota
                        pass
                    elif intOptionSelect == 2: #Modificar nota
                        pass
                    elif intOptionSelect == 3: #Eliminar nota
                        pass
                    else:
                        break
            elif intOptionSelect == 6:  # Mantenimiento Periodo Escolar
                while True:
                    intOptionSelect = menuMantPeriodo.show()
                    if intOptionSelect == 1: #Crear periodo
                        pass
                    elif intOptionSelect == 2: #Modificar periodo
                        pass
                    elif intOptionSelect == 3: #Eliminar periodo
                        pass
                    else:
                        break
            else:
                break
    else:
        break
