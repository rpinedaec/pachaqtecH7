import utils
import conexion
import alumno
import docente
import salon
import periodo
import notas
import promedio

import curso
log = utils.log("INIT")
log.info("inicio del programa")
# lstClientes = []
# lstTipoPago = []
lstEmpresa = []
lstProductos = []
lstXProductos = []
lstFactura=[]
lstFacDetalle=[]
global intBDD
intBDD=0


def mantenimento(resMenu):
    if resMenu == 1:
        log.debug("escogio 1")  
        alumno.alumno.mantenimientoalumno(intBDD)
    elif resMenu == 2:
        log.debug("escogio 2")  
        docente.docente.mantenimientodocente(intBDD)
    elif resMenu == 3:
        log.debug("escogio 3") 
        curso.curso.mantenimientosalon(intBDD) 
    elif resMenu == 4:
        log.debug("escogio 4")
        notas.notas.mantenimientonotas(intBDD)
    elif resMenu == 5:
        log.debug("escogio 5")
        periodo.periodo.mantenimientoperiodo(intBDD)
    elif resMenu == 6:
        log.debug("escogio 6")
        promedio.promedio.mantenimientopromedio(intBDD)
    elif resMenu == 7:
        log.debug("escogio 7")
        salon.salon.mantenimientosalon(intBDD)     
    else:
        log.debug(f"escogio {resMenu}")
        
def menuprincipal():
    stopMenuInicio = True
    while stopMenuInicio:
        dicMenuInicio = {"\t- Mantenimiento": 1}
        menuInicio = utils.Menu("Menu Inicio", dicMenuInicio)
        resMenuInicio = menuInicio.mostrarMenu()
        if(resMenuInicio == 1):
            log.debug("Mostramos los Mantenimientos")
            dicMenuMantenimiento = {"\t- Alumnos": 1, "\t- Docentes": 2,
                                    "\t - Curso": 3, "\t - Notas": 4,
                                    "\t- Periodo": 5, "\t- Promedio": 6}
            menuMantenimiento = utils.Menu(
                "Menu Mantenimiento", dicMenuMantenimiento)
            resMenuMantenimiento = menuMantenimiento.mostrarMenu()
            mantenimento(resMenuMantenimiento)
        elif(resMenuInicio == 9):
            log.debug("finalizar Programa")
        else:
            log.debug("volvemos a mostrar menu")
            stopMenuInicio = False
            

stopMenuInicioBD = True
while stopMenuInicioBD:
    dicMenuInicioBD = {"\t- Ingresar a Base Datos Mysql": 1,
                        "\t- Ingresar a Base Datos MongoDB": 2}
    menuInicioBD = utils.Menu("Menu Ingreso Base De Datos", dicMenuInicioBD)
    resMenuInicioBD = menuInicioBD.mostrarMenu()
    if(resMenuInicioBD == 1):
                log.debug("Ingresamos a la bd mysql") 
                intBDD=1
                menuprincipal()
    elif(resMenuInicioBD == 2):
                log.debug("Mostramos el Menu Buscar Factura")
                intBDD = 2
                menuprincipal()
    elif(resMenuInicioBD == 9):
                log.debug("finalizar Programa")

else:
    log.debug("volvemos a mostrar menu")
    stopMenuInicioBD = False


