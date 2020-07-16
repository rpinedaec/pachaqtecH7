import utils
import cruds
from time import sleep

__log = utils.log("Principal")
__log.info("Inicio del sistema")

#menu empleado
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
                tplAlumno = ("1. Agregar Alumno", "2. Listar Alumnos", "3. Modificar Alumno", "4. Eliminar Alumno", "5. Regresar")
                menuAlumno = utils.Menu("Menu Alumno", tplAlumno)
                resmenuAlumno = menuAlumno.MostrarMenu()
                #Agregar Alumno
                if resmenuAlumno == 1:
                    cruds.ingresarAlumno()
                    sleep(2)
                    __log.debug("Se ingresaron los datos del alumno")
                #Listar Alumno
                elif resmenuAlumno == 2:
                    cruds.listarAlumnos()
                    sleep(2)
                #Modificar Alumno
                elif resmenuAlumno == 3:                    
                    cruds.listarAlumnos()                        
                    idAlumno = cruds.buscarAlumno()
                    cruds.modificarAlumno(idAlumno)
                    sleep(2)
                    __log.debug("Se modificaron los datos del alumno")
                #Elimar Alumno
                elif resmenuAlumno == 4:                    
                    cruds.listarAlumnos()                        
                    idAlumno = cruds.buscarAlumno()
                    cruds.eliminarAlumno(idAlumno)
                    sleep(2)
                    __log.debug("Se eliminaron los datos del alumno")
                elif resmenuAlumno == 5:
                    mantenimientoEmpleado()
                elif resmenuAlumno == 0:
                    utils.Salir()
                else:
                    print("Ingrese una opcion valida")
        #Menu Empleado Docente
        elif resmenuEmpleado == 2:
            __log.info("Menu Empleado --> Docente")
            stopMenuDocente = True
            while stopMenuDocente:
                tplDocente = ("1. Agregar Docente", "2. Listar Docente", "3. Modificar Docente", "4. Eliminar Docente", "5. Regresar")
                menuDocente = utils.Menu("Menu Docente", tplDocente)
                resmenuDocente = menuDocente.MostrarMenu()
                #Agregar Docente
                if resmenuDocente == 1:
                    cruds.ingresarDocente()
                    sleep(2)
                    __log.debug("Se ingresaron los datos del docente")
                #Listar Docente
                elif resmenuDocente == 2:
                    cruds.listarDocente()
                    sleep(2)
                #Modificar Docente
                elif resmenuDocente == 3:                    
                    cruds.listarDocente()                        
                    idDocente = cruds.buscarDocente()
                    cruds.modificarDocente(idDocente)
                    sleep(2)
                    __log.debug("Se modificaron los datos del docente")
                #Elimar Docente
                elif resmenuDocente == 4:                    
                    cruds.listarDocente()                        
                    idDocente = cruds.buscarDocente()
                    cruds.eliminarDocente(idDocente)
                    sleep(2)
                    __log.debug("Se eliminaron los datos del docente")
                elif resmenuDocente == 5:
                    mantenimientoEmpleado()
                elif resmenuDocente == 0:
                    utils.Salir()
                else:
                    print("Ingrese una opcion valida")
        #Menu empleado Cursos
        elif resmenuEmpleado == 3:
            __log.info("Menu Empleado --> Cursos")
            stopMenuCursos = True
            while stopMenuCursos:
                tplCursos = ("1. Agregar Cursos", "2. Listar Cursos", "3. Modificar Cursos", "4. Eliminar Cursos", "5. Regresar")
                menuCursos = utils.Menu("Menu Cursos", tplCursos)
                resmenuCursos = menuCursos.MostrarMenu()
                #Agregar Cursos
                if resmenuCursos == 1:
                    cruds.ingresarCurso()
                    sleep(2)
                    __log.debug("Se ingresaron los datos del cursos")
                #Listar Cursos
                elif resmenuCursos == 2:
                    cruds.listarCurso()
                    sleep(2)
                #Modificar Cursos
                elif resmenuCursos == 3:                    
                    cruds.listarCurso()                        
                    idCursos = cruds.buscarCurso()
                    cruds.modificarCurso(idCursos)
                    sleep(2)
                    __log.debug("Se modificaron los datos del Cursos")
                #Elimar Cursos
                elif resmenuCursos == 4:                    
                    cruds.listarCurso()                        
                    idCursos = cruds.buscarCurso()
                    cruds.eliminarCurso(idCursos)
                    sleep(2)
                    __log.debug("Se eliminaron los datos del Cursos")
                elif resmenuCursos == 5:
                    mantenimientoEmpleado()
                elif resmenuCursos == 0:
                    utils.Salir()
                else:
                    print("Ingrese una opcion valida")
        #Menu empleado Salones
        elif resmenuEmpleado == 4:
            __log.info("Menu Empleado --> Salones")
            stopMenuSalones = True
            while stopMenuSalones:
                tplSalones = ("1. Agregar Salones", "2. Listar Salones", "3. Modificar Salones", "4. Eliminar Salones", "5. Regresar")
                menuSalones = utils.Menu("Menu Salones", tplSalones)
                resmenuSalones = menuSalones.MostrarMenu()
                #Agregar Salones
                if resmenuSalones == 1:
                    cruds.ingresarSalon()
                    sleep(2)
                    __log.debug("Se ingresaron los datos del Salones")
                #Listar Salones
                elif resmenuSalones == 2:
                    cruds.listarSalon()
                    sleep(2)
                #Modificar Salones
                elif resmenuSalones == 3:                    
                    cruds.listarSalon()                        
                    idSalones = cruds.buscarSalon()
                    cruds.modificarSalon(idSalones)
                    sleep(2)
                    __log.debug("Se modificaron los datos del Salones")
                #Elimar Salones
                elif resmenuSalones == 4:                    
                    cruds.listarSalon()                        
                    idSalones = cruds.buscarSalon()
                    cruds.eliminarSalon(idSalones)
                    sleep(2)
                    __log.debug("Se eliminaron los datos del Salones")
                elif resmenuSalones == 5:
                    mantenimientoEmpleado()
                elif resmenuSalones == 0:
                    utils.Salir()
                else:
                    print("Ingrese una opcion valida")
        #Menu empleado Periodo Escolar
        elif resmenuEmpleado == 5:
            __log.info("Menu Empleado --> Periodo")
            stopMenuPeriodo = True
            while stopMenuPeriodo:
                tplPeriodo = ("1. Agregar Periodo", "2. Listar Periodo", "3. Modificar Periodo", "4. Eliminar Periodo", "5. Regresar")
                menuPeriodo = utils.Menu("Menu Periodo", tplPeriodo)
                resmenuPeriodo = menuPeriodo.MostrarMenu()
                #Agregar Periodo
                if resmenuPeriodo == 1:
                    cruds.ingresarPeriodo()
                    sleep(2)
                    __log.debug("Se ingresaron los datos del Periodo")
                #Listar Periodo
                elif resmenuPeriodo == 2:
                    cruds.listarPeriodo()
                    sleep(2)
                #Modificar Periodo
                elif resmenuPeriodo == 3:                    
                    cruds.listarPeriodo()                        
                    idPeriodo = cruds.buscarPeriodo()
                    cruds.modificarPeriodo(idPeriodo)
                    sleep(2)
                    __log.debug("Se modificaron los datos del Periodo")
                #Elimar Periodo
                elif resmenuPeriodo == 4:                    
                    cruds.listarPeriodo()                        
                    idPeriodo = cruds.buscarPeriodo()
                    cruds.eliminarPeriodo(idPeriodo)
                    sleep(2)
                    __log.debug("Se eliminaron los datos del Periodo")
                elif resmenuPeriodo == 5:
                    mantenimientoEmpleado()
                elif resmenuPeriodo == 0:
                    utils.Salir()
                else:
                    print("Ingrese una opcion valida")
        #Menu empleado Matricula
        elif resmenuEmpleado == 6:
            __log.info("Menu Empleado --> Matricula")
            stopMenuMatricula = True
            while stopMenuMatricula:
                tplMatricula = ("1. Matricular Alumno", "2. Listar Matricula", "3. Asignar Docente a Curso", "4. Asignar Curso a Alumno", "5. Regresar")
                menuMatricula = utils.Menu("Menu Matricula", tplMatricula)
                resmenuMatricula = menuMatricula.MostrarMenu()
                #Agregar Matricula
                if resmenuMatricula == 1:
                    cruds.ingresarMatricula()
                #Lista todas las Matriculas
                elif resmenuMatricula == 2:
                    cruds.listarMatricula()  
                #Asignar Docente a Curso
                elif resmenuMatricula == 3:
                    cruds.docenteCurso()
                elif resmenuMatricula == 4:
                    cruds.alumnoCurso()              
                elif resmenuMatricula == 5:
                    mantenimientoEmpleado()
                elif resmenuMatricula == 0:
                    utils.Salir()
        #Regresar al menu anterior
        elif resmenuEmpleado == 7:
            InicioPrincipal()
        elif resmenuEmpleado == 0:
            utils.Salir()
        else:
            pass

def InicioPrincipal():            
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
            tplAlumnoP = ('1. Listar todos los alumnos', '2. Listar de Menor a Mayor Nota', '3.  Listar de Mayor a Menor Nota', '4. Regresar')
            menuAlumnoP = utils.Menu("Menu Alumno", tplAlumnoP)
            resMenuAlumnoP = menuAlumnoP.MostrarMenu()
            if resMenuAlumnoP == 1:
                cruds.listarNotas()
                sleep(2)
            elif resMenuAlumnoP == 2:
                cruds.listarNotasAsc()
                sleep(2)
            elif resMenuAlumnoP == 3:
                cruds.listarNotasDesc()
                sleep(2)
            else:
                utils.Salir()

        elif(resMenuInicio == 3):
            __log.debug("Mostramos el Menu Docente")
            tplMenuDocente = ('1. Listar Docente y Curso', '2. Asignar Notas', '3. Regresar')
            menuDocente = utils.Menu("Menu Docente", tplMenuDocente)
            resMenuDocente = menuDocente.MostrarMenu()
            if resMenuDocente == 1:
                cruds.listarAlumnoCurso()
                input("Continuar")
            elif resMenuDocente == 2:
                cruds.listarAlumnoCurso()
                IdAlumnoCurso = cruds.buscarAlumnoCurso()            
                cruds.asignarNota(IdAlumnoCurso)
        else:
            __log.debug("Volvemos a mostrar menu")
            utils.Salir()

InicioPrincipal()