import pymongo
from pymongo import MongoClient

class Mongo_DB:
    def __init__(self,mydb):
        self.mydb=mydb
    
    def conecc(self):
        myclient = pymongo.MongoClient('mongodb://localhost:27017')
        mydb = myclient[self.mydb]
        mycol = mydb["profesor"]
        return mycol
    
    def find(self,query):
        conexion=self.conecc()
        x=conexion.find_one()
        return x
    
    def insert(self,query):
        conexion=self.conecc()
        conexion.insert_one(query)

    def update(self,query,my_dict):
        conexion=self.conecc()
        conexion.update_one(query,my_dict)


