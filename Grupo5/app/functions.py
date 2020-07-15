from conn import Conexion
from classes import *
import time
import pymongo
from pymongo import MongoClient, errors
#FUNCIONES UTILES

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
            print("cod_grado\tdesc")
            for x in colec.find({},{"cod_grado": 1, "desc": 1}):
                print (str(x["cod_grado"]) + "\t\t" + x["desc"])
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
            print("Ya se ha configurado")
            time.sleep(3)
            break
        
def modificarGrados():
    os.system("cls")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = myclient["Hackaton_S7_G5"]
    colec = my_db["grados"]
    print("cod_grado\tdesc")
    for x in colec.find({},{"cod_grado": 1, "desc": 1}):
        print (str(x["cod_grado"]) + "\t\t" + x["desc"])
    while True:
        try:
            codGrado = int(input("Ingrese el codigo del Grado a modificar: "))
            break
        except:
            print("Error!: Ingrese un número entero positivo")
    nuevodescGrado = str(input(f"Ingresa la descripción del Grado {codGrado}: "))
    colec.update_one({ "cod_grado": codGrado },{ "$set": { "desc": f"{nuevodescGrado}"} })
    print("cod_grado\tdesc")
    for x in colec.find({},{"cod_grado": 1, "desc": 1}):
        print (str(x["cod_grado"]) + "\t\t" + x["desc"])
    print("Se modifico correctamente")
    time.sleep(2)
       
def eliminarGrados():
    os.system("cls")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = myclient["Hackaton_S7_G5"]
    colec = my_db["grados"]
    print("cod_grado\tdesc")
    for x in colec.find({},{"cod_grado": 1, "desc": 1}):
        print (str(x["cod_grado"]) + "\t\t" + x["desc"])
    while True:
        try:
            codGrado = int(input("Ingrese el codigo del Grado a eliminar: "))
            break
        except:
            print("Error!: Ingrese un número entero positivo")
    resConn = colec.delete_one(gradoDel)
    os.system("cls")
    print("cod_grado\tdesc")
    for x in colec.find({},{"cod_grado": 1, "desc": 1}):
        print (str(x["cod_grado"]) + "\t\t" + x["desc"])
    print("Se eliminó correctamente")
    time.sleep(2)

# fUNCIONES MANTENIMIENTO SALONES
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
       
def eliminarSalon():
    os.system("cls")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = myclient["Hackaton_S7_G5"]
    colec = my_db["salones"]
    print("cod_salon\tdesc")
    for x in colec.find({},{"cod_salon": 1, "desc": 1}):
        print (str(x["cod_salon"]) + "\t\t" + x["desc"])
    while True:
        try:
            codigoSalon = int(input("Ingrese el codigo del Salon a eliminar: "))
            break
        except:
            print("Error!: Ingrese un número entero positivo")
    resConn = colec.delete_one(salonDel)
    os.system("cls")
    print("cod_salon\tdesc")
    for x in colec.find({},{"cod_salon": 1, "desc": 1}):
        print (str(x["cod_salon"]) + "\t\t" + x["desc"])
    print("Se eliminó correctamente")
    time.sleep(2)
      
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
                        for x in range(numNotas):
                            colec.update({'cod_curso': codCurso},{'$set': {f"Nota {x+1} ": 0 }})  
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
        codCurso= int(input("Ingresa el codigo del CURSO que desea eliminar: "))
        resConn = colec.delete_one({"cod_curso": codCurso})
        os.system("cls")
        for x in colec.find({},{"cod_curso": 1, "nombre": 1, "cod_grado": 1, "numero_notas": 1}):
            print(x)
        print("Se eliminó correctamente")
        time.sleep(3)
        break

# CREAR PROFESOR
def crearProfesor():
    os.system("cls")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = myclient["Hackaton_S7_G5"]
    colec = my_db["profesores"]
    print("cod_profesor\tnombre\t\tapellido")
    for x in colec.find({},{"cod_profesor": 1, "nombre": 1, "apellido": 1}):
        print (str(x["cod_profesor"]) + "\t\t" + x["nombre"] + "\t\t" + x["apellido"])
    while True: 
        try:
            codigoprofesor = int(input("Ingrese el codigo del nuevo profesor: "))
            if 0 < codigoprofesor :
                break
            else:
                print("Error!: Ingrese un número entero positivo")
        except:
            print("Error!: Ingrese un número entero positivo")
    nombreprofesor = input("Ingrese el nombre del profesor: ")
    apellidoprofesor = input("Ingresde el apellido del profesor: ")
    dicProfesor = {"cod_profesor":codigoprofesor, "nombre":nombreprofesor, "apellido":apellidoprofesor}
    colec.insert_one(dicProfesor)
    print("cod_profesor\tnombre\t\tapellido")
    for x in colec.find({},{"cod_profesor": 1, "nombre": 1, "apellido": 1}):
        print (str(x["cod_profesor"]) + "\t\t" + x["nombre"] + "\t\t" + x["apellido"])
    time.sleep(2)
def modificarProfesor():
    os.system("cls")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = myclient["Hackaton_S7_G5"]
    colec = my_db["profesores"]
    print("cod_profesor\tnombre\t\tapellido")
    for x in colec.find({},{"cod_profesor": 1, "nombre": 1, "apellido": 1}):
        print (str(x["cod_profesor"]) + "\t\t" + x["nombre"] + "\t\t" + x["apellido"])
    while True:
        try:
            codProfesor = int(input("Ingrese el codigo del profesor a modificar: "))
            break
        except:
            print("Error!: Ingrese un número entero positivo")
    nuevoNombre = input("Ingrese el nuevo nombre para el profesor: ")
    nuevoApellido = input("Ingrese en nuevo apellido para el profesor: ")
    colec.update_one({ "cod_profesor": codProfesor },{ "$set": { "nombre": f"{nuevoNombre}","apellido": f"{nuevoApellido}"} })
    print("cod_profesor\tnombre\t\tapellido")
    for x in colec.find({},{"cod_profesor": 1, "nombre": 1, "apellido": 1}):
        print (str(x["cod_profesor"]) + "\t\t" + x["nombre"] + "\t\t" + x["apellido"])
    print("Se modifico correctamente")
    time.sleep(2)
def eliminarProfesor():
    os.system("cls")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = myclient["Hackaton_S7_G5"]
    colec = my_db["profesores"]
    print("cod_profesor\tnombre\t\tapellido")
    for x in colec.find({},{"cod_profesor": 1, "nombre": 1, "apellido": 1}):
        print (str(x["cod_profesor"]) + "\t\t" + x["nombre"] + "\t\t" + x["apellido"])
    while True:
        try:
            codProfesor = int(input("Ingrese el codigo del profesor a eliminar: "))
            break
        except:
            print("Error!: Ingrese un número entero positivo")
    resConn = colec.delete_one({"cod_profesor": codProfesor})
    os.system("cls")
    print("cod_profesor\tnombre\t\tapellido")
    for x in colec.find({},{"cod_profesor": 1, "nombre": 1, "apellido": 1}):
        print (str(x["cod_profesor"]) + "\t\t" + x["nombre"] + "\t\t" + x["apellido"])
    print("Se eliminó correctamente")
    time.sleep(2)
    
# CREAR ALUMNOS:
def crearAlumno():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = myclient["Hackaton_S7_G5"]
    colec = my_db["alumnos"]
    print("cod_alumno\tnombre\t\tapellido")
    for x in colec.find({},{"cod_alumno": 1, "nombre": 1, "apellido": 1}):
        print (str(x["cod_alumno"]) + "\t\t" + x["nombre"] + "\t\t" + x["apellido"])
    while True: 
        try:
            codigoAlumno = int(input("Ingrese el codigo del nuevo alumno: "))
            if 0 < codigoAlumno :
                break
            else:
                print("Error!: Ingrese un número entero positivo")
                pass
        except:
            print("Error!: Ingrese un número entero positivo")
    nombreAlumno = input("Ingrese el nombre del alumno: ")
    apellidoAlumno = input ("Ingrese el apellido del alumno: ")
    dicAlumno = {"cod_alumno":codigoAlumno, "nombre":nombreAlumno, "apellido":apellidoAlumno}
    colec.insert_one(dicAlumno)
    print("cod_alumno\tnombre\t\tapellido")
    for x in colec.find({},{"cod_alumno": 1, "nombre": 1, "apellido": 1}):
        print (str(x["cod_alumno"]) + "\t\t" + x["nombre"] + "\t\t" + x["apellido"])
    time.sleep(2)
def modificarAlumno():
    os.system("cls")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = myclient["Hackaton_S7_G5"]
    colec = my_db["alumnos"]
    print("cod_alumno\tnombre\t\tapellido")
    for x in colec.find({},{"cod_alumno": 1, "nombre": 1, "apellido": 1}):
        print (str(x["cod_alumno"]) + "\t\t" + x["nombre"] + "\t\t" + x["apellido"])
    while True:
        try:
            codAlumno = int(input("Ingrese el codigo del profesor a modificar: "))
            break
        except:
            print("Error!: Ingrese un número entero positivo")
    nuevoNombre = input("Ingrese el nuevo nombre para el profesor: ")
    nuevoApellido = input("Ingrese en nuevo apellido para el profesor: ")
    colec.update_one({ "cod_alumno": codAlumno },{ "$set": { "nombre": f"{nuevoNombre}","apellido": f"{nuevoApellido}"} })
    print("cod_alumno\tnombre\t\tapellido")
    for x in colec.find({},{"cod_alumno": 1, "nombre": 1, "apellido": 1}):
        print (str(x["cod_alumno"]) + "\t\t" + x["nombre"] + "\t\t" + x["apellido"])
    print("Se modifico correctamente")
    time.sleep(2)
def eliminarAlumno():  
    os.system("cls")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = myclient["Hackaton_S7_G5"]
    colec = my_db["alumnos"]
    print("cod_alumno\tnombre\t\tapellido")
    for x in colec.find({},{"cod_alumno": 1, "nombre": 1, "apellido": 1}):
        print (str(x["cod_alumno"]) + "\t\t" + x["nombre"] + "\t\t" + x["apellido"])
    while True:
        try:
            codAlumno = int(input("Ingrese el codigo del profesor a eliminar: "))
            break
        except:
            print("Error!: Ingrese un número entero positivo")
    resConn = colec.delete_one({"cod_alumno": codAlumno})
    os.system("cls")
    print("cod_alumno\tnombre\t\tapellido")
    for x in colec.find({},{"cod_alumno": 1, "nombre": 1, "apellido": 1}):
        print (str(x["cod_alumno"]) + "\t\t" + x["nombre"] + "\t\t" + x["apellido"])
    print("Se eliminó correctamente")
    time.sleep(2)











