import conexion
import pymongo
import salon
import utils


lstSalon=[]
log = utils.log("INIT")
MsjContinuar = "Enter para continuar..."
conn = conexion.conexionBDD()

def cargarSalon():
    lstSalon.clear()
    coll1 = conn.leerRegistrosTotal("salon")
    for obj in coll1: 
        DataRestor = salon.salon(obj['_id'],obj['nombreSalon'])
        lstSalon.append(DataRestor) 

def MostrarSalon(): 
    stopMenu = True
    while stopMenu:
        dicMenu = {"\t- Listar": 1, "\t- Buscar por Salon": 2, "\t- Insertar": 3, "\t- Eliminar": 4}
        menuInicio = utils.Menu("Menu Salon", dicMenu)
        resMenu = menuInicio.mostrarMenu()
        if(resMenu == 1):
            log.debug("Listar")
            cargarSalon() 
            utils.listaSimple(lstSalon,4,1)
        elif(resMenu == 2):
            log.debug("Buscar por Salon")
            cargarSalon() 
            utils.listaSimple(lstSalon,4,1)
        elif(resMenu == 3):
            log.debug("Insertar Salon")
            nombre = input("Nombre del Salon: ")
            data = { "nombreSalon":f"{nombre}" }
            insertado = conn.insertarRegistro("salon", data)
            if insertado:
                cargarSalon()
                print("Insertado correctamente.") 
            else:
                print("Error al insertar.") 
            input(MsjContinuar)
        elif(resMenu == 4):
            log.debug("Eliminar")
            utils.listaSimple(lstSalon,4,0) 
            NombreEliminar = input("Nombre a Eliminar: ")
            dataEliminar = { "nombreSalon": f"{NombreEliminar}" }
            coleli = conn.eliminarRegistro("salon", dataEliminar)
            if coleli:
                cargarSalon()
                print("Eliminado correctamente.") 
            else:
                print("Error al eliminar.") 
            input(MsjContinuar)
            
        elif(resMenu == 9):
            stopMenu = False 
        else:
            log.debug("volvemos a mostrar menu")

stopMenuInicio = True
while stopMenuInicio:
    dicMenuInicio = {"\t- Alumnos": 1, "\t- Notas": 2, "\t- Cursos": 3,"\t- Salon": 4}
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
    elif(resMenuInicio == 4):
        log.debug("Mostramos Salones")
        MostrarSalon()
    elif(resMenuInicio == 9):
        log.debug("finalizar Programa")
        stopMenuInicio = False
    else:
        log.debug("volvemos a mostrar menu")
