import pymongo
from pymongo import MongoClient, errors
from pprint import PrettyPrinter


class Connection:
    def __init__(self, uri, database):
        self.client = MongoClient(uri)
        self.db = self.client.pachaqtec
        print("Conexion Exitosa")

    # Metodo insertar un registro

    def insertRegistro(self, collection, data):
        collection = self.db[collection]
        result = collection.insert_one(data)
        print(f"Se ingreso el registro : {result.inserted_id} ")

    # Metodo obtener registros
    def obtenerRegistros(self, collection, condition=None):
        collection = self.db[collection]
        data = collection.find(condition)
        return list(data)

    # Metodo obtener un solo registro
    def obtenerRegistro(self, collection, condition=None):
        collection = self.db[collection]
        data = collection.find_one(condition)
        return data

    # Metodo cerrar conexion
    def cerrarConexion(self):
        self.db.close()
        return True

    # change seria lo que vamos a actualizar
    def actualizarRegistro(self, collection, condition, change):
        collection = self.db[collection]
        collection.update(condition, {
            '$set': change
        })
        print("Se actualizo un registro")

    def eliminarRegistro(self, collection, condition=None):
        collection = self.db[collection]
        collection.delete_one(condition)
        print(f"Delete Row")

    def returnCollection(self, collection):
        collection = self.db[collection]
        return collection
