from conn import Conexion
from classes import *
import time
import pymongo
from pymongo import MongoClient, errors

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = myclient["Hackaton_S7_G5"]
colec = my_db["alumnos"]
for x in colec.find({},{"cod_alumno": 1, "nombre": 1, "apellido": 1}):
    print(x)
codAlumno = int(input("Ingrese el codigo del Alumno: "))
dicAlumno =colec.find_one({"cod_alumno":codAlumno})    
campos =list(dicAlumno.keys())
gradoAlumno = str(campos[4])
colec = my_db["cursos"]
