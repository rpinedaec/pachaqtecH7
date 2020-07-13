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

class Periodo:
    def __init__(self, cod_periodo, desc):
        self.cod_periodo = cod_periodo
        self.desc = desc
        
class Grados:
    def __init__(self, cod_grado, desc):
        self.cod_grado = cod_grado
        self.desc = desc
       

# Definición de todos los menus:
menuPrincipal = Menu({1: "Cuadro de merito", 2: "Listar Docentes", 3: "Listar Alumnos", 4: "Crear Reporte", 5: "Mantenimiento"},
                     "Colegio Perez de Cuellar", "Menú Principal")                     
menuMantenimiento = Menu({1: "Alumnos",    2: "Docentes", 3: "Salones", 4: "Cursos", 5: "Notas", 6: "Periodo escolar", 7: "Grados"},
                   "Colegio Perez de Cuellar", "Menú Mantenimiento")
menuMantAlumnos = Menu({1: "Crear Alumno",    2: "Modificar Alumno", 3: "Eliminar Alumno"},
                   "Colegio Perez de Cuellar", "Menú mantenimiento Alumno")
menuMantDocentes = Menu({1: "Crear Docente",    2: "Modificar Docente", 3: "Eliminar Docente"},
                   "Colegio Perez de Cuellar", "Menú mantenimiento Docente")
menuMantSalones = Menu({1: "Crear Salón",    2: "Modificar Salón", 3: "Eliminar Salón"},
                   "Colegio Perez de Cuellar", "Menú mantenimiento Salon")
menuMantCursos = Menu({1: "Crear Curso",    2: "Modificar Curso", 3: "Eliminar Curso"},
                   "Colegio Perez de Cuellar", "Menú mantenimiento Curso")
menuMantNotas = Menu({1: "Crear Notas",    2: "Modificar Nota", 3: "Eliminar Nota"},
                   "Colegio Perez de Cuellar", "Menú mantenimiento Nota")
menuMantPeriodo = Menu({1: "Crear Periodo",    2: "Modificar Periodo", 3: "Eliminar Periodo"},
                   "Colegio Perez de Cuellar", "Menú mantenimiento Periodo")
menuMantGrados = Menu({1: "Crear Grados",    2: "Modificar Grados", 3: "Eliminar Grados"},
                   "Colegio Perez de Cuellar", "Menú mantenimiento Grados")

def crearSalon():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["salones"]
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
        colec = my_db["salones"]
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
        colec = my_db["salones"]
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

def crearPeriodo():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["periodos"]
        for x in colec.find({},{"cod_periodo": 1, "desc": 1}):
            print(x)
        codPeriodo = str(input("Crea un código para el periodo: "))
        desc = "Periodo - " + codPeriodo
        dicPeriodo = {"cod_periodo": codPeriodo,"desc": desc}
        resConn = colec.insert_one(dicPeriodo)
        os.system("cls")
        for x in colec.find({},{"cod_periodo": 1, "desc": 1}):
            print(x)
        print("Se agregó correctamente")
        time.sleep(3)
        break
    
def modificarPeriodo():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["periodos"]
        for x in colec.find({},{"cod_periodo": 1, "desc": 1}):
            print(x)
        codPeriodo = str(input("Ingresa el codigo del PERIODO que desea modificar: "))
        nuevoCodPeriodo = str(input("Ingresa el NUEVO codigo del PERIODO: "))
        periodoMod = {"cod_periodo": codPeriodo}
    
        colec.find_and_modify(periodoMod, {"$set":{"cod_periodo":nuevoCodPeriodo}})
        os.system("cls")
        for x in colec.find({},{"cod_periodo": 1, "desc": 1}):
            print(x)
        print("Se modifico correctamente")
        time.sleep(3)
        break

def eliminarPeriodo ():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["periodos"]
        for x in colec.find({},{"cod_periodo": 1, "desc": 1}):
            print(x)
        codPeriodo = str(input("Ingresa el codigo del PERIODO que desea eliminar: "))
        periodoDel = {"cod_periodo": codPeriodo}
        resConn = colec.delete_one(periodoDel)
        os.system("cls")
        for x in colec.find({},{"cod_periodo": 1, "desc": 1}):
            print(x)
        print("Se eliminó correctamente")
        time.sleep(3)
        break

def crearGrados():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["grados"]
        for x in colec.find({},{"cod_grado": 1, "desc": 1}):
            print(x)
        codGrado = str(input("Crea un código para el grado: "))
        desc = codGrado + "-Primaria"
        dicGrado = {"cod_grado": codGrado,"desc": desc}
        resConn = colec.insert_one(dicGrado)
        os.system("cls")
        for x in colec.find({},{"cod_grado": 1, "desc": 1}):
            print(x)
        print("Se agregó correctamente")
        time.sleep(3)
        break

def modificarGrados():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["grados"]
        for x in colec.find({},{"cod_grado": 1, "desc": 1}):
            print(x)
        codGrado = str(input("Ingresa el codigo del GRADO que desea modificar: "))
        nuevoCodGrado = str(input("Ingresa el NUEVO codigo del GRADO: "))
        gradoMod = {"cod_grado": codGrado}
    
        colec.find_and_modify(gradoMod, {"$set":{"cod_grado":nuevoCodGrado}})
        os.system("cls")
        for x in colec.find({},{"cod_grado": 1, "desc": 1}):
            print(x)
        print("Se modifico correctamente")
        time.sleep(3)
        break

def eliminarGrados():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["grados"]
        for x in colec.find({},{"cod_grado": 1, "desc": 1}):
            print(x)
        codGrado= str(input("Ingresa el codigo del GRADO que desea eliminar: "))
        gradoDel = {"cod_grado": codGrado}
        resConn = colec.delete_one(gradoDel)
        os.system("cls")
        for x in colec.find({},{"cod_grado": 1, "desc": 1}):
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
                        crearPeriodo()
                    elif intOptionSelect == 2: #Modificar periodo
                        modificarPeriodo()
                    elif intOptionSelect == 3: #Eliminar periodo
                        eliminarPeriodo()
                    else:
                        break
            elif intOptionSelect == 7:  # Mantenimiento Grados
                while True:
                    intOptionSelect = menuMantGrados.show()
                    if intOptionSelect == 1: #Crear Grados
                        crearGrados()
                    elif intOptionSelect == 2: #Modificar Grados
                        modificarGrados()
                    elif intOptionSelect == 3: #Eliminar Grados
                        eliminarGrados()
                    else:
                        break
            else:
                break
    else:
        break
