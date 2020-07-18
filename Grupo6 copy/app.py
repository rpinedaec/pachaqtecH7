import pymongo
import conexion
import a_profesor.funcion
import a_salon.funcion
# import a_nota.funcion
import a_perdesc.funcion
import a_curso.funcion
# import a_alumno.funcion

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
#Profesor
profesor_lst_num=['1','2','3','4','9']
profesor_lst_opciones=['Buscar','Agregar','Actulizar','Eliminar','Salir']
profesor_menu=menu.Menu('profesor',profesor_lst_opciones,profesor_lst_num)
#Alumno
alumno_lst_num=['1','2','3','4','9']
alumno_lst_opciones=['Buscar','Agregar','Actulizar','Eliminar','Salir']
alumno_menu=menu.Menu('alumno',alumno_lst_opciones,alumno_lst_num)
#Salon
salon_lst_num=['1','2','3','4','5','9']
salon_lst_opciones=['Listar','Buscar por pabellon','Agregar','Actulizar','Eliminar','Salir']
salon_menu=menu.Menu('salon',salon_lst_opciones,salon_lst_num)
#Curso
curso_lst_num=['1','2','3','4','5','9']
curso_lst_opciones=['Listar','Buscar por nombre','Agregar','Actulizar','Eliminar','Salir']
curso_menu=menu.Menu('curso',curso_lst_opciones,curso_lst_num)
#Notas
notas_lst_num=['1','2','3','4','9']
notas_lst_opciones=['Listar','Buscar','Agregar','Actulizar','Eliminar','Salir']
notas_menu=menu.Menu('notas',notas_lst_opciones,notas_lst_num)
#Periodo escolar
perdesc_lst_num=['1','2','3','4','5','9']
perdesc_lst_opciones=['Listar','Buscar por año','Agregar','Actulizar','Eliminar','Salir']
perdesc_menu=menu.Menu('periodo escolar',perdesc_lst_opciones,perdesc_lst_num)

#set_up
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = myclient.list_database_names()
if not "Hackaton7Grupo6" in dblist:
  prof_conn=conexion.Mongo_DB("profesor")
  alum_conn=conexion.Mongo_DB("alumno")
  cur_conn=conexion.Mongo_DB("curso")
  not_conn=conexion.Mongo_DB("notas")
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

#conexions
prof_conn=conexion.Mongo_DB("profesor")
alum_conn=conexion.Mongo_DB("alumno")
cur_conn=conexion.Mongo_DB("curso")
not_conn=conexion.Mongo_DB("notas")
salon_conn=conexion.Mongo_DB("salon")
perdesc_conn=conexion.Mongo_DB("periodo escolar")

#program start
r=True
while r:
    ans=Menu_menu.show_menu()
    if(ans=='2'):
        ans=profesor_menu.show_menu()
        mod_prof=modulo_profesor.Modulo_prof(ans,prof_conn)
        mod_prof.execute_modulo()
    elif(ans=='1'):
        ans=alumno_menu.show_menu()
    elif(ans=='3'):
        ans=notas_menu.show_menu()
    elif(ans=='4'):
        ans=curso_menu.show_menu()
        mod_curso=modulo_curso.Modulo_curso(ans,cur_conn)
        mod_curso.execute_modulo()
    elif(ans=='5'):
        ans=salon_menu.show_menu()
        mod_salon=modulo_salon.Modulo_salon(ans,salon_conn)
        mod_salon.execute_modulo()
    elif(ans=='6'):
        ans=perdesc_menu.show_menu()
        mod_perdesc=modulo_perdesc.Modulo_perdesc(ans,perdesc_conn)
        mod_perdesc.execute_modulo()
    print(" ")
    print("Desea volver al menu (m) o salir(9) del programa ")
    t=True
    while t:
        ans=input("Respuesta: ")
        if(ans=='9'):
            r=False
            break
        elif(ans=='m'):            
            break
        else:
            print(" ")
            print(color.WARNING+"Opcion invalida deben ser numeros segun el menu"+color.END)
            print(" ")      







