
# set_up
def set_up_alumno():
    alumno_list=[
        {'nombreAlumno':'martin','apellidoAlumno': 'perez'
        ,'dniAlumno':'12121212','direccionAlumno': 'lima norte'},
        {'nombreAlumno':'braulio','apellidoAlumno': 'pachaqtec'
        ,'dniAlumno':'34343434','direccionAlumno': 'lima sur'},
        {'nombreAlumno':'hipolito','apellidoAlumno': 'pachaqtec'
        ,'dniAlumno':'56565656','direccionAlumno': 'lima centro'},
        {'nombreAlumno':'sergio','apellidoAlumno': 'perez'
        ,'dniAlumno':'78787878','direccionAlumno': 'lima sur'}    
    ]
    return alumno_list

#  create one
def insert_alumno(nombreAlumno,apellidoAlumno,dniAlumno,direccionAlumno):
    mydict={"nombreAlumno":nombreAlumno,"apellidoAlumno":apellidoAlumno
            ,"dniAlumno":dniAlumno,"direccionAlumno":direccionAlumno}
    return mydict
    
# find
def find_alumno(nombreAlumno,apellidoAlumno,dniAlumno,direccionAlumno):
    query={"nombreAlumno":nombreAlumno,"apellidoAlumno":apellidoAlumno
            ,"dniAlumno":dniAlumno,"direccionAlumno":direccionAlumno}
    return query

# delete
def delete_alumno(nombre,apellido):
    query={"nombreAlumno":nombre,"apellidoAlumno":apellido}
    return query

# update
# update
def update_input(nombre,apellido,dni,direccion):
    query={"nombreAlumno":nombre,"apellidoAlumno":apellido
            ,"dniAlumno":dni,"direccionAlumno":direccion}
    return query

def update_alumno(new_value,field):    
    my_dict={'$set':{field:new_value}}
    return my_dict

