from pymongo import MongoClient, errors
from pprint import PrettyPrinter


class Connection:
    def __init__(self, uri, database):
        self.client = MongoClient(uri)
        self.db = self.client.get_database('pachaqtec')
        print("Conexion Exitosa")

    # Metodo insertar un registro

    def insertRegistro(self, collection, data):
        collection = self.db[collection]
        result = collection.insert_one(data)
        print(f"Se ingreso el registro : {result.inserted_id} ")

    # Metodo obtener registros
    def obtenerRegistros(self, collection, condition={}):
        collection = self.db[collection]
        data = collection.find()
        return list(data)

    # Metodo obtener un solo registro
    def obtenerRegistro(self, collection, condition={}):
        collection = self.db[collection]
        data = collection.find_one(condition)
        return data

    # Metodo cerrar conexion
    def cerrarConexion(self):
        self.db.close()
        return True
