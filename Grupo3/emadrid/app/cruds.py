import conexion
import querys
from time import sleep

#Empleado -- Alumno
def ingresarAlumno():
    nombre = input("Ingrese Nombre del Alumno:\n")
    apellido = input("Ingrese Apellido del Alumno:\n")
    correo = input("Ingrese Correo del Alumno:\n")
    fechanac = input("Ingrese Fecha Nacimiento del Alumno:\n")
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    consulta = query.InsertAlumno(nombre, apellido, correo, fechanac)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print("Añadido")
    else:
        print("Fallaste")
    input("Desea continuar")

#####EMPLEADOR -- DOCENTE####
#Metodo Ingresar Nuevo Docente
def ingresarDocente():
    nombre = input("Ingrese Nombre del Docente:\n")
    dni = input("Ingrese DNI del Docente:\n")
    correo = input("Ingrese Correo del Docente:\n")
    fechanac = input("Ingrese Fecha de Nacimiento del Docente:\n")
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    consulta = query.InsertDocente(nombre, dni, correo, fechanac)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print("Añadido")
    else:
        print("Fallaste")
    input("Desea continuar")

####INICIO METODOS DOCENTE####
#Metodo Listar Docentes
def listarDocente():
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    consulta = query.ListarAllDocentes()
    resconn = conn.consultarBDD(consulta)
    #Imprime Cabecera
    print("ID\t", "Nombre\t\t", "DNI\t\t", "Correo\t\t\t", "Fecha Nacimiento""\t")
    #Mostrar Lista de Docentes
    for tplDocente in resconn:
        print(tplDocente[0],"\t", tplDocente[1],"\t", tplDocente[2],"\t", tplDocente[3],"\t\t", tplDocente[4])

#Metodo Buscar Docentes por ID
def buscarDocente():
    try:
        idDocente = int(input("Ingrese el ID del Docente que desea modificar:\n"))
        conn = conexion.conexionBDD(1)
        query = querys.Querys()
        consulta = query.BuscarDocente(idDocente)
        resconn = conn.consultarBDD(consulta)
        for tplDocente in resconn:
            print(tplDocente[0], tplDocente[1], tplDocente[2], tplDocente[3], tplDocente[4])
        return idDocente
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)

#Metodo Modifica Docente
def modificarDocente(idDocente):
    Nombre = input("Ingrese el nuevo nombre del Docente:\n")
    Dni = input(f"Ingrese el nuevo DNI del Docente {Nombre}:\n")
    Correo = input(f"Ingrese el nuevo correo del Docente {Nombre}:\n")
    FechaNac = input(f"Ingrese la nueva fecha de nacimiento del Docente {Nombre}:\n")
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    consulta = query.ModificarDocente(Nombre, Dni, Correo, FechaNac, idDocente)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
       print("Se modifico correctamente")
    else:
       print("No fue posible modificar al Docente")
       input("Desea continuar")

#Metodo Elimina Docente
def eliminaDocente(idDocente):
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    connsulta = query.EliminarDocente(str(idDocente))
    resconn = conn.ejecutarBDD(connsulta)
    if resconn:
        print(f"Se elimino Docente {idDocente}")
    else:
        print("Fallaste")
        print("No fue posible eliminar al Docente")
    input("Desea continuar")
####FIN METODOS DOCENTE####