import conexion
import profesor

class Menu:
    def __init__(self,nombre,list_nom,list_num):
        self.nombre=nombre
        self.list_nom=list_nom
        self.list_num=list_num
    
    def show_menu(self):
        print("Menu: "+self.nombre)
        print("Ingrese la opcion que desea realizar")
        n=len(self.list_nom)
        for x in range(n):
            print(self.list_nom[x-1]+":"+self.list_num[x-1])
        ans=input("Respuesta")
        return ans

profesor_lst_opciones=['1','2','3','4','5']
profesor_lst_num=['Buscar','Agregar','Actulizar','Eliminar','Salir']
profesor_menu=Menu("Profesor",profesor_lst_opciones,profesor_lst_num)

print("Ingrese para su base de datos")
nombre_db=input("Respuesta:")
conn=conexion.Mongo_DB(nombre_db)
conn.conecc()
ans=profesor_menu.show_menu()

if(ans=='1'):
    print("Ingrese el DNI del profesor:")
    DNI_profesor=input()
    query=profesor.find_profesor(DNI_profesor)
    record=conn.find(query)
    print(record)
elif(ans=='2'):
    print("Ingrese los datos del porfesor: ")
    DNI=input("DNI: ")
    Nombre_profesor=input("Nombre: ")
    Apellido_profesor=input("Apellido: ")
    query=profesor.insert_profesor(DNI,Nombre_profesor,Apellido_profesor)
    conn.insert(query)
elif(ans=='3'):
    print("Ingrese el DNI del prosor:")
    DNI_profesor=input("Respuesta: ")
    print("Ingrese el campo que desea modificar:")
    print("DNI➜ [1]           Nombre➜ [2]          Apellido➜ [3]")
    Field=input("Respuesta: ")
    if (Field=='1'):
        field="DNI"
    elif (Field=='2'):
        field="nombre"
    elif (Field=='3'):
        field="apellido"
    print("Ingrese el nuevo valor:")
    New_value=input("Respuesta: ")
    query=profesor.update_profesor_DNI(DNI_profesor)
    my_dict=profesor.update_profesor(New_value,field)
    conn.update(query,my_dict)

elif(ans=='4'):
    pass
elif(ans=='5'):
    pass
