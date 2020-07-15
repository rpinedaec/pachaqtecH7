import a_perdesc
import utils
from pymongo import MongoClient

class Modulo_perdesc:
    def __init__(self,ans,conexion):
        self.ans=ans
        self.conexion=conexion
    
    def execute_modulo(self):
        if(self.ans=='1'): #read list
            query={'_id':0,'Año':1,'Bimestre':1}    
            record=self.conexion.find_all(query)
            print(record)
        elif(self.ans=='2'): #read
            print("Ingrese el datos solicitados:")
            Año=input("Año: ")
            query={"Año":Año}
            record=self.conexion.find_all_cond(query)
            print(record)
        elif(self.ans=='3'): #create
            print("Ingrese los datos solicitados: ")
            Año=input("Año: ")
            Bimestre=input("Bimestre: ")
            query=a_perdesc.funcion.insert_perdesc(Año,Bimestre)
            utils.logging.info(query)
            self.conexion.insert(query)
        # elif(self.ans=='4'): #update
        #     print("Ingrese el Año:")
        #     Año=input("Respuesta: ")
        #     print("Ingrese el campo que desea modificar:")
        #     print("DNI➜ [1]           Nombre➜ [2]          Apellido➜ [3]")
        #     Field=input("Respuesta: ")
        #     if (Field=='1'):
        #         field="DNI"
        #     elif (Field=='2'):
        #         field="nombre"
        #     elif (Field=='3'):
        #         field="apellido"
        #     print("Ingrese el nuevo valor:")
        #     New_value=input("Respuesta: ")
        #     query=a_perdesc.funcion.update_profesor_DNI(DNI_profesor)
        #     my_dict=a_perdesc.funcion.update_profesor(New_value,field)
        #     self.conexion.update(query,my_dict)
        elif(self.ans=='5'): #delete
            print("Ingrese los datos que desea eliminar")
            Año=input("Año:")
            Bimestre=input("Bimestre: ")
            query=a_perdesc.funcion.delete_perdesc(Año,Bimestre)
            self.conexion.delete(query)
        elif(self.ans=='9'):
            exit()
