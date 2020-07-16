import utils
import conn
import Alumnos
import Profesores
import Salon
import Periodo
import Curso

def MantenimientoAlumnos():
    while True:
        dicMenuAlumnos = {"Agregar Alumno": 1, "Modificar Alumno": 2, "Eliminar Alumno": 3, "Ver Alumnos": 4, "Salir":9}
        menuAlumnos = utils.Menu("Alumnos",dicMenuAlumnos)
        menuAlumnos.printMenu()
        opcionMenuAlumnos = menuAlumnos.inputMenu()
        
        if(opcionMenuAlumnos == 1):
            print("Entro a agregar Alumno")
            print("Ingrese el dni del Alumno")
            dniAlumno = input()
            print("Ingrese el nombre del Alumno")
            nomAlumno = input()
            print("Ingrese el apellido del Alumno")
            apeAlumno = input()
            print("Ingrese el correo del Alumno")
            correoAlumno = input()
            x = conn.Conexion(4)
            nuevoAlumno = Alumnos.Alumnos(dniAlumno,nomAlumno,apeAlumno,correoAlumno)
            query = x.insertar_registro('Alumnos',nuevoAlumno.dictAlumno())
            if(query):
                print("Se agrego correctamente")
            else:
                print("Hubo un error")
            input("Continuar?")
        elif(opcionMenuAlumnos == 2):
            print("Elija el dni del Alumno que quiera modificar")
            x = conn.Conexion(4)
            x.ver_registros('Alumnos')
            dniA = input()
            print("Ingrese el nuevo dni del Alumno")
            nuevoDniA = input()
            print("Ingrese el nuevo nombre para el Alumno")
            nuevoNomA = input()
            print("Ingrese el nuevo apellido para el Alumno")
            nuevoApeA = input()
            print("Ingrese el nuevo correo del Alumno")
            nuevoCorreoA = input()
            condition = {'dniAlumno':dniA}
            change = Alumnos.Alumnos(nuevoDniA,nuevoNomA,nuevoApeA,nuevoCorreoA)
            query = x.actualizar_registro('Alumnos',condition,change.dictAlumno())
            if(query):
                print("Se actualizo correctamente")
            else:
                print("No se actualizo correctamente")
                print("Digite bien")
            input("Continuar?")
        elif(opcionMenuAlumnos == 3):
            print("Elija el dni del Alumno que desea eliminar")
            x = conn.Conexion(4)
            x.ver_registros('Alumnos')
            dniA = input()
            condition = {'dniAlumno':dniA}
            query = x.eliminar_registro('Alumnos',condition)
            if(query):
                print("Se elimino correctamente")
            else:
                print("Digite bien")
            input("Continuar?")
        elif(opcionMenuAlumnos == 4):
            print("Usted esta viendo la lista de Alumnos:")
            x = conn.Conexion(4)
            x.ver_registros('Alumnos')
            input("Continuar?")

        elif(opcionMenuAlumnos == 9):
            break

def MantenimientoPeriodo():
    while True:
        dicMenuPeriodo = {"Agregar Periodo": 1, "Modificar Periodo": 2, "Eliminar Periodo": 3, "Ver Periodos": 4, "Salir":9}
        menuPeriodo = utils.Menu("Periodo",dicMenuPeriodo)
        menuPeriodo.printMenu()
        opcionMenuPeriodo = menuPeriodo.inputMenu()
        
        if(opcionMenuPeriodo == 1):
            print("Entro a agregar Periodo")
            print("Ingrese el nombre del Periodo")
            nomPeriodo = input()
            x = conn.Conexion(4)
            nuevoPeriodo = Periodo.Periodo(nomPeriodo)
            query = x.insertar_registro('Periodo',nuevoPeriodo.dictPeriodo())
            if(query):
                print("Se agrego correctamente")
            else:
                print("Hubo un error")
            input("Continuar?")

        elif(opcionMenuPeriodo == 2):
            print("Elija el nombre del Periodo que quiera modificar")
            x = conn.Conexion(4)
            x.ver_registros('Periodo')
            nomP = input()
            print("Ingrese el nuevo nombre para el Periodo")
            nuevoNomP = input()
            condition = {'nombrePeriodo':nomP}
            change = Periodo.Periodo(nuevoNomP)
            query = x.actualizar_registro('Periodo',condition,change)
            if(query):
                print("Se actualizo correctamente")
            else:
                print("Hubo un error")
            input("Continuar?")

        elif(opcionMenuPeriodo == 3):
            print("Elija el nombre del Periodo que desea eliminar")
            x = conn.Conexion(4)
            x.ver_registros('Periodo')
            nomP = input()
            condition = {'nombrePeriodo':nomP}
            query = x.eliminar_registro('Periodo',condition)
            if(query):
                print("Se elimino correctamente")
            else:
                print("Hubo un error")
            input("Continuar?")

        elif(opcionMenuPeriodo == 4):
            print("Usted esta viendo la lista de Periodos:")
            x = conn.Conexion(4)
            x.ver_registros('Periodo')
            input("Continuar?")

        elif(opcionMenuPeriodo == 9):
            break

def MantenimientoCurso():
    while True:
        dicMenuCurso = {"Agregar Curso": 1, "Modificar Curso": 2, "Eliminar Curso": 3, "Ver Cursos": 4, "Salir":9}
        menuCurso = utils.Menu("Curso",dicMenuCurso)
        menuCurso.printMenu()
        opcionMenuCurso = menuCurso.inputMenu()
        
        if(opcionMenuCurso == 1):
            print("Entro a agregar Curso")
            print("Ingrese el nombre del Curso")
            nomCurso = input()
            x = conn.Conexion(4)
            nuevoCurso = Curso.Curso(nomCurso)
            query = x.insertar_registro('Curso',nuevoCurso.dictCurso())
            if(query):
                print("Se agrego correctamente")
            else:
                print("Hubo un error")
            input("Continuar?")

        elif(opcionMenuCurso == 2):
            print("Elija el nombre del Curso que quiera modificar")
            x = conn.Conexion(4)
            x.ver_registros('Curso')
            nomC = input()
            print("Ingrese el nuevo nombre para el Curso")
            nuevoNomC = input()
            condition = {'nombreCurso':nomC}
            change = Curso.Curso(nuevoNomC)
            query = x.actualizar_registro('Curso',condition,change)
            if(query):
                print("Se actualizo correctamente")
            else:
                print("Hubo un error")
            input("Continuar?")

        elif(opcionMenuCurso == 3):
            print("Elija el nombre del Curso que desea eliminar")
            x = conn.Conexion(4)
            x.ver_registros('Curso')
            nomC = input()
            condition = {'nombreCurso':nomC}
            query = x.eliminar_registro('Curso',condition)
            if(query):
                print("Se elimino correctamente")
            else:
                print("Hubo un error")
            input("Continuar?")

        elif(opcionMenuCurso == 4):
            print("Usted esta viendo la lista de Cursos:")
            x = conn.Conexion(4)
            x.ver_registros('Curso')
            input("Continuar?")

        elif(opcionMenuCurso == 9):
            break

def MantenimientoProfesores():
    while True:
        dicMenuProfesores = {"Agregar Profesor": 1, "Modificar Profesor": 2, "Eliminar Profesor": 3, "Ver Profesores": 4, "Salir":9}
        menuProfesores = utils.Menu("Profesores",dicMenuProfesores)
        menuProfesores.printMenu()
        opcionMenuProfesores = menuProfesores.inputMenu()
        
        if(opcionMenuProfesores == 1):
            print("Entro a agregar Profesor")
            print("Ingrese el dni del Profesor")
            dniProfesor = input()
            print("Ingrese el nombre del Profesor")
            nomProfesor = input()
            print("Ingrese el apellido del Profesor")
            apeProfesor = input()
            print("Ingrese el correo del Profesor")
            correoProfesor = input()
            x = conn.Conexion(4)
            nuevoProfesor = Profesores.Profesores(dniProfesor,nomProfesor,apeProfesor,correoProfesor)
            query = x.insertar_registro('Profesores',nuevoProfesor.dictProfesor())
            if(query):
                print("Se agrego correctamente")
            else:
                print("Hubo un error")
            input("Continuar?")

        elif(opcionMenuProfesores == 2):
            print("Elija el dni del Profesor que quiera modificar")
            x = conn.Conexion(4)
            x.ver_registros('Profesores')
            dniP = input()
            print("Ingrese el nuevo dni del Profesor")
            nuevoDniP = input()
            print("Ingrese el nuevo nombre para el Profesor")
            nuevoNomP = input()
            print("Ingrese el nuevo apellido para el Profesor")
            nuevoApeP = input()
            print("Ingrese el nuevo correo del Profesor")
            nuevoCorreoP = input()
            condition = {'dniProfesor':dniP}
            change = Profesores.Profesores(nuevoDniP,nuevoNomP,nuevoApeP,nuevoCorreoP)
            query = x.actualizar_registro('Profesores',condition,change.dictProfesor())
            if(query):
                print("Se actualizo correctamente")
            else:
                print("No se actualizo correctamente")
                print("Digite bien")
            input("Continuar?")

        elif(opcionMenuProfesores == 3):
            print("Elija el dni del profesor que desea eliminar")
            x = conn.Conexion(4)
            x.ver_registros('Profesores')
            dniP = input()
            condition = {'dniProfesor':dniP}
            query = x.eliminar_registro('Profesores',condition)
            if(query):
                print("Se elimino correctamente")
            else:
                print("Digite bien")
            input("Continuar?")

        elif(opcionMenuProfesores == 4):
            print("Usted esta viendo la lista de profesores:")
            x = conn.Conexion(4)
            x.ver_registros('Profesores')
            input("Continuar?")

        elif(opcionMenuProfesores == 9):
            break

def MantenimientoSalon():
    while True:
        dicMenuSalon = {"Agregar Salon": 1, "Modificar Salon": 2, "Eliminar Salon": 3, "Ver Salones": 4, "Salir":9}
        menuSalon = utils.Menu("Salon",dicMenuSalon)
        menuSalon.printMenu()
        opcionMenuSalon = menuSalon.inputMenu()
        
        if(opcionMenuSalon == 1):
            print("Entro a agregar Salon")
            print("Ingrese el nombre del Salon")
            nomSalon = input()
            x = conn.Conexion(4)
            nuevoSalon = Salon.Salon(nomSalon)
            query = x.insertar_registro('Salon',nuevoSalon.dictSalon())
            if(query):
                print("Se agrego correctamente")
            else:
                print("Hubo un error")
            input("Continuar?")

        elif(opcionMenuSalon == 2):
            print("Elija el nombre del Salon que quiera modificar")
            x = conn.Conexion(4)
            x.ver_registros('Salon')
            nomS = input()
            print("Ingrese el nuevo nombre para el Salon")
            nuevoNomS = input()
            condition = {'nombreSalon':nomS}
            change = Salon.Salon(nuevoNomS)
            query = x.actualizar_registro('Salon',condition,change)
            if(query):
                print("Se actualizo correctamente")
            else:
                print("Hubo un error")
            input("Continuar?")

        elif(opcionMenuSalon == 3):
            print("Elija el nombre del Salon que desea eliminar")
            x = conn.Conexion(4)
            x.ver_registros('Salon')
            nomS = input()
            condition = {'nombreSalon':nomS}
            query = x.eliminar_registro('Salon',condition)
            if(query):
                print("Se elimino correctamente")
            else:
                print("Hubo un error")
            input("Continuar?")

        elif(opcionMenuSalon == 4):
            print("Usted esta viendo la lista de Salones:")
            x = conn.Conexion(4)
            x.ver_registros('Salon')
            input("Continuar?")

        elif(opcionMenuSalon == 9):
            break

def Mantenimiento():
    while True:
        dicMenuMantenimiento = {"Alumnos": 1, "Periodo": 2,"Curso": 3, "Profesores":4, "Salon":5, "Salir":9}
        menuMantenimiento = utils.Menu("Mantenimiento",dicMenuMantenimiento)
        menuMantenimiento.printMenu()
        opcionMenuMantenimiento = menuMantenimiento.inputMenu()

        if(opcionMenuMantenimiento == 1):   
            MantenimientoAlumnos()

        elif(opcionMenuMantenimiento == 2):
            MantenimientoPeriodo()

        elif(opcionMenuMantenimiento == 3):
            MantenimientoCurso()
        
        elif(opcionMenuMantenimiento == 4):
            MantenimientoProfesores()

        elif(opcionMenuMantenimiento == 5):
            MantenimientoSalon()

        elif(opcionMenuMantenimiento == 9):
            break
