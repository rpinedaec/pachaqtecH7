import a_curso
import utils

class Modulo_curso:
    def __init__(self,ans,conexion):
        self.ans=ans
        self.conexion=conexion
    
    def execute_modulo(self):
        if(self.ans=='1'): #read list
            query={'_id':0,'curso':1,'año academico':1}    
            record=self.conexion.find_all(query)
            print(record)
        elif(self.ans=='2'): 
            print("Ingrese el datos solicitados:")
            curso=input("nombre del curso: ")
            query={"curso":curso}
            record=self.conexion.find_all_cond(query)
            print(record)   
        elif(self.ans=='3'): #create
            print("Ingrese los datos solicitados: ")
            Curso=input("Curso: ")
            Año=input("Año: ")
            query=a_curso.funcion.insert_curso(Curso,Año)
            utils.logging.info(query)
            self.conexion.insert(query)
        # elif(self.ans=='4'): #update
            # print("Ingrese el Año:")
            # Año=input("Respuesta: ")
            # print("Ingrese el campo que desea modificar:")
            # print("DNI➜ [1]           Nombre➜ [2]          Apellido➜ [3]")
            # Field=input("Respuesta: ")
            # if (Field=='1'):
            #     field="DNI"
            # elif (Field=='2'):
            #     field="nombre"
            # elif (Field=='3'):
            #     field="apellido"
            # print("Ingrese el nuevo valor:")
            # New_value=input("Respuesta: ")
            # query=a_curso.funcion.update_profesor_DNI(DNI_profesor)
            # my_dict=a_curso.funcion.update_profesor(New_value,field)
            # self.conexion.update(query,my_dict)
        elif(self.ans=='5'): #delete
            print("Ingrese los datos que desea eliminar")
            Curso=input("Curso:")
            Año=input("Año: ")
            query=a_curso.funcion.delete_curso(Curso,Año)
            self.conexion.delete(query)
        elif(self.ans=='9'):
            exit()
