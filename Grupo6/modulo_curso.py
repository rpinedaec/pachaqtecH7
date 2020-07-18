import a_curso
import utils
import menu


#Curso
curso_lst_num=['1','2','3','4','5','9']
curso_lst_opciones=['Listar','Buscar por nombre','Agregar','Actulizar','Eliminar','Salir']
curso_menu=menu.Menu('curso',curso_lst_opciones,curso_lst_num)


class Modulo_curso:
    def __init__(self,conexion):
        self.conexion=conexion
    
    def execute_modulo(self):
        retornar=True
        while retornar: 
            resMenuInicio = curso_menu.show_menu()
            if(resMenuInicio=='1'): #read list
                #query={'_id':0,'curso':1,'año academico':1}    
                query={}
                record=self.conexion.find_all(query)
                print(record)
                input("Enter para continuar...") 
            elif(resMenuInicio=='2'): 
                print("Ingrese el datos solicitados:")
                curso=input("nombre del curso: ")
                query={"curso":curso}
                record=self.conexion.find_all_cond(query)
                print(record)   
            elif(resMenuInicio=='3'): #create
                print("Ingrese los datos solicitados: ")
                Curso=input("Curso: ")
                Año=input("Año: ")
                query=a_curso.funcion.insert_curso(Curso,Año)
                utils.logging.info(query)
                self.conexion.insert(query)
            elif(resMenuInicio=='4'): #update
                print("Ingrese la informacion solicitada:")
                Nombre=input("Nombre: ")
                Año_academico=input("Año academico: ")
                print("Ingrese los datos solicitados del registro que desea cambiar:")
                print("Nombre➜ [1]           Año academico➜ [2]")
                Field=input("Respuesta: ")
                if (Field=='1'):
                    field="curso"
                elif (Field=='2'):
                    field="año academico"
                print("Ingrese el nuevo valor:")
                New_value=input("Respuesta: ")
                query=a_curso.funcion.update_input(Nombre,Año_academico)
                my_dict=a_curso.funcion.update_curso(New_value,field)
                self.conexion.update(query,my_dict)
            elif(resMenuInicio=='5'): #delete
                print("Ingrese los datos que desea eliminar")
                Curso=input("Curso:")
                Año=input("Año: ")
                query=a_curso.funcion.delete_curso(Curso,Año)
                self.conexion.delete(query)
            elif(resMenuInicio=='9'):
                retornar = False


