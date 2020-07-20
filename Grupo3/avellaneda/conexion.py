#CRUD en una clase generica
#Mysql
import mysql.connector
from mysql.connector import errorcode
#Posgres
import psycopg2
from psycopg2 import Error
#sqlite
import sqlite3
#mongoDB
from pymongo import MongoClient, errors
#Log
import utils


class conexionBDD:

    __log = utils.log("Conexion")
    def __init__(self, intBDD):
        self.intBDD = intBDD
#si es 1 conectarnos a Mysql, si es 2 conectarnos a postgres y si 3 conectarnos sqlite

    def conexion(self):
        if(self.intBDD == 1):
            try:
                conn = mysql.connector.connect(user='root',
                                               password='RICARDO1984PAPO2011',
                                               host="localhost",
                                               port="3306",
                                               database="PerezdeCuellar-H7")
                return conn
            except(mysql.connector.Error, Exception) as error:
                return False
              
        elif(self.intBDD == 4):
            uri = 'mongodb://localhost:27017'
            database = 'Colegio'
            try:
                conn = MongoClient(uri)
                db = conn[str(f"{database}")]
                return db
            except Exception as error:
                return False

                # db[<database-name>][<Alumno>].insert(<document>);

    def consultarBDD(self, query):
        try:
            conexion = self.conexion()
            cur = conexion.cursor()
            cur.execute(query)
            records = cur.fetchall()
            return records
        except Error as error:
            return False

    def ejecutarBDD(self, query):
        try:
            conexion = self.conexion()
            cur = conexion.cursor()
            cur.execute(query)
            conexion.commit()
            exito = True
            return exito
        except Exception as identifier:
            return False
    

#INTENTO DE BUSQUEDA DE ALUMNOS

    # def listarAlumnos(self, query):
    #     try:
    #         conexion = self.conexion()
    #         cur = conexion.cursor()
    #         cur.execute(query)
    #         resultado = cur.fetchall()
    #         resultadofinal = [list(i) for i in resultado]
    #         # final_result = [i[0] for i in cursor.fetchall()]
    #     except Error as error:
    #         return False



    def insertarRegistro(self, collection, data):
        conexion = self.conexion()
        doc = conexion[str(f"{collection}")]
        res = doc.insert_one(data).inserted_id
        return res

    def insertarRegistros(self, collection, data):
        conexion = self.conexion()
        doc = conexion[str(f"{collection}")]
        res = doc.insert_many(data).inserted_ids
        return res

    def leerRegistro(self, collection, data):
        conexion = self.conexion()
        doc = conexion[str(f"{collection}")]
        res = doc.find_one(data)
        return res

    def leerRegistros(self, collection, data):
        conexion = self.conexion()
        doc = conexion[str(f"{collection}")]
        res = doc.find(data)
        return res

    def actualizarRegistro(self, collection, condicion, cambio):
        try:
            conexion = self.conexion()
            doc = conexion[str(f"{collection}")]
            doc.update_one(condicion, {'$set': cambio})
            return True
        except Exception as error:
            self.__log.debug(error)
            return False
    
    def eliminarRegistro(self, collection, eliminar):
        try:
            conexion = self.conexion()
            doc = conexion[str(f"{collection}")]
            doc.delete_one(eliminar)
            return True
        except Exception as error:
            self.__log.debug(error)
            return False
    
    def eliminarRegistros(self, collection,  eliminar):
        try:
            conexion = self.conexion()
            doc = conexion[str(f"{collection}")]
            doc.delete_many(eliminar)
            return True
        except Exception as error:
            self.__log.debug(error)
            return False