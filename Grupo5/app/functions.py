from conn import Conexion
from classes import *
import time
import pymongo
from pymongo import MongoClient, errors
#FUNCIONES UTILES

# FUNCIONES MANTENIMIENTO SALON
def crearSalon():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["salones"]
        for x in colec.find({},{"cod_salon": 1, "desc": 1, "cod_grado": 1}):
            print(x)
        try: 
            codSalon = int(input("Crea un código para el  salón: "))
            codexiste = bool(colec.find_one({"cod_salon":codSalon}))
            if codexiste:
                print(f"Ya existe un salon con codigo {codSalon}")
                time.sleep(2)
                break
            colec = my_db["grados"]
            for x in colec.find({},{"cod_grado": 1, "desc": 1}):
                print(x)
            colec = my_db["salones"]
            codGrado = int(input("Ingresa el código del grado para el salón: "))
            desc = "SALON - " + str(codSalon)
            dicSalon = {"cod_salon": codSalon,"desc": desc,"cod_grado": codGrado}
            resConn = colec.insert_one(dicSalon)
            os.system("cls")
            for x in colec.find({},{"cod_salon": 1, "desc": 1, "cod_grado": 1}):
                print(x)
            print("Se agregó correctamente")
            time.sleep(2)
        except:
            print(f"Error inesperado")
            time.sleep(2)
        break 
def modificarSalon():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["salones"]
        for x in colec.find({},{"cod_salon": 1, "desc": 1, "cod_grado": 1}):
            print(x)
        codSalon= int(input("Ingresa el codigo del SALON que desea modificar: "))
        nuevoCodGrad = int(input("Ingresa el nuevo codigo del grado para el SALON: "))
        nuevoDesc = input("Ingrese una nueva descripción: ")
        colec.update({"cod_salon": codSalon}, {"$set":{"desc":nuevoDesc, "cod_grado":nuevoCodGrad}})
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

# FUNCIONES MANTENIMIENTO PERIODO
def crearPeriodo():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["periodos"]
        try:    
            numPeriodos = int(input("Ingrese el número de periodos que estara divido el año escolar(1-4): "))
            if 0 < numPeriodos < 5 :
                for i in range(numPeriodos):
                    resConn = colec.insert_one({"cod_periodo":(i+1), "desc":f"Periodo - {i+1}"})
                os.system("cls")
                for x in colec.find({},{"cod_periodo": 1, "desc": 1}):
                    print(x)
                print("Se agregó correctamente")
                time.sleep(2)
            else:
                print("Ingrese un número entero de 1 a 4")
                time.sleep(2)
        except errors.DuplicateKeyError:
            print("Error!: Objeto duplicado, elimine todos los periodos y vuelva a intentar")
            time.sleep(2)  
        except:
            print("Error inesperado")
            time.sleep(2)        
        break
def modificarPeriodo():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["periodos"]
        for x in colec.find({},{"cod_periodo": 1, "desc": 1}):
            print(x)
        codPeriodo = int(input("Ingresa el codigo del PERIODO que desea modificar: "))
        nuevodescPeriodo = str(input(f"Ingresa la descripción del PERIODO {codPeriodo}: "))
        colec.update({ "cod_periodo": codPeriodo }, {"$set":{"desc": nuevodescPeriodo}})
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
        codPeriodo = int(input("Ingresa el codigo del PERIODO que desea eliminar: "))
        periodoDel = {"cod_periodo": codPeriodo}
        resConn = colec.delete_one(periodoDel)
        os.system("cls")
        for x in colec.find({},{"cod_periodo": 1, "desc": 1}):
            print(x)
        print("Se eliminó correctamente")
        time.sleep(3)
        break

# fUNCIONES MANTENIMIENTO GRADOS
def crearGrados():
    while True:
        try: 
            os.system("cls")
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            my_db = myclient["Hackaton_S7_G5"]
            colec = my_db["grados"]
            while True: 
                Primaria = input("¿El colegio brindara educación primaria? S/N: ")
                if Primaria == "S":
                    for i in range(6):
                            resConn = colec.insert_one({"cod_grado":(i+1), "desc":f"{i+1} - Primaria"}) 
                    break            
                elif Primaria == "N":
                    break
                else: 
                    print( "Digite S o N")
            while True: 
                Secundaria = input("¿El colegio brindara educación Secundaria? S/N: ")
                if Secundaria == "S":
                    for i in range(5):
                            resConn = colec.insert_one({"cod_grado":(7+i), "desc":f"{i+1} - Secundaria"}) 
                    break               
                elif Secundaria == "N":
                    break
                else: 
                    print( "Digite S o N")          
            for x in colec.find({},{"cod_grado": 1, "desc": 1}):
                print(x)
            print("Se agregó correctamente")
            time.sleep(3)
            break
        except:
            print("Ya se ah configurado")
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
        codGrado = int(input("Ingresa el codigo del GRADO que desea modificar: "))
        nuevodescGrado = str(input(f"Ingresa la descripción del Grado {codGrado}: "))
        colec.update({ "cod_grado": codGrado}, {"$set":{"desc": nuevodescGrado}})
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
        codGrado = int(input("Ingresa el codigo del GRADO que desea eliminar: "))
        gradoDel = {"cod_grado": codGrado}
        resConn = colec.delete_one(gradoDel)
        os.system("cls")
        for x in colec.find({},{"cod_grado": 1, "desc": 1}):
            print(x)
        print("Se eliminó correctamente")
        time.sleep(3)
        break
  
# FUNCIONES MANTENIMIENTO CURSOS
def crearCurso():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["cursos"]
        for x in colec.find({},{"cod_curso": 1, "nombre": 1, "cod_grado": 1, "numero_notas": 1}):
            print(x)
        while True:
            try:
                codCurso = int(input("Crea un código para el  Curso: "))
                codexiste = bool(colec.find_one({"cod_curso":codCurso}))
                if codexiste :
                    print(f"Ya existe un curso con codigo {codCurso}")
                    time.sleep(2)
                else:
                    break
            except:
                print("Ingrese un número entero para el cod_curso")
        nombreCurso = str(input("Ingresa el nombre del curso: "))
        #Mostar todos los grados
        colec = my_db["grados"]
        for x in colec.find({},{"cod_grado": 1, "desc": 1}):
            print(x)
        while True:
            try:
                colec = my_db["grados"]
                codGrado = int(input("Ingrese el codigo del grado donde se dictara el curso: "))
                codexiste = bool(colec.find_one({"cod_grado":codGrado}))
                colec = my_db["cursos"]
                if codexiste :
                    while True:
                        try:
                            numNotas = int(input("Ingrese la cantidad de notas que tendra el curso: "))
                            break
                        except:
                            print("Ingrese un numero entero")
                            time.sleep(2)
                    dicCurso = {"cod_curso": codCurso,"nombre": nombreCurso,"cod_grado": codGrado, "numero_notas": numNotas}
                    try:
                        resConn = colec.insert_one(dicCurso)
                        os.system("cls")
                        for x in colec.find({},{"cod_curso": 1, "nombre": 1, "cod_grado": 1, "numero_notas": 1}):
                            print(x)
                        print("Se agregó correctamente")
                        time.sleep(2)
                        break
                    except:
                        print(f"Ya existe un curso con codigo {codCurso}")
                        time.sleep(2)
                else: 
                    print("El grado indicado no existe")
                    time.sleep(2)  
            except:
                print("Ingrese el cod_grado correctamente")    
                time.sleep(2)  
        break           
def modificarCursos():
   while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["cursos"]
        for x in colec.find({},{"cod_curso": 1, "nombre": 1, "cod_grado": 1, "numero_notas": 1}):
            print(x)
        codCurso = str(input("Ingresa el codigo del CURSO que desea modificar: "))
        nuevoNombre = str(input("Ingresa el NUEVO nombre del CURSO: "))
        nuevoCodgrado = str(input("Ingresa el NUEVO codigó grado del CURSO: "))
        nuevoNumnotas = int(input("Ingrese el nuevo numero de notas: "))
        colec.update_one({ "cod_curso": f"{codCurso}" },{ "$set": { "nombre": f"{nuevoNombre}","cod_grado": f"{nuevoCodgrado}", "numero_notas": f"{nuevoNumnotas}" } })
        os.system("cls")
        for x in colec.find({},{"cod_curso": 1, "nombre": 1, "cod_grado": 1, "numero_notas": 1}):
            print(x)
        print("Se modifico correctamente")
        time.sleep(3)
        break
def eliminarCursos():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["cursos"]
        for x in colec.find({},{"cod_curso": 1, "nombre": 1, "cod_grado": 1, "numero_notas": 1}):
            print(x)
        codCurso= str(input("Ingresa el codigo del CURSO que desea eliminar: "))
        resConn = colec.delete_one({"cod_curso": f"{codCurso}"})
        os.system("cls")
        for x in colec.find({},{"cod_curso": 1, "nombre": 1, "cod_grado": 1, "numero_notas": 1}):
            print(x)
        print("Se eliminó correctamente")
        time.sleep(3)
        break