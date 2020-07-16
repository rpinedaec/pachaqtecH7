from conn import Conexion
from classes import *
import time
import pymongo
from pymongo import MongoClient, errors

# FUNCIONES MANTENIMIENTO SALON
def crearSalon():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["salones"]
        for x in colec.find({},{"cod_salon": 1, "desc": 1}):
            print(x)
        try: 
            codSalon = int(input("Crea un código para el  salón: "))
            codexiste = bool(colec.find_one({"cod_salon":codSalon}))
            if codexiste:
                print(f"Ya existe un salon con codigo {codSalon}")
                time.sleep(2)
                break
            desc = input("Ingrese la descripción del salón: ")
            dicSalon = {"cod_salon": codSalon,"desc": desc}
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
        for x in colec.find({},{"cod_salon": 1, "desc": 1}):
            print(x)
        codSalon= int(input("Ingresa el codigo del SALON que desea modificar: "))
        nuevoDesc = input("Ingrese una nueva descripción: ")
        colec.update({"cod_salon": codSalon}, {"$set":{"desc":nuevoDesc}})
        os.system("cls")
        for x in colec.find({},{"cod_salon": 1, "desc": 1}):
            print(x)
        print("Se modifico correctamente")
        time.sleep(2)
        break
def eliminarSalon():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["salones"]
        for x in colec.find({},{"cod_salon": 1, "desc": 1}):
            print(x)
        codSalon= int(input("Ingresa el codigo del SALON que desea eliminar: "))
        salonDel = {"cod_salon": codSalon}
        resConn = colec.delete_one(salonDel)
        os.system("cls")
        for x in colec.find({},{"cod_salon": 1, "desc": 1}):
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

#FUNCIONES MANTENIMIENTOS CURSOS
def crearCurso():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["cursos"]
        for x in colec.find({},{"cod_curso": 1, "nombre": 1}):
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
        # colec = my_db["grados"]
        # for x in colec.find({},{"cod_grado": 1, "desc": 1}):
        #     print(x)
        # while True:
            # try:
            #     colec = my_db["grados"]
            #     codGrado = int(input("Ingrese el codigo del grado donde se dictara el curso: "))
            #     codexiste = bool(colec.find_one({"cod_grado":codGrado}))
            #     colec = my_db["cursos"]
            #     if codexiste :
            #         while True:
            #             try:
            #                 numNotas = int(input("Ingrese la cantidad de notas que tendra el curso: "))
            #                 break
            #             except:
            #                 print("Ingrese un numero entero")
            #                 time.sleep(2)
        dicCurso = {"cod_curso": codCurso,"nombre": nombreCurso}
        try:
            resConn = colec.insert_one(dicCurso)
                        # for x in range(numNotas):
                        #     colec.update({'cod_curso': codCurso},{'$set': {f"Nota {x+1} ": 0 }})  
                        # os.system("cls")
            for x in colec.find({},{"cod_curso": 1, "nombre": 1}):
                print(x)
                print("Se agregó correctamente")
                time.sleep(2)
                break
        except:
            print(f"Ya existe un curso con codigo {codCurso}")
            time.sleep(2)
        break           
def modificarCursos():
   while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["cursos"]
        for x in colec.find({},{"cod_curso": 1, "nombre": 1}):
            print(x)
        codCurso = int(input("Ingresa el codigo del CURSO que desea modificar: "))
        nuevoNombre = str(input("Ingresa el NUEVO nombre del CURSO: "))
        # nuevoCodgrado = str(input("Ingresa el NUEVO codigó grado del CURSO: "))
        # nuevoNumnotas = int(input("Ingrese el nuevo numero de notas: "))
        colec.update_one({"cod_curso":codCurso},{ "$set": {"nombre": nuevoNombre}})
        os.system("cls")
        for x in colec.find({},{"cod_curso": 1, "nombre": 1}):
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
        for x in colec.find({},{"cod_curso": 1, "nombre": 1}):
            print(x)
        codCurso= int(input("Ingresa el codigo del CURSO que desea eliminar: "))
        colec.delete_one({"cod_curso": codCurso})
        os.system("cls")
        for x in colec.find({},{"cod_curso": 1, "nombre": 1}):
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
    os.system("cls")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = myclient["Hackaton_S7_G5"]
    colec = my_db["salones"]
    for x in colec.find({},{"cod_salon": 1, "desc": 1}):
        print(x)
    codSalon = int(input("Crea un código para el  salón: "))
    desc = input("Ingresa la descripción del salon: ")
    dicSalon = {"cod_salon": codSalon,"desc": desc}
    resConn = colec.insert_one(dicSalon)
    os.system("cls")
    for x in colec.find({},{"cod_salon": 1, "desc": 1}):
        print(x)
    print("Se agregó correctamente")
    time.sleep(2)       
def modificarSalon():
    while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["salones"]
        for x in colec.find({},{"cod_salon": 1, "desc": 1}):
            print(x)
        codSalon= int(input("Ingresa el codigo del SALON que desea modificar: "))
        desc = str(input("Ingresa la nueva descripción para el SALON: "))
        salonMod = {"cod_salon": codSalon}
        colec.find_and_modify(salonMod, {"$set":{"desc":desc}})
        os.system("cls")
        for x in colec.find({},{"cod_salon": 1, "desc": 1}):
            print(x)
        print("Se modifico correctamente")
        time.sleep(2)
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
        for x in colec.find({},{"cod_curso": 1, "nombre": 1}):
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
        dicCurso = {"cod_curso": codCurso,"nombre": nombreCurso}
        try:
            resConn = colec.insert_one(dicCurso)
            for x in colec.find({},{"cod_curso": 1, "nombre": 1}):
                print(x)
                print("Se agregó correctamente")
                time.sleep(2)
                break
        except:
            print(f"Ya existe un curso con codigo {codCurso}")
            time.sleep(2)
        break           
def modificarCursos():
   while True:
        os.system("cls")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = myclient["Hackaton_S7_G5"]
        colec = my_db["cursos"]
        for x in colec.find({},{"cod_curso": 1, "nombre": 1}):
            print(x)
        codCurso = int(input("Ingresa el codigo del CURSO que desea modificar: "))
        nuevoNombre = str(input("Ingresa el NUEVO nombre del CURSO: "))
        colec.update_one({"cod_curso":codCurso},{ "$set": {"nombre": nuevoNombre}})
        os.system("cls")
        for x in colec.find({},{"cod_curso": 1, "nombre": 1}):
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
        for x in colec.find({},{"cod_curso": 1, "nombre": 1}):
            print(x)
        codCurso= int(input("Ingresa el codigo del CURSO que desea eliminar: "))
        colec.delete_one({"cod_curso": codCurso})
        os.system("cls")
        for x in colec.find({},{"cod_curso": 1, "nombre": 1}):
            print(x)
        print("Se eliminó correctamente")
        time.sleep(3)
        break
# FUNCIONES MANTENIMEINTO PROFESOR
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
    
# FUNCIONES MANTENIMIENTO ALUMNOS:
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

#CREAR MATRICULA
def crearMatricula():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = myclient["Hackaton_S7_G5"]
    colec = my_db["matriculas"]
    print("cod_matricula\talumno\t\tnombre\t\tgrado\t\tperiodo")
    for x in colec.find():
        alumno=x["alumno"]
        grado = x["grado"]
        periodo = x["periodo"]
        print(str(x["cod_matricula"]) + "\t\t" + alumno["nombre"] + "\t\t" + alumno["apellido"] + "\t" + grado["desc"] + "\t" + periodo["desc"])   
    while True: 
        try:
            codigoMatricula = int(input("Ingrese el codigo de la matricula: "))
            if 0 < codigoMatricula :
                break
            else:
                print("Error!: Ingrese un número entero positivo")
                pass
        except:
            print("Error!: Ingrese un número entero positivo")
    os.system("cls")
    colec = my_db["alumnos"]
    print("cod_alumno\tnombre\t\tapellido")
    for x in colec.find({},{"cod_alumno": 1, "nombre": 1, "apellido": 1}):
        print (str(x["cod_alumno"]) + "\t\t" + x["nombre"] + "\t\t" + x["apellido"])       
    codigoAlumno = int(input("Ingrese el codigo del alumno: "))
    dicAlumno = colec.find_one({"cod_alumno":codigoAlumno})
    os.system("cls")
    colec = my_db["grados"]
    print("cod_grado\tdesc")
    for x in colec.find({},{"cod_grado": 1, "desc": 1}):
        print (str(x["cod_grado"]) + "\t\t" + x["desc"])       
    codigoGrado = int(input("Ingrese el codigo del grado: "))   
    dicGrado = colec.find_one({"cod_grado":codigoGrado})
    os.system("cls")
    colec = my_db["periodos"]
    print("cod_periodo\tdesc")
    for x in colec.find({},{"cod_periodo": 1, "desc": 1}):
        print (str(x["cod_periodo"]) + "\t\t" + x["desc"])       
    codigoPeriodo = int(input("Ingrese el codigo del periodo: "))   
    dicPeriodo = colec.find_one({"cod_periodo":codigoPeriodo})
    os.system("cls")
    colec = my_db["cursos"]
    print("cod_curso\tnombre")
    for x in colec.find({},{"cod_curso": 1, "nombre": 1}):
        print (str(x["cod_curso"]) + "\t\t" + x["nombre"])       
    codigoCurso = int(input("Ingrese el codigo del curso: "))   
    dicCurso = colec.find_one({"cod_curso":codigoCurso})
    os.system("cls")
    colec = my_db["profesores"]
    print("cod_profesor\tnombre\t\tapellido")
    for x in colec.find({},{"cod_profesor": 1, "nombre": 1, "apellido":1}):
        print (str(x["cod_profesor"]) + "\t\t" + x["nombre"] + "\t\t"+ x["apellido"])       
    codigoProfesor = int(input("Ingrese el codigo del profesor: "))
    dicProfesor = colec.find_one({"cod_profesor":codigoProfesor})
    os.system("cls")
    colec = my_db["salones"]
    print("cod_salon\tdesc")
    for x in colec.find({},{"cod_salon": 1, "desc": 1}):
        print (str(x["cod_salon"]) + "\t\t" + x["desc"])     
    codigoSalon= int(input("Ingrese el codigo del Salon: "))
    dicSalon = colec.find_one({"cod_salon":codigoSalon})
    os.system("cls")
    colec = my_db["matriculas"]
    colec.insert_one({"cod_matricula": codigoMatricula,"alumno": dicAlumno, "grado": dicGrado, "periodo":dicPeriodo, "cursos":[] })
    colec.update_one({'cod_matricula': codigoMatricula},{'$push': {'cursos':[dicCurso,dicProfesor,dicSalon]}})

    while True:
        more = input("Deseas agregar mas cursos? S/N: ")
        if more == "S":
            colec = my_db["cursos"]
            print("cod_curso\tnombre")
            for x in colec.find({},{"cod_curso": 1, "nombre": 1}):
                print (str(x["cod_curso"]) + "\t\t" + x["nombre"])       
            codigoCurso = int(input("Ingrese el codigo del curso: "))   
            dicCurso = colec.find_one({"cod_curso":codigoCurso})
            os.system("cls")
            colec = my_db["profesores"]
            print("cod_profesor\tnombre\t\tapellido")
            for x in colec.find({},{"cod_profesor": 1, "nombre": 1, "apellido":1}):
                print (str(x["cod_profesor"]) + "\t\t" + x["nombre"] + "\t\t"+ x["apellido"])       
            codigoProfesor = int(input("Ingrese el codigo del profesor: "))
            dicProfesor = colec.find_one({"cod_profesor":codigoProfesor})
            os.system("cls")
            colec = my_db["salones"]
            print("cod_salon\tdesc")
            for x in colec.find({},{"cod_salon": 1, "desc": 1}):
                print (str(x["cod_salon"]) + "\t\t" + x["desc"])     
            codigoSalon= int(input("Ingrese el codigo del Salon: "))
            dicSalon = colec.find_one({"cod_salon":codigoSalon})
            colec = my_db["matriculas"]
            colec.update_one({'cod_matricula': codigoMatricula},{'$push': {'cursos':[dicCurso,dicProfesor,dicSalon]}})
        elif more == "N":
            break
        else:
            print("Ingrese S o N")    
    print("cod_matricula\talumno\t\tnombre\t\tgrado\t\tperiodo")
    for x in colec.find():
        alumno=x["alumno"]
        grado = x["grado"]
        periodo = x["periodo"]
        print(str(x["cod_matricula"]) + "\t\t" + alumno["nombre"] + "\t\t" + alumno["apellido"] + "\t" + grado["desc"] + "\t" + periodo["desc"])   
    time.sleep(2) 
#CREAR NOTAS
def crearNota():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = myclient["Hackaton_S7_G5"]
    colec = my_db["matriculas"]
    listAlumnos = colec.find()
    print("cod_matricula\talumno\t\tnombre\t\tgrado\t\tperiodo")
    for x in colec.find():
        alumno=x["alumno"]
        grado = x["grado"]
        periodo = x["periodo"]
        print(str(x["cod_matricula"]) + "\t\t" + alumno["nombre"] + "\t\t" + alumno["apellido"] + "\t" + grado["desc"] + "\t" + periodo["desc"])   
    codmatricula = int(input("Ingrese el codigo de matricula del alumno a ingresar la nota: "))
    print("cod_curso\tnombre")
    dicalumno=colec.find_one({"cod_matricula":codmatricula})
    numcursos=len(dicalumno["cursos"])
    for i in range(numcursos):
        cod = dicalumno["cursos"][i][0]["cod_curso"]
        nombre = dicalumno["cursos"][i][0]["nombre"]
        print(f'{cod}\t\t{nombre}')
    codCurso = int(input("Ingrese el codigo de curso: "))
    nota = int(input("Ingrese la nota del cuso: "))
    colec = my_db["notas"]
    colec.insert_one({"cod_matricula":codmatricula, "cod_curso":codCurso, "nota": nota})
    time.sleep(2)

def modificarNota():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = myclient["Hackaton_S7_G5"]
    colec = my_db["matriculas"]
    listAlumnos = colec.find()
    print("cod_matricula\talumno\t\tnombre\t\tgrado\t\tperiodo")
    for x in colec.find():
        alumno=x["alumno"]
        grado = x["grado"]
        periodo = x["periodo"]
        print(str(x["cod_matricula"]) + "\t\t" + alumno["nombre"] + "\t\t" + alumno["apellido"] + "\t" + grado["desc"] + "\t" + periodo["desc"])   
    codmatricula = int(input("Ingrese el codigo de matricula del alumno a modificar la nota: "))
    print("cod_curso\tnombre")
    dicalumno=colec.find_one({"cod_matricula":codmatricula})
    numcursos=len(dicalumno["cursos"])
    for i in range(numcursos):
        cod = dicalumno["cursos"][i][0]["cod_curso"]
        nombre = dicalumno["cursos"][i][0]["nombre"]
        print(f'{cod}\t\t{nombre}')
    codCurso = int(input("Ingrese el codigo de curso: "))
    nota = int(input("ingrese la nueva nota del cuso: "))
    colec.update_one({"cod_matricula":codmatricula, "cod_curso":codCurso, "nota": nota})
    print("cod_matricula\tcod_curso\t\tnota")
    for x in colec.find({},{"cod_matricula":codmatricula, "cod_curso":codCurso, "nota": nota}):
        print (str(x["cod_matricula"]) + "\t\t" + x["cod_curso"] + "\t\t" + x["nota"])
    print("Se modifico correctamente")
    time.sleep(2)

def eliminarNota():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = myclient["Hackaton_S7_G5"]
    colec = my_db["matriculas"]
    listAlumnos = colec.find()
    print("cod_matricula\talumno\t\tnombre\t\tgrado\t\tperiodo")
    for x in colec.find():
        alumno=x["alumno"]
        grado = x["grado"]
        periodo = x["periodo"]
        print(str(x["cod_matricula"]) + "\t\t" + alumno["nombre"] + "\t\t" + alumno["apellido"] + "\t" + grado["desc"] + "\t" + periodo["desc"])   
    codmatricula = int(input("Ingrese el codigo de matricula del alumno a elimar la nota: "))
    print("cod_curso\tnombre")
    dicalumno=colec.find_one({"cod_matricula":codmatricula})
    numcursos=len(dicalumno["cursos"])
    for i in range(numcursos):
        cod = dicalumno["cursos"][i][0]["cod_curso"]
        nombre = dicalumno["cursos"][i][0]["nombre"]
        print(f'{cod}\t\t{nombre}')
    codCurso = int(input("Ingrese el codigo de curso: "))
    resConn = colec.delete_one({"nota": nota})
    os.system("cls")
    print("cod_matricula\tcod_curso\t\tnota")
    for x in colec.find({},{"cod_matricula":codmatricula, "cod_curso":codCurso, "nota": nota}):
        print (str(x["cod_matricula"]) + "\t\t" + x["cod_curso"] + "\t\t" + x["nota"])
    print("Se modifico correctamente")
    time.sleep(2)
