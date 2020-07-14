import conexion
import utils

import alumno
import curso
import nota
from bson.objectid import ObjectId


lstAlumno = []
lstNota = []
lstCurso = []
log = utils.log("INIT")
MsjContinuar = "Enter para continuar..."
conn = conexion.conexionBDD()



def cargarAlumnos():
    lstAlumno.clear()
    coll = conn.leerRegistrosTotal("alumno")
    for obj in coll:
        DataRestor = alumno.alumno(obj['_id'],obj['nombreAlumno'],obj['apellidoAlumno']
                                    ,obj['dniAlumno'],obj['direccionAlumno'])
        lstAlumno.append(DataRestor)

def cargarNota():
    lstNota.clear()
    coll1 = conn.leerRegistrosTotal("nota")
    for obj in coll1: 
        DataRestor = nota.nota(obj['_id'],obj['descripcionNota'],obj['idCurso'],obj['idAlumno'])
        lstNota.append(DataRestor) 

def cargarCurso():
    lstCurso.clear()
    coll = conn.leerRegistrosTotal("curso")
    for obj in coll: 
        DataRestor = curso.curso(obj['_id'],obj['nombreCurso'])
        lstCurso.append(DataRestor)

def MostrarAlumnos():
    cargarAlumnos() 
    stopMenu = True
    while stopMenu:
        dicMenu = {"\t- Listar": 1, "\t- Buscar por Nombre": 2, "\t- Insertar": 3, "\t- Eliminar": 4
                    , "\t- Actualizar": 5}
        menuInicio = utils.Menu("Menu ALUMNOS", dicMenu)
        resMenu = menuInicio.mostrarMenu()
        if(resMenu == 1):
            log.debug("Listar")
            utils.listaSimple(lstAlumno,1,1) 
        elif(resMenu == 2):
            log.debug("Buscar por nombre")
            nombrebuscar = input("Nombre: ")
            fitro = {"nombreAlumno":f"{nombrebuscar}"}
            lstAlumnoTemp = []
            lstAlumnoTemp.clear()
            collt = conn.leerRegistros("alumno", fitro)
            for obj2 in collt:
                DataRestor2 = alumno.alumno(obj2['_id'],obj2['nombreAlumno'],obj2['apellidoAlumno']
                                            ,obj2['dniAlumno'],obj2['direccionAlumno'])
                lstAlumnoTemp.append(DataRestor2)
            utils.listaSimple(lstAlumnoTemp,1,1)
        elif(resMenu == 3):
            log.debug("Insertar")
            nombre = input("Nombre: ") 
            apellido = input("Apellido: ") 
            dni = utils.validarEntero("DNI: ") 
            Direccion = input("Direccion: ") 
            data ={
                    "nombreAlumno":f"{nombre}"
                    ,"apellidoAlumno":f"{apellido}"
                    ,"dniAlumno":f"{dni}"
                    ,"direccionAlumno":f"{Direccion}"
                }
            insertado = conn.insertarRegistro("alumno", data)
            if insertado:
                cargarAlumnos()
                print("Insertado correctamente.") 
            else:
                print("Error al insertar.") 
            input(MsjContinuar)
        elif(resMenu == 4):
            log.debug("Eliminar")
            utils.listaSimple(lstAlumno,1,0) 
            NombreEliminar = input("Nombre a Eliminar: ")
            dataEliminar = { "nombreAlumno": f"{NombreEliminar}" }
            coleli = conn.eliminarRegistro("alumno", dataEliminar)
            if coleli:
                cargarAlumnos()
                print("Eliminado correctamente.") 
            else:
                print("Error al eliminar.") 
            input(MsjContinuar)
        elif(resMenu == 5):
            log.debug("Eliminar Alumno")
            utils.listaSimple(lstAlumno,1,0) 
            NombreEliminar = input("Nombre a Actualizar: ")
            dataEliminar = { "nombreAlumno": f"{NombreEliminar}" }
            
            nombre = input("Nuevo Nombre: ") 
            apellido = input("Nuevo Apellido: ") 
            dni = utils.validarEntero("Nuevo DNI: ") 
            Direccion = input("Nueva Direccion: ") 
            dataActualizada ={
                    "nombreAlumno":f"{nombre}"
                    ,"apellidoAlumno":f"{apellido}"
                    ,"dniAlumno":f"{dni}"
                    ,"direccionAlumno":f"{Direccion}"
                } 
            coleli = conn.actualizarRegistro("alumno", dataEliminar,dataActualizada)
            if coleli:
                cargarAlumnos()
                print("Actualizado correctamente.") 
            else:
                print("Error al actualizar.") 
            input(MsjContinuar)
        elif(resMenu == 9):
            stopMenu = False 
        else:
            log.debug("volvemos a mostrar menu")

def MostrarNotas(): 
    stopMenu = True
    while stopMenu:
        dicMenu = {"\t- Listar": 1, "\t- Buscar por Alumno": 2, "\t- Insertar": 3, "\t- Eliminar": 4}
        menuInicio = utils.Menu("Menu NOTAS", dicMenu)
        resMenu = menuInicio.mostrarMenu()
        if(resMenu == 1):
            log.debug("Listar") 
            lstNotasTemp1 = []
            lstNotasTemp1.clear()
            collt = conn.leerRegistrosTotal("nota")
            for obj2 in collt: 
                idAlumnoT = obj2['idAlumno'] 
                FiltroAlumnoId = {"_id": ObjectId(f"{idAlumnoT}")}
                colltAlumno = conn.leerRegistro("alumno", FiltroAlumnoId)
                nombreAlumnoDes=colltAlumno['nombreAlumno']
                
                idCursoT = obj2['idCurso'] 
                FiltroCursoId = {"_id": ObjectId(f"{idCursoT}")}
                colltCurso = conn.leerRegistro("curso", FiltroCursoId)
                nombreCursoDes=colltCurso['nombreCurso']

                DataRestor2 = nota.notaDescripcion(obj2['_id'],obj2['descripcionNota'],nombreCursoDes
                                            ,nombreAlumnoDes)
                lstNotasTemp1.append(DataRestor2)
            utils.listaSimple(lstNotasTemp1,2,1)

        elif(resMenu == 2):
            log.debug("Buscar por Alumno")
            cargarAlumnos()
            utils.listaSimple(lstAlumno,1,0) 
            nombrebuscar = input("Alumno Nombre: ")
            fitro = {"nombreAlumno":f"{nombrebuscar}"} 
            colltAlum = conn.leerRegistro("alumno", fitro)
            idAlumno=colltAlum['_id']
            nombreAlumnoDes = colltAlum['nombreAlumno']
            fitroNotas = {"idAlumno":f"{idAlumno}"}            
            lstNotasTemp = []
            lstNotasTemp.clear()
            collt = conn.leerRegistros("nota", fitroNotas)
            for obj2 in collt: 
                idCursoT = obj2['idCurso'] 
                FiltroCursoId = {"_id": ObjectId(f"{idCursoT}")}
                colltCurso = conn.leerRegistro("curso", FiltroCursoId)
                nombreCursoDes=colltCurso['nombreCurso']
                DataRestor2 = nota.nota(obj2['_id'],obj2['descripcionNota'],nombreCursoDes
                                            ,nombreAlumnoDes)
                lstNotasTemp.append(DataRestor2)
            utils.listaSimple(lstNotasTemp,2,1)
        elif(resMenu == 3):
            log.debug("Insertar Notas")

            cargarAlumnos()
            utils.listaSimple(lstAlumno,1,0) 
            nombrebuscar = input("Nombre del Alumno: ")
            fitro = {"nombreAlumno":f"{nombrebuscar}"} 
            colltAlum = conn.leerRegistro("alumno", fitro)
            idAlumno=colltAlum['_id']

            cargarCurso()
            utils.listaSimple(lstCurso,3,0) 
            cursobuscar = input("Nombre del Curso: ")
            fitroCurso = {"nombreCurso":f"{cursobuscar}"} 
            colltCurs = conn.leerRegistro("curso", fitroCurso)
            idCurso=colltCurs['_id']

            Numnota = utils.validarEntero("Nota: ")
            data = { "descripcionNota":f"{Numnota}"
                    ,"idCurso":f"{idCurso}"
                    ,"idAlumno":f"{idAlumno}" }
            insertado = conn.insertarRegistro("nota", data)
            if insertado:
                cargarNota()
                print("Insertado correctamente.") 
            else:
                print("Error al insertar.") 
            input(MsjContinuar)
        elif(resMenu == 4):
            log.debug("Eliminar")
            

        elif(resMenu == 9):
            stopMenu = False 
        else:
            log.debug("volvemos a mostrar menu")

def MostrarCursos(): 
    stopMenu = True
    while stopMenu:
        dicMenu = {"\t- Listar": 1, "\t- Buscar por Nombre": 2, "\t- Insertar": 3, "\t- Eliminar": 4}
        menuInicio = utils.Menu("Menu CURSOS", dicMenu)
        resMenu = menuInicio.mostrarMenu()
        if(resMenu == 1):
            log.debug("Listar")
            cargarCurso() 
            utils.listaSimple(lstCurso,3,1)
        elif(resMenu == 2):
            log.debug("Buscar por nombre")
            cargarCurso() 
            utils.listaSimple(lstCurso,3,1)
        elif(resMenu == 3):
            log.debug("Insertar Cursos")
            nombre = input("Nombre del Curso: ")
            data = { "nombreCurso":f"{nombre}" }
            insertado = conn.insertarRegistro("curso", data)
            if insertado:
                cargarCurso()
                print("Insertado correctamente.") 
            else:
                print("Error al insertar.") 
            input(MsjContinuar)
        elif(resMenu == 4):
            log.debug("Actualizar")
            pass
        elif(resMenu == 9):
            stopMenu = False 
        else:
            log.debug("volvemos a mostrar menu")

stopMenuInicio = True
while stopMenuInicio:
    dicMenuInicio = {"\t- Alumnos": 1, "\t- Notas": 2, "\t- Cursos": 3}
    menuInicio = utils.Menu("Menu Inicio", dicMenuInicio)
    resMenuInicio = menuInicio.mostrarMenu()
    if(resMenuInicio == 1):
        log.debug("Mostramos Alumnos")
        MostrarAlumnos()
    elif(resMenuInicio == 2):
        log.debug("Mostramos Notas")
        MostrarNotas()
    elif(resMenuInicio == 3):
        log.debug("Mostramos Cursos")
        MostrarCursos()
    elif(resMenuInicio == 9):
        log.debug("finalizar Programa")
        stopMenuInicio = False
    else:
        log.debug("volvemos a mostrar menu")

