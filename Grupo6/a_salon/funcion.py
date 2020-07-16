# set_up
def set_up_salon():
    salon_list=[
        {'numero':'1','seccion': 'A'},
        {'numero':'1','seccion': 'B'}, 
        {'numero':'2','seccion': 'A'}, 
        {'numero':'2','seccion': 'B'}, 
        {'numero':'3','seccion': 'A'}, 
        {'numero':'3','seccion': 'B'}, 
        {'numero':'4','seccion': 'A'}, 
        {'numero':'4','seccion': 'B'}, 
        {'numero':'5','seccion': 'A'}, 
        {'numero':'5','seccion': 'B'}  
    ]
    return salon_list

#  create one
def insert_salon(numero,seccion):
    mydict={"numero":numero,"seccion":seccion}
    return mydict
    
# find
# def find_salon(numero):
#     query={'numero':numero}
#     return query

# delete
def delete_salon(numero,seccion):
    query={"numero":numero,"seccion":seccion}
    return query

# update
def update_input(numero,seccion):
    query={'numero':numero,'seccion':seccion}
    return query

def update_salon(new_value,field):    
    my_dict={'$set':{field:new_value}}
    return my_dict

