from a_nota import nota
import a_alumno
from a_notacurso import cursonota
import menu
from menu import color
import utils
from bson.objectid import ObjectId
 


class Modulo_Nota:
    def __init__(self,conexion,conexionAlumno,conexionCurso): 
        self.conexion=conexion
        self.conexionAlumno=conexionAlumno
        self.conexionCurso=conexionCurso
        
    lstNota = []
    lstAlumno = []
    lstCurso = []

    def cargarAlumnos(self):
        self.lstAlumno.clear()
        coll = self.conexionAlumno.leerRegistrosTotal() 
        for obj in coll:
            DataRestor = a_alumno.alumno.alumno(obj['_id'],obj['nombreAlumno']
                                        ,obj['apellidoAlumno'],obj['dniAlumno']
                                        ,obj['direccionAlumno'])
            self.lstAlumno.append(DataRestor)


    def cargarNota(self):
        self.lstNota.clear()
        coll = self.conexion.leerRegistrosTotal()
        for obj in coll: 
            id = obj['_id']
            nott = obj['descripcionNota']
            idCur = obj['idCurso']
            idAlum = obj['idAlumno'] 
            DataRestor44 = nota.nota(id,nott,idCur,idAlum)
            self.lstNota.append(DataRestor44)


    def cargarCurso(self):
        self.lstCurso.clear()
        coll = self.conexionCurso.leerRegistrosTotal() 
        for obj in coll:
            id = str(obj['_id']) 
            nom = obj['curso']
            anio = str(obj['año academico'])
            DataRestor3 = cursonota.cursonota(id,nom,anio)
            self.lstCurso.append(DataRestor3)




    def execute_modulo(self):
        retornar=True
        while retornar:
            notas_lst_num=['1','2','3','4','9']
            notas_lst_opciones=['Listar','Buscar','Agregar','Eliminar','Salir']
            notas_menu=menu.Menu('notas',notas_lst_opciones,notas_lst_num)
            resMenuInicio = notas_menu.show_menu()
            if(resMenuInicio=='1'): #read
                lstNotasTemp1 = []
                lstNotasTemp1.clear()
                collt = self.conexion.leerRegistrosTotal()
                for obj2 in collt: 
                    idAlumnoT = obj2['idAlumno'] 
                    FiltroAlumnoId = {"_id": ObjectId(f"{idAlumnoT}")}
                    colltAlumno = self.conexionAlumno.leerRegistro(FiltroAlumnoId)
                    nombreAlumnoDes=colltAlumno['nombreAlumno']
                    
                    idCursoT = obj2['idCurso'] 
                    FiltroCursoId = {"_id": ObjectId(f"{idCursoT}")}
                    colltCurso = self.conexionCurso.leerRegistro(FiltroCursoId)
                    nombreCursoDes=colltCurso['curso']

                    DataRestor2 = nota.notaDescripcion(obj2['_id'],obj2['descripcionNota']
                                                ,nombreCursoDes,nombreAlumnoDes)
                    lstNotasTemp1.append(DataRestor2)
                utils.listaSimple(lstNotasTemp1,"nota",1)
            elif(resMenuInicio=='2'): #search
                self.cargarAlumnos()
                utils.listaSimple(self.lstAlumno,"alumno",0) 
                datoBuscar = utils.validarDniAlumnoEnLista(self.lstAlumno,"Ingrese un DNI: ")
                fitro = {"dniAlumno":f"{datoBuscar}"} 
                colltAlum = self.conexionAlumno.leerRegistro(fitro)
                idAlumno=colltAlum['_id']
                nombreAlumnoDes = colltAlum['nombreAlumno']
                fitroNotas = {"idAlumno":f"{idAlumno}"}            
                lstNotasTemp = []
                lstNotasTemp.clear()
                collt = self.conexion.leerRegistros(fitroNotas)
                for obj2 in collt: 
                    idCursoT = obj2['idCurso'] 
                    FiltroCursoId = {"_id": ObjectId(f"{idCursoT}")}
                    colltCurso = self.conexionCurso.leerRegistro(FiltroCursoId)
                    nombreCursoDes=colltCurso['curso']
                    DataRestor2 = nota.notaDescripcion(obj2['_id'],obj2['descripcionNota']
                                                ,nombreCursoDes,nombreAlumnoDes)
                    lstNotasTemp.append(DataRestor2)
                utils.listaSimple(lstNotasTemp,"nota",1)
            elif(resMenuInicio=='3'): #create
                self.cargarAlumnos()
                utils.listaSimple(self.lstAlumno,"alumno",0) 
                dbuscar = utils.validarDniAlumnoEnLista(self.lstAlumno,"DNI: ")
                fitro = {"dniAlumno":f"{dbuscar}"} 
                colltAlum = self.conexionAlumno.leerRegistro(fitro)
                idAlumno=colltAlum['_id']

                self.cargarCurso()
                utils.listaSimple(self.lstCurso,"curso",0) 
                numero = utils.validarEntero("Numero del Curso: ")
                cont = 0
                cursobuscar = ""
                for i in self.lstCurso:
                    cont +=1
                    if cont == numero:
                        cursobuscar = i.idcurso
                idCurso=cursobuscar
                Numnota = utils.validarEntero("Nota: ")
                data = { "descripcionNota":f"{Numnota}"
                        ,"idCurso":f"{idCurso}"
                        ,"idAlumno":f"{idAlumno}" }
                insertado = self.conexion.insertarRegistro(data)
                if insertado:
                    self.cargarNota()
                    print("Insertado correctamente.") 
                else:
                    print("Error al insertar.") 
                input("Enter para continuar..")
            elif(resMenuInicio=='4'): #delete 
                lstNotasTemp1 = []
                lstNotasTemp1.clear()
                collt = self.conexion.leerRegistrosTotal()
                for obj2 in collt: 
                    idAlumnoT = obj2['idAlumno'] 
                    FiltroAlumnoId = {"_id": ObjectId(f"{idAlumnoT}")}
                    colltAlumno = self.conexionAlumno.leerRegistro(FiltroAlumnoId)
                    nombreAlumnoDes=colltAlumno['nombreAlumno']
                    
                    idCursoT = obj2['idCurso'] 
                    FiltroCursoId = {"_id": ObjectId(f"{idCursoT}")}
                    colltCurso = self.conexionCurso.leerRegistro(FiltroCursoId)
                    nombreCursoDes=colltCurso['curso']

                    DataRestor2 = nota.notaDescripcion(obj2['_id'],obj2['descripcionNota']
                                                ,nombreCursoDes,nombreAlumnoDes)
                    lstNotasTemp1.append(DataRestor2)
                utils.listaSimple(lstNotasTemp1,"notaDescriptiva",0)
                numero = utils.validarEntero("Numero de Nota: ")
                cont = 0
                NotaIdd = ""
                for i in lstNotasTemp1:
                    cont +=1
                    if cont == numero:
                        NotaIdd = i.idNota
                data = { "_id":f"{NotaIdd}" } 
                eliminar = self.conexion.eliminarRegistro(data) 
                if eliminar:
                    self.cargarNota()
                    print("Eliminado correctamente.") 
                else:
                    print("Error al insertar.") 
                input("Enter para continuar..")

            elif(resMenuInicio=='9'):
                retornar = False

                