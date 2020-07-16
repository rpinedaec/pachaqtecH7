import utils
import conn
import mantenimiento
from time import sleep
import Matricula0
from pymongo import MongoClient
import Nota

def Reportes():
    while True:
        dictMenuReportes = {"Lista de notas": 1,
                            "Lista de profesores":2, 
                            "Lista de alumnos con su salon y sus profesores por curso":3,
                            "Reporte escolar":4, 
                            "Salir":9}
        MenuReportes = utils.Menu("Reportes",dictMenuReportes)
        MenuReportes.printMenu()
        opcionMenuReportes = MenuReportes.inputMenu()

        if(opcionMenuReportes == 1):
            x = conn.Conexion(4)
            x.ver_registros('Nota')
            input("Continuar?")
    
        elif(opcionMenuReportes == 2):
            print("ver profesores")
            x = conn.Conexion(4)
            while True:
                x.ver_registros('Profesores')
                input("Seguir?")
                break

        elif(opcionMenuReportes == 3):
            class color:
                PURPLE = '\033[95m'
                CYAN = '\033[96m'
                DARKCYAN = '\033[36m'
                BLUE = '\033[94m'
                GREEN = '\033[92m'
                YELLOW = '\033[93m'
                RED = '\033[91m'
                BOLD = '\033[1m'
                UNDERLINE = '\033[4m'
                CEND = '\033[0m'

            uri = 'mongodb://localhost:27017'
            database = 'wui'
            conne = MongoClient(uri)
            db = conne[str(f"{database}")]

            wui = db.Matricula.find({},{"alumnoMatricula":1,"_id":0})
            for obj in wui:
                y = obj.get('alumnoMatricula')
                o = y.get('nombreAlumno')
                print(color.BLUE+":::::::::::::::::: " + o + " ::::::::::::::::::"+color.CEND)
                yey = db.Matricula.find({},{"cursoMatricula":1,"_id":0})
                for obj in yey:
                    y = obj.get('cursoMatricula')
                for j in range(len(y)):
                    ai = y[j]
                    print(ai)
            input("Continuar?")

        elif(opcionMenuReportes == 4):
            x = conn.Conexion(4)
            x.ver_registros('Matricula')
            input("Continuar?")

        elif(opcionMenuReportes == 9):
            break

def IngresarNotas():
    while True:

        print("Elija el dni del Alumno al que quiere ponerle la nota")
        x = conn.Conexion(4)
        x.ver_registros('Alumnos')
        alumno = input()
        data = {'dniAlumno':alumno}
        alumnoNota = x.obtener_registro('Alumnos',data)
        if(alumnoNota):
            input("Seguir")
        else:
            input("Digite bien")
            break

        print("Elija el periodo donde quiere agregar la nota")
        x.ver_registros('Periodo')
        periodo = input()
        data = {'nombrePeriodo':periodo}
        periodoNota = x.obtener_registro('Periodo',data)
        if(periodoNota):
            input("Seguir")
        else:
            input("Digite bien")
            break

        print("Elija el curso donde quiere agregar la nota")
        x.ver_registros('Curso')
        curso = input()
        data = {'nombreCurso':curso}
        cursoNota = x.obtener_registro('Curso',data)
        if(cursoNota):
            input("Seguir")
        else:
            input("Digite bien")
            break

        print("Ingrese la nota que desea añadir")
        nota = int(input())
        nuevaNota = Nota.Nota(alumnoNota,periodoNota,cursoNota,nota)
        query = x.insertar_registro('Nota',nuevaNota.dictNota())
        if(query):
            print("Se agrego correctamente")
            break
        else:
            print("Hubo un error")
            break
    input("Continuar?")
        



def Matricula():
    while True:
        dictMenuMatricula = {"Generar Matricula": 1, "Eliminar Matricula":2, "Salir":9}
        MenuMatricula = utils.Menu("Matricula",dictMenuMatricula)
        MenuMatricula.printMenu()
        opcionMenuMatricula = MenuMatricula.inputMenu()

        if(opcionMenuMatricula == 1):
            print("Eliga el dni alumno que desea matricular")
            x = conn.Conexion(4)
            x.ver_registros('Alumnos')
            alumno = input()
            data = {'dniAlumno':alumno}
            alumnoMatricula = x.obtener_registro('Alumnos',data)
            if(alumnoMatricula):
                input("Seguir")
            else:
                input("Digite bien")
                break

            print("Elija el periodo en donde lo desea matricular")
            x.ver_registros('Periodo')
            periodo = input()
            data = {'nombrePeriodo':periodo}
            periodoMatricula = x.obtener_registro('Periodo',data)
            if(periodoMatricula):
                input("Seguir")
            else:
                input("Digite bien")
                break
            lstCurso = []
            while True:
                print("Elija el curso en donde lo desea matricular")
                x.ver_registros('Curso')
                curso = input()
                data = {'nombreCurso':curso}
                cursoMatricula = x.obtener_registro('Curso',data)
                if(cursoMatricula):
                    input("Seguir")
                else:
                    input("Digite bien")
                    break

                print("Elija el dni del profesor del curso")
                x.ver_registros('Profesores')
                profesor = input()
                data = {'dniProfesor':profesor}
                profesorMatricula = x.obtener_registro('Profesores',data)
                if(profesorMatricula):
                    input("Seguir")
                else:
                    input("Digite bien")
                    break

                print("Elija el salon del profesor")
                x.ver_registros('Salon')
                salon = input()
                data = {'nombreSalon':salon}
                salonMatricula = x.obtener_registro('Salon',data)
                if(salonMatricula):
                    input("Seguir")
                else:
                    input("Digite bien")
                    break

                dictCurso = {'curso':cursoMatricula,'profesor':profesorMatricula,'salon':salonMatricula}
                lstCurso.append(dictCurso)

                opcion = input("Desea agregar otro curso? Si/No -> ")
                if(opcion == "No"):
                    break
            
            nuevaMatricula = Matricula0.Matricula(alumnoMatricula,periodoMatricula,lstCurso)
            query = x.insertar_registro('Matricula',nuevaMatricula.dictMatricula())
            if(query):
                print("Se agrego correctamente")
            else:
                print("Hubo un error")
            input("Continuar?")

        if(opcionMenuMatricula == 2):
            print("Elija el nombre del alumno de la matricula que desea eliminar")
            x = conn.Conexion(4)
            x.ver_registros('Matricula')
            nomAluMatricula = input()
            condition = {'alumnoMatricula':nomAluMatricula}
            query = x.eliminar_registro('Matricula',condition)
            if(query):
                print("Se elimino correctamente")
            else:
                print("Hubo un error")
            input("Continuar?")

        if(opcionMenuMatricula == 9):
            break


while True:
    dictMenuPrincipal = {"Mantenimientos": 1, "Matricula":2, "Ingresar Notas":3, "Reportes": 4, "Salir":9}
    MenuPrincipal = utils.Menu("Principal",dictMenuPrincipal)
    MenuPrincipal.printMenu()
    opcionMenuPrincipal = MenuPrincipal.inputMenu()

    if(opcionMenuPrincipal == 1):
        mantenimiento.Mantenimiento()

    elif(opcionMenuPrincipal == 2):
        Matricula()

    elif(opcionMenuPrincipal == 3):
        IngresarNotas()

    elif(opcionMenuPrincipal == 4):
        Reportes()

    elif(opcionMenuPrincipal == 9):
        break