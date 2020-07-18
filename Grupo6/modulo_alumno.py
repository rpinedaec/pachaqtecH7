import a_alumno.alumno
import menu
from menu import color
import utils

 



class Modulo_Alumno:
    lstAlumno = []  

    def __init__(self,conexion): 
        self.conexion=conexion

    def cargarAlumnos(self):
        self.lstAlumno.clear()
        coll = self.conexion.leerRegistrosTotal() 
        for obj in coll:
            DataRestor = a_alumno.alumno.alumno(obj['_id'],obj['nombreAlumno']
                                        ,obj['apellidoAlumno'],obj['dniAlumno']
                                        ,obj['direccionAlumno'])
            self.lstAlumno.append(DataRestor)


    def execute_modulo(self):
        self.cargarAlumnos()
        alumno_lst_num=['1','2','3','4','5','9']
        alumno_lst_opciones=['Listar','Buscar','Agregar','Actualizar','Eliminar','Salir']
        alumno_menu=menu.Menu('Alumno',alumno_lst_opciones,alumno_lst_num)
        retornar=True
        while retornar:
            resMenuInicio = alumno_menu.show_menu()
            if(resMenuInicio=='1'): #read
                utils.listaSimple(self.lstAlumno,"alumno",1) 
            elif(resMenuInicio=='2'): #Search
                nombrebuscar = input("Nombre: ")
                fitro = {"nombreAlumno": f"{nombrebuscar}" }
                lstAlumnoTemp = []
                lstAlumnoTemp.clear()
                collt = self.conexion.leerRegistros(fitro)
                for obj2 in collt:
                    DataRestor2 = a_alumno.alumno.alumno(obj2['_id'],obj2['nombreAlumno']
                                                ,obj2['apellidoAlumno'],obj2['dniAlumno']
                                                ,obj2['direccionAlumno'])
                    lstAlumnoTemp.append(DataRestor2)
                utils.listaSimple(lstAlumnoTemp,"alumno",1)
            elif(resMenuInicio=='3'): #create
                nombre = input("Nombre: ") 
                apellido = input("Apellido: ")
                dni = utils.validarNoExitaDniAlumnoEnLista(self.lstAlumno,"Cancelar: 9999 / DNI Nuevo: ")
                if dni!=9999:
                    Direccion = input("Direccion: ") 
                    data ={
                            "nombreAlumno":f"{nombre}"
                            ,"apellidoAlumno":f"{apellido}"
                            ,"dniAlumno":f"{dni}"
                            ,"direccionAlumno":f"{Direccion}"
                        }
                    insertado = self.conexion.insertarRegistro(data)
                    if insertado:
                        self.cargarAlumnos()
                        print("Insertado correctamente.") 
                    else:
                        print("Error al insertar.") 
                else:
                    print("Operacion Cancelada.")
                input("Enter para continuar")
            elif(resMenuInicio=='4'): #update
                utils.listaSimple(self.lstAlumno,"alumno",0)
                NActualizar = utils.validarDniAlumnoEnLista(self.lstAlumno,"Cancelar: 9999 / Dni a Actualizar: ")
                if NActualizar!=9999:
                    dataActualizar = { "dniAlumno": f"{NActualizar}" }                
                    nombre = input("Nuevo Nombre: ") 
                    apellido = input("Nuevo Apellido: ") 
                    #dni = utils.validarEntero("Nuevo DNI: ") 
                    dni = NActualizar 
                    Direccion = input("Nueva Direccion: ") 
                    dataActualizada ={
                            "nombreAlumno":f"{nombre}"
                            ,"apellidoAlumno":f"{apellido}"
                            ,"dniAlumno":f"{dni}"
                            ,"direccionAlumno":f"{Direccion}"
                        } 
                    coleli = self.conexion.actualizarRegistro(dataActualizar,dataActualizada)
                    if coleli:
                        self.cargarAlumnos()
                        print("Actualizado correctamente.") 
                    else:
                        print("Error al actualizar.")
                else:
                    print("Operacion cancelada.")
                input("Enter para continuar")
            elif(resMenuInicio=='5'): #delete
                utils.listaSimple(self.lstAlumno,"alumno",0) 
                NEliminar = utils.validarDniAlumnoEnLista(self.lstAlumno,"Cancelar: 9999 / Dni a Eliminar: ")
                if NEliminar!=9999:
                    dataEliminar = { "dniAlumno": f"{NEliminar}" }
                    coleli = self.conexion.eliminarRegistro(dataEliminar)
                    if coleli:
                        self.cargarAlumnos()
                        print("Eliminado correctamente.") 
                    else:
                        print("Error al eliminar.") 
                else:
                    print("Operacion cancelada.")
                input("Enter para continuar")
            elif(resMenuInicio=='9'):
                retornar = False

                
