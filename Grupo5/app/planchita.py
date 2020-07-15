from conn import Conexion
from classes import *
import time
import pymongo
from pymongo import MongoClient, errors

os.system("cls")
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = myclient["Hackaton_S7_G5"]
colec = my_db["profesores"]
print("cod_profesor\tnombre\t\tapellido")
for x in colec.find({},{"cod_profesor": 1, "nombre": 1, "apellido": 1}):
    print (str(x["cod_profesor"]) + "\t\t" + x["nombre"] + "\t\t" + x["apellido"])
