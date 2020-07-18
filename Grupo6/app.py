import pymongo
import conexion
import a_profesor.funcion
import a_salon.funcion
# import a_nota.funcion
import a_perdesc.funcion
import a_curso.funcion
import a_alumno.funcion

import modulo_profesor
import modulo_salon
import modulo_notas
import modulo_perdesc
import modulo_curso
import modulo_alumno

import menu
import utils
from menu import color

#Menus
#Main
Menu_lst_num=['1','2','3','4','5','6','9']
Menu_lst_opciones=['Alumnos','Profesores','Notas','Cursos','Salones','Periodo escolar','Salir']
Menu_menu=menu.Menu('Home',Menu_lst_opciones,Menu_lst_num)




#set_up
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = myclient.list_database_names()
if not "Hackaton7Grupo6" in dblist:
  prof_conn=conexion.Mongo_DB("profesor")
  alum_conn=conexion.Mongo_DB("alumno")
  cur_conn=conexion.Mongo_DB("curso")
  not_conn=conexion.Mongo_DB("nota")
  salon_conn=conexion.Mongo_DB("salon")
  perdesc_conn=conexion.Mongo_DB("periodo escolar")
  query=a_profesor.funcion.set_up_profesor()
  prof_conn.insert_many(query)
  query=a_perdesc.funcion.set_up_perdesc()
  perdesc_conn.insert_many(query)
  query=a_curso.funcion.set_up_curso()
  cur_conn.insert_many(query)
  query=a_salon.funcion.set_up_salon()
  salon_conn.insert_many(query)
  query=a_alumno.funcion.set_up_alumno()
  alum_conn.insert_many(query)



#conexions
prof_conn=conexion.Mongo_DB("profesor")
alum_conn=conexion.Mongo_DB("alumno")
cur_conn=conexion.Mongo_DB("curso")
not_conn=conexion.Mongo_DB("nota")
salon_conn=conexion.Mongo_DB("salon")
perdesc_conn=conexion.Mongo_DB("periodo escolar")



#program start
r=True
while r:
    ans=Menu_menu.show_menu()
    if(ans=='2'): # Profesor
        mod_prof=modulo_profesor.Modulo_prof(prof_conn)
        mod_prof.execute_modulo()
    elif(ans=='1'): # Alumno
        mod_alumno=modulo_alumno.Modulo_Alumno(alum_conn)
        mod_alumno.execute_modulo()
    elif(ans=='3'): # Notas
        mod_nota=modulo_notas.Modulo_Nota(not_conn, alum_conn, cur_conn)
        mod_nota.execute_modulo()
    elif(ans=='4'): # Cursos 
        mod_curso=modulo_curso.Modulo_curso(cur_conn)
        mod_curso.execute_modulo() 
    elif(ans=='5'): # Salon 
        mod_salon=modulo_salon.Modulo_salon(salon_conn)
        mod_salon.execute_modulo()
    elif(ans=='6'): # Periodo
        mod_perdesc=modulo_perdesc.Modulo_perdesc(perdesc_conn)
        mod_perdesc.execute_modulo()
    elif(ans=='9'):
        r = False






