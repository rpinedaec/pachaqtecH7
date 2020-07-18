
# set_up
def set_up_datos():
    #datos_list=[ {'descripcionNota':'martin','idCurso': '','idAlumno':'12121212'}  ]
    #return datos_list
    pass


#  create one
def insert_dato(nota,idAlumno,idCurso):
    mydict={"descripcionNota":nota,"idAlumno":idAlumno,"idCurso":idCurso}
    return mydict

# find
def find_dato(nombre):
    query={ 'nombreAlumno' : nombre }
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

