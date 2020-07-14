import conexion
import querys

#Empleado -- Alumno
def ingresarAlumno():
    nombre = input("Ingrese Nombre del Alumno:\n")
    apellido = input("Ingrese Nombre del Alumno:\n")
    correo = input("Ingrese Nombre del Alumno:\n")
    fechanac = input("Ingrese Nombre del Alumno:\n")
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    consulta = query.InsertAlumno(nombre, apellido, correo, fechanac)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print("Añadido")
    else:
        print("Fallaste")
    input("Desea continuar")