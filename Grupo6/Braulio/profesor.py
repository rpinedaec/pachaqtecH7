import utils

# set_up
def set_up_profesor():
    profesor_list=[
        {'DNI':'213233212','nombre': 'Roberto','apellido': 'Pineda'}, 
        {'DNI':'2973273','nombre': 'Braulio','apellido': 'Berlanga'},
        {'DNI': '6565906956','nombre': 'Hipolito','apellido': 'Vasquez'},
        {'DNI':'355454354','nombre':'Martin','apellido':'Pérez'},
        {'DNI':'8658587','nombre':'Mirta','apellido':'Arevalo'},
        {'DNI':'38767686','nombre':'Sergio','apellido':'Pérez'},
        {'DNI':'694345678','nombre':'Agusto','apellido':'Diaz'}
    ]
    return profesor_list

#  create one
def insert_profesor(DNI,nombre,apellido):
    mydict={"DNI":DNI,"nombre":nombre,"apellido":apellido}
    return mydict
    
# find
def find_profesor(DNI):
    query={'DNI':DNI}
    utils.logging.info("La query find: "+str(query))
    return query

# delete
def delete_profesor(DNI):
    query={"DNI":DNI}
    return query

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

