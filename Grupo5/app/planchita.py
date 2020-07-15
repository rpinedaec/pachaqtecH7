from conn import Conexion
from classes import *
import time
import pymongo
from pymongo import MongoClient, errors
def crearnota():
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
    nota = int(input("ingrese la nota del cusor: "))
    colec = my_db["notas"]
    colec.insert_one({"cod_matricula":codmatricula, "cod_curso":codCurso, "nota": nota})
