import utils
log = utils.log("INIT")
# mongoDB
#import pymongo
import pymongo
from pymongo import MongoClient, errors


class conexionBDD:

    def conexion(self): 
        url = 'mongodb://localhost:27017'
        try:
            conn = pymongo.MongoClient(url) 
            #db = conn[str(f"{database}")]
            db = conn["Hackaton7Grupo6"]
            db["curso"]
            db["alumno"]
            db["nota"]
            db["salon"]
            return db
        except Exception as error:
            log.error(error)
            return error 
             
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

    def leerRegistroPorId(self, collection, data):
        conexion = self.conexion()
        doc = conexion[str(f"{collection}")]
        res = doc.find_one(data)
        return res

    def leerRegistros(self, collection, data):
        try:
            conexion = self.conexion()
            doc = conexion[str(f"{collection}")]
            res = doc.find(data)
            return res
        except Exception as error:
            log.error(error)  


    def actualizarRegistro(self, collection, condicion, cambio):
        try:
            conexion = self.conexion()
            doc = conexion[str(f"{collection}")] 
            doc.update_one(condicion,{ '$set' : cambio } )
            return doc
        except Exception as error:
            log.error(error) 


    def eliminarRegistro(self, collection, eliminar):
        try:
            conexion = self.conexion()
            doc = conexion[str(f"{collection}")] 
            doc.delete_one(eliminar)
            return doc
        except Exception as error:
            log.error(error) 


    def eliminarRegistros(self, collection, eliminar):
        try:
            conexion = self.conexion()
            doc = conexion[str(f"{collection}")] 
            doc.delete_many(eliminar)
            return doc
        except Exception as error:
            log.error(error) 




    def leerRegistrosTotal(self, collection):
        try:
            conexion = self.conexion()
            doc = conexion[str(f"{collection}")]
            res = doc.find()
            return res
        except Exception as error:
            log.error(error)  