import pymongo
from pymongo import MongoClient
import utils


class Mongo_DB:
    def __init__(self,mydb,collection):
        self.mydb=mydb
        self.collection=collection
    
    def conecc(self):
        myclient = pymongo.MongoClient('mongodb://localhost:27017')
        mydb = myclient[self.mydb]
        mycol = mydb[self.collection]
        return mycol
    
    def find(self,query):
        conexion=self.conecc()
        utils.logging.info(conexion)
        x=conexion.find_one(query)
        return x
    
    def insert(self,query):
        conexion=self.conecc()
        conexion.insert_one(query)

    def insert_many(self,query):
        conexion=self.conecc()
        conexion.insert_many(query)

    def update(self,query,my_dict):
        conexion=self.conecc()
        conexion.update_one(query,my_dict)
    
    def delete(self,query):
        conexion=self.conecc()
        conexion.delete_one(query)



