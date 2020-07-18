import a_profesor
import menu
from menu import color

import menu
import utils

import utils


#Profesor
profesor_lst_num=['1','2','3','4','9']
profesor_lst_opciones=['Buscar','Agregar','Actulizar','Eliminar','Salir']
profesor_menu=menu.Menu('profesor',profesor_lst_opciones,profesor_lst_num)



class Modulo_prof:
    def __init__(self,conexion,ans): 
        self.conexion=conexion
        self.ans=ans
    
    def execute_modulo(self):
        if(self.ans=='1'): #read
            print("Ingrese el DNI del profesor:")
            DNI_profesor=input()
            query=a_profesor.funcion.find_profesor(DNI_profesor)
            record=self.conexion.find(query)
            print(record)
        elif(self.ans=='2'): #create
            print("Ingrese los datos del porfesor: ")
            DNI=input("DNI: ")
            Nombre_profesor=input("Nombre: ")
            Apellido_profesor=input("Apellido: ")
            query=a_profesor.funcion.insert_profesor(DNI,Nombre_profesor,Apellido_profesor)
            self.conexion.insert(query)
        elif(self.ans=='3'): #update
            print("Ingrese el DNI del prosor:")
            DNI_profesor=input("Respuesta: ")
            print("Ingrese el campo que desea modificar:")
            list_op_nom=['Cambiar nombre','Cambiar DNI','Cambiar Apellido']
            list_op_num=['1','2','3']
            menu_update_prof=menu.Menu('profesor',list_op_nom,list_op_num)
            Field=menu_update_prof.show_menu()
            utils.logging.info(Field)
            if (Field=='1'):
                field="DNI"
            elif (Field=='2'):
                field="nombre"
            elif (Field=='3'):
                field="apellido"
            print("Ingrese el nuevo valor:")
            New_value=input("Respuesta: ")
            query=a_profesor.funcion.update_profesor_DNI(DNI_profesor)
            my_dict=a_profesor.funcion.update_profesor(New_value,field)
            self.conexion.update(query,my_dict)
        elif(self.ans=='4'): #delete
            print("Ingrese el DNI del profesor")
            DNI_profesor=input("")
            query=a_profesor.funcion.delete_profesor(DNI_profesor)
            self.conexion.delete(query)
        elif(self.ans=='9'):
            exit()

    # def execute_modulo(self): 
    #     retornar=True
    #     while retornar: 
    #         resMenuInicio = profesor_menu.show_menu()
    #         if(resMenuInicio=='1'): #read
    #             #print("Ingrese el DNI del profesor:")
    #             #DNI=input("DNI: ")
    #             DNI_profesor=utils.validarEntero("Ingrese DNI del profesor:")
    #             query=a_profesor.funcion.find_profesor(DNI_profesor)
    #             record=self.conexion.find(query)
    #             print(record)
    #         elif(resMenuInicio=='2'): #create
    #             #print("Ingrese los datos del porfesor: ")
    #             #DNI=input("DNI: ")
    #             DNI=utils.validarEntero("Ingrese DNI del profesor:")
    #             Nombre_profesor=input("Nombre: ")
    #             Apellido_profesor=input("Apellido: ")
    #             query=a_profesor.funcion.insert_profesor(DNI,Nombre_profesor,Apellido_profesor)
    #             self.conexion.insert(query)
    #         elif(resMenuInicio=='3'): #update
    #             #print("Ingrese el DNI del prosor:")
    #             #DNI_profesor=input("Respuesta: ")
    #             DNI_profesor=utils.validarEntero("Ingrese DNI del profesor:")
    #             print("Ingrese el campo que desea modificar:")
    #             print("DNI➜ [1]           Nombre➜ [2]          Apellido➜ [3]")
    #             Field=input("Respuesta: ")
    #             if (Field=='1'):
    #                 field="DNI"
    #             elif (Field=='2'):
    #                 field="nombre"
    #             elif (Field=='3'):
    #                 field="apellido"
    #             print("Ingrese el nuevo valor:")
    #             New_value=input("Respuesta: ")
    #             query=a_profesor.funcion.update_profesor_DNI(DNI_profesor)
    #             my_dict=a_profesor.funcion.update_profesor(New_value,field)
    #             self.conexion.update(query,my_dict)
    #         elif(resMenuInicio=='4'): #delete
    #             #print("Ingrese el DNI del profesor")
    #             #DNI_profesor=input("")
    #             DNI_profesor=utils.validarEntero("Ingrese DNI del profesor:")
    #             query=a_profesor.funcion.delete_profesor(DNI_profesor)
    #             self.conexion.delete(query)
    #         elif(resMenuInicio=='9'):
    #             retornar = False
    #             #exit()


                
