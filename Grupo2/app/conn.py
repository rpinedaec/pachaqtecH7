import mysql.connector
import psycopg2
from pymongo import MongoClient, errors

class Conexion:
    def __init__(self, intBDD):
        self.intBDD = intBDD

    def conexion(self):
        if(self.intBDD == 1):
            try:
                conn = mysql.connector.connect(user='root',
                                    password='SH4wnM3nd3s',
                                    host='localhost',
                                    database='Hackatons6fmilla')
                return conn
            except:
                return False
            
        elif(self.intBDD == 2):
            try:
                conn = psycopg2.connect(user='postgres',
                            password='SH4wnM3nd3s',
                            host="localhost",
                            port="5432",
                            database="fmilla")
                return conn
            except:
                return False

        elif(self.intBDD == 4):
            uri = 'mongodb://localhost:27017'
            database = 'wui'
            try:
                conn = MongoClient(uri)
                db = conn[str(f"{database}")]
                return db
            except Exception as error:
                return False
        
    def obtener_registro(self, collection, data):
        conexion = self.conexion()
        doc = conexion[str(f"{collection}")]
        res = doc.find_one(data)
        return res

    def obtener_registros(self, collection, data):
        conexion = self.conexion()
        doc = conexion[str(f"{collection}")]
        res = doc.find(data)
        return res

    def insertar_registro(self,collection,data):
        conexion = self.conexion()
        doc = conexion[str(f"{collection}")]
        res = doc.insert_one(data).inserted_id
        return res

    def insertar_registros(self,collection,data):
        conexion = self.conexion()
        doc = conexion[str(f"{collection}")]
        res = doc.insert_many(data).inserted_ids
        return res

    def actualizar_registro(self,collection,condition,change):
        try:
            conexion = self.conexion()
            doc = conexion[str(f"{collection}")]
            doc.update_one(condition, {'$set': change})
            return True
        except Exception as error:
            return False

    def eliminar_registro(self,collection,condition):
        try:
            conexion = self.conexion()
            doc = conexion[str(f"{collection}")]
            doc.delete_one(condition)
            return True
        except Exception as error:
            return False
    
    def eliminar_registros(self,collection,condition):
        try:
            conexion = self.conexion()
            doc = conexion[str(f"{collection}")]
            doc.delete_many(condition)
            return True
        except Exception as error:
            return False

    def ver_registros(self,collection):
        data = {}
        conexion = self.conexion()
        doc = conexion[str(f"{collection}")]
        query = doc.find(data)
        for obj in query:
                print(obj)
