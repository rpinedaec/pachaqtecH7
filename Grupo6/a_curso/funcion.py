
# set_up
def set_up_curso():
    curso_list=[
        {'curso':'Matematicas','año academico': '1ro'},
        {'curso':'Matematicas','año academico': '2do'},
        {'curso':'Matematicas','año academico': '3ro'},
        {'curso':'Matematicas','año academico': '4to'},
        {'curso':'Matematicas','año academico': '5to'},
        {'curso':'Historia','año academico': '1ro'},
        {'curso':'Historia','año academico': '2do'},
        {'curso':'Historia','año academico': '3ro'},       
        {'curso':'Historia','año academico': '4to'},
        {'curso':'Historia','año academico': '5to'},
        {'curso':'Lengua','año academico': '1ro'},
        {'curso':'Lengua','año academico': '2do'},        
        {'curso':'Lengua','año academico': '3ro'},
        {'curso':'Lengua','año academico': '4to'},
        {'curso':'Lengua','año academico': '5to'},
        {'curso':'Ciencias','año academico': '1ro'},
        {'curso':'Ciencias','año academico': '2do'},
        {'curso':'Ciencias','año academico': '3ro'},
        {'curso':'Ciencias','año academico': '4to'},
        {'curso':'Ciencias','año academico': '5to'}    
    ]
    return curso_list

#  create one
def insert_curso(curso,ano_acd):
    mydict={"curso":curso,"ano_acd":ano_acd}
    return mydict
    
# find
def find_curso(curso):
    query={'curso':curso}
    return query

# delete
def delete_curso(curso,ano_academico):
    query={"curso":curso,"año academico":ano_academico}
    return query

# update
# update
def update_input(nombre,ano_academico):
    query={'curso':nombre,'año academico':ano_academico}
    return query

def update_curso(new_value,field):    
    my_dict={'$set':{field:new_value}}
    return my_dict

