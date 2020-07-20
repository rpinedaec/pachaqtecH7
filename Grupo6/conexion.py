import pymongo
import utils

class Mongo_DB:
    def __init__(self,collection):
        self.collection=collection
    
    def conecc(self):
        myclient = pymongo.MongoClient('mongodb://localhost:27017')
        mydb = myclient['Hackaton7Grupo6']
        mycol = mydb[self.collection]
        return mycol
    
    def find(self,query):
        conexion=self.conecc()
        x=conexion.find_one(query)
        return x
     
    def find_all(self,query):
        conexion=self.conecc()
        list_all=[]
        for x in conexion.find({},query):
            list_all.append(x)
        return list_all

    def find_all_cond(self,query):
        conexion=self.conecc()
        list_all=[]
        for x in conexion.find(query):
            list_all.append(x)
        return list_all
     
    def insert(self,query):
        conexion=self.conecc()
        utils.logging.info(query)
        conexion.insert_one(query)

    def insert_many(self,query):
        conexion=self.conecc()
        utils.logging.info(query)
        conexion.insert_many(query)

    def update(self,query,my_dict):
        conexion=self.conecc()
        conexion.update_one(query,my_dict)
    
    def delete(self,query):
        conexion=self.conecc()
        conexion.delete_one(query)




    def leerRegistro(self, data):
        conexion=self.conecc()
        res = conexion.find_one(data)
        return res

    def leerRegistrosTotal(self): 
        conexion=self.conecc()
        res = conexion.find()
        return res 

    def leerRegistros(self, data):
        conexion=self.conecc()
        res = conexion.find(data)
        return res

    def insertarRegistro(self, data):
        conexion=self.conecc()
        res = conexion.insert_one(data).inserted_id
        return res

    def eliminarRegistro(self, eliminar):
        conexion=self.conecc()
        res = conexion.delete_one(eliminar)
        return res

    def actualizarRegistro(self, condicion, cambio): 
        conexion=self.conecc()
        res = conexion.update_one(condicion,{ '$set' : cambio } )
        return res

