import utils
import cruds

__log = utils.log("Principal")
__log.info("Inicio del sistema")

def mantenimientoEmpleado():
    tplEmpleado = ("1. Alumno", "2. Docente", "3. Cursos", "4. Salones", 
                    "5. Periodo Escolar", "6. Matricula", "7. Regresar")
    menuEmpleado = utils.Menu("Menu Empleado", tplEmpleado)
    resmenuEmpleado = menuEmpleado.MostrarMenu()

    stopMenuEmpleado = True
    while stopMenuEmpleado:
        if resmenuEmpleado == 1:
            __log.info("Menu Empleado --> Alumno")
            stopMenuAlumno = True
            while stopMenuAlumno:
                tplAlumno = ("1. Agregar Alumno", "2.")
                menuAlumno = utils.Menu("Menu Alumno", tplAlumno)
                resmenuAlumno = menuAlumno.MostrarMenu()
                if resmenuAlumno == 1:
                    cruds.ingresarAlumno()
                elif resmenuAlumno == 2:
                    pass               
                else:
                    pass
        else:
            pass
            
stopMenuInicio = True
while stopMenuInicio:
    dicMenuInicio = ("1. Empleado", "2. Alumno", "3. Docente")
    menuInicio = utils.Menu("Menu Inicio", dicMenuInicio)
    resMenuInicio = menuInicio.MostrarMenu()
    if(resMenuInicio == 1):
        __log.debug("Mostramos el Menu Empleado")
        mantenimientoEmpleado()
        #cargarObjetos()

    elif(resMenuInicio == 2):
        __log.debug("Mostramos el Menu Alumno")
        print("Alumno") 

    elif(resMenuInicio == 3):
        __log.debug("Mostramos el Menu Docente")
        print("Docente")

    else:
        __log.debug("Volvemos a mostrar menu")
        utils.Salir()
