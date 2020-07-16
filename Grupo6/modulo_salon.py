import utils
import a_salon

class Modulo_salon:
    def __init__(self,ans,conexion):
        self.ans=ans
        self.conexion=conexion
    
    def execute_modulo(self):
        if(self.ans=='1'): #read list
            query={'_id':0,'numero':1,'seccion':1}    
            record=self.conexion.find_all(query)
            print(record)
        elif(self.ans=='2'): 
            print("Ingrese el datos solicitados:")
            numero=input("numero: ")
            query={"numero":numero}
            record=self.conexion.find_all_cond(query)
            print(record)             
        elif(self.ans=='3'): #create
            print("Ingrese los datos solicitados del registro que desea cambiar: ")
            Numero=input("numero: ")
            Seccion=input("Seccion: ")
            query=a_salon.funcion.insert_salon(Numero,Seccion)
            utils.logging.info(query)
            self.conexion.insert(query)
        elif(self.ans=='4'): #update
            print("Ingrese la informacion solicitada:")
            Numero=input("Numero: ")
            Seccion=input("Seccion: ")
            print("Ingrese el campo que desea modificar:")
            print("Numero➜ [1]           Seccion➜ [2]")
            Field=input("Respuesta: ")
            if (Field=='1'):
                field="numero"
            elif (Field=='2'):
                field="seccion"
            print("Ingrese el nuevo valor:")
            New_value=input("Respuesta: ")
            query=a_salon.funcion.update_input(Numero,Seccion)
            my_dict=a_salon.funcion.update_salon(New_value,field)
            self.conexion.update(query,my_dict)
        elif(self.ans=='5'): #delete
            print("Ingrese los datos que desea eliminar")
            Numero=input("Numero:")
            Seccion=input("Seccion: ")
            query=a_salon.funcion.delete_salon(Numero,Seccion)
            self.conexion.delete(query)
        elif(self.ans=='9'):
            exit()
