from pymongo import MongoClient, errors

class Conexion:

    #INICIO CONEXION
    def __init__(self, uri, database):
        self.client = MongoClient(uri)
        self.db = self.client[database]
        print("Conexion exitosa")

    #CREATE
    def insertar_registro(self, collection, data):
        collection = self.db[collection]
        result = collection.insert_one(data)
        print(f"Insert row: {result.inserted_id}")

    #READE
    def obtener_registros(self, collection, condition={}):
        collection = self.db[collection]
        data = collection.find(condition)
        return list(data)
    
    def obtener_registro(self, collection, condition={}):
        collection = self.db[collection]
        data = collection.find_one(condition)
        return data

    #UPDATE
    def actualizar_registro(self, collection, condition, change):
        collection = self.db[collection]
        collection.update_one(condition, {
            '$set': change
        })

    #DELETE
    def eliminar_registro(self, collection, condition={}):
        collection = self.db[collection]
        collection.delete(condition)
        print('Se elimino registro')

    #CERRAR CONEXION
    def cerrar_conexion(self):
        self.db.close()
        print("Se cerro la conexion con exito")
        return True