import pymongo
from pymongo import MongoClient
import utils


myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient["colegio"]
mycol = mydb["profesor"]

# create_setup
# profesor_1 = {
#     'DNI':'213233212',
#     'nombre': 'Roberto',
#     'apellido': 'Pineda',    
# }
# result = mycol.insert_one(profesor_1)

# profesor_2 = {
#     'DNI':'2973273',
#     'nombre': 'Braulio',
#     'apellido': 'Berlanga',    
# }
# result = mycol.insert_one(profesor_2)

# profesor_3 = {
#     'DNI': '6565906956',    
#     'nombre': 'Hipolito',
#     'apellido': 'Vasquez',    
# }
# result = mycol.insert_one(profesor_3)

# profesor_4 = {
#     'DNI':'355454354',   
#     'nombre':'Martin',
#     'apellido':'Pérez',    
# }
# result = mycol.insert_one(profesor_4)

#  create one
def insert_profesor(DNI,nombre,apellido):
    mydict={"DNI":DNI,"nombre":nombre,"apellido":apellido}
    return mydict
    

# find
def find_profesor(DNI):
    query={'DNI':DNI}
    return query


# read all
# for x in mycol.find():
#     print(x)

# delete

# myquery={"nombre":"Manuel"}
# mycol.delete_one(myquery)

# update
def update_profesor_DNI(DNI):
    query_DNI={"DNI":DNI}
    utils.logging.info(query_DNI)
    return query_DNI

def update_profesor(new_value,new_field):
    profesor_dict={'$set':{'field':'value'}}
    profesor_dict['$set']['field']=new_value
    profesor_dict['$set'][new_field]=profesor_dict['$set'].pop('field')
    utils.logging.info(profesor_dict)
    return profesor_dict


# myquery = { "DNI": "213233212" }
# newvalues = { "$set": { "nombre": "Esteban" } }
# query=(myquery,newvalues)

# mycol.update_many(myquery,newvalues)
