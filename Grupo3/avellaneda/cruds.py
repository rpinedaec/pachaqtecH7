import conexion
import querys
from time import sleep
import alumnos
import periodoEscolar
import matricula
import docentes
import cursos
import salones
import DocenteCurso
import AlumnoCurso
import notas

conn = conexion.conexionBDD(4)
query = querys.Querys()



#  █████  ██      ██    ██ ███    ███ ███    ██  ██████  
# ██   ██ ██      ██    ██ ████  ████ ████   ██ ██    ██ 
# ███████ ██      ██    ██ ██ ████ ██ ██ ██  ██ ██    ██ 
# ██   ██ ██      ██    ██ ██  ██  ██ ██  ██ ██ ██    ██ 
# ██   ██ ███████  ██████  ██      ██ ██   ████  ██████ 

#Ingresar Alumno
def ingresarAlumno():
    #Datos del alumno
    idAlumno = input("Ingrese id del Alumno:\n")
    nombre = input("Ingrese Nombre del Alumno:\n")
    apellido = input(f"Ingrese Apellido del Alumno {nombre}:\n")
    correo = input(f"Ingrese Correo del Alumno {nombre}:\n")
    fechanac = input(f"Ingrese Fecha de Nacimiento del Alumno {nombre}:\n")
    nuevoAlumno = alumnos.alumnos(idAlumno, nombre, apellido, correo, fechanac)
    resConn = conn.insertarRegistro("Alumno",nuevoAlumno.toDic())
    """try:
        consulta = query.InsertAlumno(nombre, apellido, correo, fechanac)
        resconn = conn.ejecutarBDD(consulta)
        if resconn:
            print("Se agrego correctamente")
        else:
            print("No fue posible agregar al alumno")
        input("Desea continuar")
    except ValueError as e:
        print(e)"""
    
#Listar Alumno
def listarAlumnos():
    dic = {}
    resConn = conn.leerRegistros("Alumno", dic)
    for row in resConn:
        print(f"{str(row['idAlumno'])}\t{str(row['nombrealumno'])}\t{str(row['apellidoalumno'])}\t{str(row['correoalumno'])}\t{str(row['nacalumno'])}")
    """consulta = query.ListarAllAlumno()
    resconn = conn.consultarBDD(consulta)
    for tplAlumno in resconn:
        print(tplAlumno[0], tplAlumno[1], tplAlumno[2], tplAlumno[3], tplAlumno[4])"""

#Buscar Alumno
def buscarAlumno():
    try:
        idAlumno = input("Ingrese el id del alumno que desea buscar:\n")
        query = {'idAlumno' : idAlumno}
        print(query)
        resConn = conn.leerRegistro("Alumno", query)
        a = alumnos.alumnos(resConn['idAlumno'], resConn['nombrealumno'], resConn['apellidoalumno'], resConn['correoalumno'], resConn['nacalumno'])
        return a.toDic()
        """consulta = query.BuscarAlumno(idAlumno)
        resconn = conn.consultarBDD(consulta)
        for tplAlumno in resconn:
            print(tplAlumno[0], tplAlumno[1], tplAlumno[2], tplAlumno[3], tplAlumno[4])
        return idAlumno"""
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)

#Modificar Alumno   
def modificarAlumno(dicAlumno):
    query = dicAlumno
    idAlumno = input("Ingrese nuevo id del alumno:\n")
    Nombre = input("Ingrese el nuevo nombre del alumno:\n")
    Apellido = input(f"Ingrese el nuevo apellido del alumno {Nombre}:\n")
    Correo = input(f"Ingrese el nuevo correo del alumno {Nombre}:\n")
    FechaNac = input(f"Ingrese la nueva fecha de nacimiento del alumno {Nombre}:\n")
    """consulta = query.ModificarAlumno(Nombre, Apellido, Correo, FechaNac, idAlumno)
    resconn = conn.ejecutarBDD(consulta)"""
    modiAlumno = alumnos.alumnos(idAlumno, Nombre, Apellido, Correo, FechaNac)
    resconn = conn.actualizarRegistro("Alumno", query, modiAlumno.toDic())
    if resconn:
        print("Se modifico correctamente")
    else:
        print("No fue posible modificar al alumno")
    input("Desea continuar")

#Eliminar Alumno
def eliminarAlumno(dicAlumno):
    """consulta = query.EliminarAlumno(idAlumno)
    resconn = conn.ejecutarBDD(consulta)"""
    query = dicAlumno
    resconn = conn.eliminarRegistro("Alumno", query)
    if resconn:
        print("Se elimino al alumno seleccionado")
    else:
        print("No fue posible eliminar al alumno")
    input("Desea continuar")



# ██████   ██████   ██████ ███████ ███    ██ ████████ ███████ ███████ 
# ██   ██ ██    ██ ██      ██      ████   ██    ██    ██      ██      
# ██   ██ ██    ██ ██      █████   ██ ██  ██    ██    █████   ███████ 
# ██   ██ ██    ██ ██      ██      ██  ██ ██    ██    ██           ██ 
# ██████   ██████   ██████ ███████ ██   ████    ██    ███████ ███████ 


#Ingresar Docente
def ingresarDocente():
    #Datos del docente
    idDocente = input("Ingresar Id del Docente:\n")
    nombre = input("Ingrese Nombre del Docente:\n")
    dni = input(f"Ingrese Dni del Docente {nombre}:\n")
    correo = input(f"Ingrese Correo del Docente {nombre}:\n")
    fechanac = input(f"Ingrese Fecha de Nacimiento del Docente {nombre}:\n")
    try:
        """consulta = query.InsertDocente(nombre, dni, correo, fechanac)
        resconn = conn.ejecutarBDD(consulta)"""
        nuevoDocente = docentes.docentes(idDocente, nombre, dni, correo, fechanac)
        resconn = conn.insertarRegistro("Docente", nuevoDocente.toDic())
        if resconn:
            print("Se agrego correctamente")
        else:
            print("No fue posible agregar al docente")
        input("Desea continuar")
    except ValueError as e:
        print(e)
    
#Listar Docente
def listarDocente():
    """consulta = query.ListarAllDocente()
    resconn = conn.consultarBDD(consulta)"""
    query = {}
    resconn = conn.leerRegistros("Docente", query)
    for tplDocente in resconn:
        print(tplDocente['iddocentes'], tplDocente['nombredocente'], tplDocente['dnidocente'], tplDocente['correodocente'], tplDocente['nacdocente'])

#Buscar Docente
def buscarDocente():
    try:
        idDocente = input("Ingrese el id del docente que desea buscar:\n")
        """consulta = query.BuscarDocente(idDocente)
        resconn = conn.consultarBDD(consulta)"""
        query = {'iddocentes' : idDocente}
        resconn = conn.leerRegistros("Docente", query)
        for tplDocente in resconn:
            print(tplDocente['iddocentes'], tplDocente['nombredocente'], tplDocente['dnidocente'], tplDocente['correodocente'], tplDocente['nacdocente'])
        d = docentes.docentes(tplDocente['iddocentes'], tplDocente['nombredocente'], tplDocente['dnidocente'], tplDocente['correodocente'], tplDocente['nacdocente'])
        return d.toDic()
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)

#Modificar Docente  
def modificarDocente(idDocente):
    IdDocente = input("Ingresar el nuevo id del docente:\n")
    Nombre = input("Ingrese el nuevo nombre del docente:\n")
    Dni = input(f"Ingrese el nuevo Dni del docente {Nombre}:\n")
    Correo = input(f"Ingrese el nuevo correo del docente {Nombre}:\n")
    FechaNac = input(f"Ingrese la nueva fecha de nacimiento del docente {Nombre}:\n")
    """consulta = query.ModificarDocente(Nombre, Dni, Correo, FechaNac, idDocente)
    resconn = conn.ejecutarBDD(consulta)"""
    modiDocente = docentes.docentes(IdDocente, Nombre, Dni, Correo, FechaNac)
    resconn = conn.actualizarRegistro("Docente", idDocente, modiDocente.toDic())
    if resconn:
        print("Se modifico correctamente")
    else:
        print("No fue posible modificar al alumno")
    input("Desea continuar")

#Eliminar Docente
def eliminarDocente(idDocente):
    """consulta = query.EliminarDocente(idDocente)
    resconn = conn.ejecutarBDD(consulta)"""
    resconn = conn.eliminarRegistro("Docente", idDocente)
    if resconn:
        print("Se elimino al docente seleccionado")
    else:
        print("No fue posible eliminar al docente")
    input("Desea continuar")



# ███████  █████  ██       ██████   ██████  ███    ██ ███████ ███████ 
# ██      ██   ██ ██      ██    ██ ██    ██ ████   ██ ██      ██      
# ███████ ███████ ██      ██    ██ ██    ██ ██ ██  ██ █████   ███████ 
#      ██ ██   ██ ██      ██    ██ ██    ██ ██  ██ ██ ██           ██ 
# ███████ ██   ██ ███████  ██████   ██████  ██   ████ ███████ ███████


#Ingresar Salon
def ingresarSalon():
    #Datos del Salon
    idSalon = input("Ingrese id del Salon:\n")
    nombre = input("Ingrese Nombre del Salon:\n")
    try:
        """consulta = query.InsertSalon(nombre)
        resconn = conn.ejecutarBDD(consulta)"""
        nuevoSalon = salones.salones(idSalon, nombre)
        resconn = conn.insertarRegistro("Salon", nuevoSalon.toDic())
        if resconn:
            print("Se agrego correctamente")
        else:
            print("No fue posible agregar al salon")
        input("Desea continuar")
    except ValueError as e:
        print(e)
    
#Listar Salones
def listarSalon():
    """consulta = query.ListarAllSalones()
    resconn = conn.consultarBDD(consulta)"""
    query = {}
    resconn = conn.leerRegistros("Salon", query)
    for tplSalon in resconn:
        print(tplSalon['idsalones'], tplSalon['nombresalon'])

#Buscar Salon
def buscarSalon():
    try:
        idSalon = input("Ingrese el id del salon que desea buscar:\n")
        """consulta = query.BuscarSalon(idSalon)
        resconn = conn.consultarBDD(consulta)"""
        query = {'idsalones' : idSalon}
        resconn = conn.leerRegistros("Salon", query)   
        for tplSalon in resconn:
            print(tplSalon['idsalones'], tplSalon['nombresalon'])
        s = salones.salones(tplSalon['idsalones'], tplSalon['nombresalon'])
        return s.toDic()
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)

#Modificar Salon   
def modificarSalon(dicSalon):
    idSalon = input("Ingrese el nuevo id del salon:\n")
    Nombre = input("Ingrese el nuevo nombre del salon:\n")
    """consulta = query.ModificarSalon(Nombre, idSalon)
    resconn = conn.ejecutarBDD(consulta)"""
    modiSalon = salones.salones(idSalon, Nombre)
    resconn = conn.actualizarRegistro("Salon", dicSalon, modiSalon.toDic())
    if resconn:
        print("Se modifico correctamente")
    else:
        print("No fue posible modificar el Salon")
    input("Desea continuar")

#Eliminar Salon
def eliminarSalon(idSalon):
    """consulta = query.EliminarSalon(idSalon)
    resconn = conn.ejecutarBDD(consulta)"""
    resconn = conn.eliminarRegistro("Salon", idSalon)
    if resconn:
        print("Se elimino al salon selecciondo")
    else:
        print("No fue posible eliminar al salon")
    input("Desea continuar")



#  ██████ ██    ██ ██████  ███████  ██████  ███████ 
# ██      ██    ██ ██   ██ ██      ██    ██ ██      
# ██      ██    ██ ██████  ███████ ██    ██ ███████ 
# ██      ██    ██ ██   ██      ██ ██    ██      ██ 
#  ██████  ██████  ██   ██ ███████  ██████  ███████


#Ingresar Curso
def ingresarCurso():
    #Datos del Curso
    idCurso = input("Ingrese id del Curso:\n")
    nombre = input("Ingrese Nombre del Curso:\n")
    try:
        """consulta = query.InsertCurso(nombre)
        resconn = conn.ejecutarBDD(consulta)"""
        nuevoCurso = cursos.cursos(idCurso, nombre)
        resconn = conn.insertarRegistro("Curso", nuevoCurso.toDic())
        if resconn:
            print("Se agrego correctamente")
        else:
            print("No fue posible agregar curso")
        input("Desea continuar")
    except ValueError as e:
        print(e)
    
#Listar Cursos
def listarCurso():
    """consulta = query.ListarAllCursos()
    resconn = conn.consultarBDD(consulta)"""
    query = {}
    resconn = conn.leerRegistros("Curso", query)
    for tplCurso in resconn:
        print(tplCurso['idcursos'], tplCurso['nombrecurso'])

#Buscar Curso
def buscarCurso():
    try:
        idCurso = input("Ingrese el id del curso que desea buscar:\n")
        """consulta = query.BuscarCurso(idCurso)
        resconn = conn.consultarBDD(consulta)"""
        query = {'idcursos' : idCurso}
        resconn = conn.leerRegistros("Curso", query)
        for tplCurso in resconn:
            print(tplCurso['idcursos'], tplCurso['nombrecurso'])
        c = cursos.cursos(tplCurso['idcursos'], tplCurso['nombrecurso'])
        return c.toDic()
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)

#Modificar Curso   
def modificarCurso(dicCurso):
    idCurso = input("Ingresar el nuevo id del curso:\n")
    Nombre = input("Ingrese el nuevo nombre del curso:\n")
    """consulta = query.ModificarCurso(Nombre, idCurso)
    resconn = conn.ejecutarBDD(consulta)"""
    modiCurso = cursos.cursos(idCurso, Nombre)
    resconn = conn.actualizarRegistro("Curso", dicCurso, modiCurso.toDic())
    if resconn:
        print("Se modifico correctamente")
    else:
        print("No fue posible modificar el curso")
    input("Desea continuar")

#Eliminar Curso
def eliminarCurso(idCurso):
    """consulta = query.EliminarCurso(idCurso)
    resconn = conn.ejecutarBDD(consulta)"""
    resconn = conn.eliminarRegistro("Curso", idCurso)
    if resconn:
        print("Se elimino el curso seleccionado")
    else:
        print("No fue posible eliminar el curso")
    input("Desea continuar")



# ██████  ███████ ██████  ██  ██████  ██████   ██████      ███████ ███████  ██████  ██████  ██       █████  ██████  
# ██   ██ ██      ██   ██ ██ ██    ██ ██   ██ ██    ██     ██      ██      ██      ██    ██ ██      ██   ██ ██   ██ 
# ██████  █████   ██████  ██ ██    ██ ██   ██ ██    ██     █████   ███████ ██      ██    ██ ██      ███████ ██████  
# ██      ██      ██   ██ ██ ██    ██ ██   ██ ██    ██     ██           ██ ██      ██    ██ ██      ██   ██ ██   ██ 
# ██      ███████ ██   ██ ██  ██████  ██████   ██████      ███████ ███████  ██████  ██████  ███████ ██   ██ ██   ██ 


#Ingresar Periodo
def ingresarPeriodo():
    #Datos del Periodo
    idPeriodo = input("Ingrese id del Periodo:\n")
    nombre = input("Ingrese Nombre del Periodo:\n")
    try:
        """consulta = query.InsertPeriodo(nombre)
        resconn = conn.ejecutarBDD(consulta)"""
        nuevoPeriodo = periodoEscolar.periodoEscolar(idPeriodo, nombre)
        resconn = conn.insertarRegistro("Periodo Escolar", nuevoPeriodo.toDic())
        if resconn:
            print("Se agrego correctamente")
        else:
            print("No fue posible agregar el periodo escolar")
        input("Desea continuar")
    except ValueError as e:
        print(e)
    
#Listar Periodos
def listarPeriodo():
    """consulta = query.ListarAllPeriodos()
    resconn = conn.consultarBDD(consulta)"""
    query = {}
    resconn = conn.leerRegistros("Periodo Escolar", query)
    for tplPeriodo in resconn:
        print(tplPeriodo['idperiodoEscolar'], tplPeriodo['desperiodo'])

#Buscar Periodo
def buscarPeriodo():
    try:
        idPeriodo = input("Ingrese el id del periodo que desea buscar:\n")
        """consulta = query.BuscarPeriodo(idPeriodo)
        resconn = conn.consultarBDD(consulta)"""
        query = {'idperiodoEscolar' : idPeriodo}
        resconn = conn.leerRegistro("Periodo Escolar", query)
        print(resconn['idperiodoEscolar'], resconn['desperiodo'])
        pe = periodoEscolar.periodoEscolar(resconn['idperiodoEscolar'], resconn['desperiodo'])
        return pe.toDic()
        """for tplPeriodo in resconn:
            print(tplPeriodo[0], tplPeriodo[1])
        return idPeriodo"""
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)

#Modificar Periodo   
def modificarPeriodo(idPeriodo):
    Nombre = input("Ingrese el nuevo nombre del periodo escolar:\n")
    consulta = query.ModificarPeriodo(Nombre, idPeriodo)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print("Se modifico correctamente")
    else:
        print("No fue posible modificar el periodo")
    input("Desea continuar")

#Eliminar Periodo
def eliminarPeriodo(idPeriodo):
    consulta = query.EliminarPeriodo(idPeriodo)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print(f"Se elimino el periodo {idPeriodo}")
    else:
        print("No fue posible eliminar el periodo")
    input("Desea continuar")



# ███    ██  ██████  ████████  █████  ███████ 
# ████   ██ ██    ██    ██    ██   ██ ██      
# ██ ██  ██ ██    ██    ██    ███████ ███████ 
# ██  ██ ██ ██    ██    ██    ██   ██      ██ 
# ██   ████  ██████     ██    ██   ██ ███████ 


#Ingresar Nota
def ingresarNota():
    #Datos de la nota
    nombre = input("Ingrese Nota del Curso:\n")
    try:
        consulta = query.InsertNota(nombre)
        resconn = conn.ejecutarBDD(consulta)
        if resconn:
            print("Se agrego correctamente")
        else:
            print("No fue posible agregar la nota al curso")
        input("Desea continuar")
    except ValueError as e:
        print(e)
    
#Listar Notas
# def listarNota():
#     consulta = query.ListarAllNotas()
#     resconn = conn.consultarBDD(consulta)
#     for tplNota in resconn:
#         print(tplNota[0])

#Buscar Nota
def buscarNota():
    try:
        idNota = int(input("Ingrese la nota del curso que desea buscar:\n"))
        consulta = query.BuscarNota(idNota)
        resconn = conn.consultarBDD(consulta)
        for tplNota in resconn:
            print(tplNota[0])
        return idNota
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)

#Modificar Nota   
def modificarNota(Nota):
    Nombre = input("Ingrese la nueva nota del curso:\n")
    consulta = query.ModificarNota(Nombre, Nota)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print("Se modifico correctamente")
    else:
        print("No fue posible modificar la nota")
    input("Desea continuar")

#Eliminar Nota
def eliminarNota(Nota):
    consulta = query.EliminarNota(Nota)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print(f"Se elimino la nota {Nota}")
    else:
        print("No fue posible eliminar la nota")
    input("Desea continuar")

#Matricula
def ingresarMatricula():
    #Datos alumno
    listarAlumnos()
    IdAlumno = buscarAlumno()
    #Datos Periodo
    listarPeriodo()
    IdPeriodo = buscarPeriodo()
    #Id Matricula
    IdMatricula = input("Ingrese id de matricula:\n")
    try:
        """consulta = query.InsertMatricula(IdAlumno, IdPeriodo)
        resconn = conn.ejecutarBDD(consulta)"""
        nuevaMatricula = matricula.matricula(IdMatricula, IdAlumno, IdPeriodo)
        resconn = conn.insertarRegistro("Matricula", nuevaMatricula.toDic())
        if resconn:
            print("Se agrego correctamente")
        else:
            print("No fue posible agregar la matricula")
        input("Desea continuar")
    except Exception as e:
        print(e)

def listarMatricula():
    try:
        """consulta = query.ListarAllMatricula()
        resconn = conn.consultarBDD(consulta)   """
        query = {}
        resconn = conn.leerRegistros("Matricula", query)
        for tplMatricula in resconn:
            print(tplMatricula['idmatricula'], tplMatricula['alumno'], tplMatricula['periodo'])
        sleep(2)
    except Exception as e:
        print(e)

def buscarMatricula():
    try:
        idMatricula = input("Ingrese id de matricula:\n")
        """consulta = query.BuscarMatricula(idMatricula)
        resconn = conn.consultarBDD(consulta)  """ 
        query = {'idmatricula' : idMatricula}
        resconn = conn.leerRegistros("Matricula", query)
        for tplMatricula in resconn:
            print(tplMatricula['idmatricula'], tplMatricula['alumno'], tplMatricula['periodo'])
        m = matricula.matricula(tplMatricula['idmatricula'], tplMatricula['alumno'], tplMatricula['periodo'])
        return idMatricula
    except Exception as e:
        print(e)

#██████   ██████   ██████ ███████ ███    ██ ████████ ███████      ██████ ██    ██ ██████  ███████  ██████  
#██   ██ ██    ██ ██      ██      ████   ██    ██    ██          ██      ██    ██ ██   ██ ██      ██    ██ 
#██   ██ ██    ██ ██      █████   ██ ██  ██    ██    █████       ██      ██    ██ ██████  ███████ ██    ██ 
#██   ██ ██    ██ ██      ██      ██  ██ ██    ██    ██          ██      ██    ██ ██   ██      ██ ██    ██ 
#██████   ██████   ██████ ███████ ██   ████    ██    ███████      ██████  ██████  ██   ██ ███████  ██████  

def docenteCurso():
    #Datos docente
    listarDocente()
    IdDocente = buscarDocente()
    #Datos Curso
    listarCurso()
    IdCurso = buscarCurso()
    #Datos Salon
    listarSalon()
    IdSalon = buscarSalon()
    IdDocenteCurso = input("Ingresar id:\n")
    try:
        """consulta = query.InsertDocenteCurso(IdDocente, IdCurso, IdSalon)
        resconn = conn.ejecutarBDD(consulta)"""
        nuevoDocenteCurso = DocenteCurso.docenteCurso(IdDocenteCurso, IdDocente, IdCurso, IdSalon)
        resconn = conn.insertarRegistro("Asigacion Docente Curso", nuevoDocenteCurso.toDic())
        if resconn:
            print("Se agrego correctamente")
        else:
            print("No fue posible asignar al docente")
        input("Desea continuar")
    except Exception as e:
        print(e)


def listarDocenteCurso():
    try:
        """consulta = query.ListarDocenteCurso()
        resconn = conn.consultarBDD(consulta)""" 
        query = {}
        resconn = conn.leerRegistros("Asigacion Docente Curso", query)  
        for tplDocenteCurso in resconn:
            print(tplDocenteCurso['IdAlumnoCurso'], tplDocenteCurso['Matricula'], tplDocenteCurso['Curso'])
        sleep(2)
    except Exception as e:
        print(e)

def buscarDocenteCurso():
    try:
        IdDocenteCurso = input("Ingrese id del docente para detalle:\n")
        """consulta = query.BuscarDocenteCurso(IdDocenteCurso)
        resconn = conn.consultarBDD(consulta)"""   
        query = {'IdDocenteCurso' : IdDocenteCurso}
        resconn = conn.leerRegistros("Asigacion Docente Curso", query)
        for tplDocenteCurso in resconn:
            print(tplDocenteCurso['IdAlumnoCurso'], tplDocenteCurso['Matricula'], tplDocenteCurso['Curso'])
        sleep(2)
    except Exception as e:
        print(e)


# █████  ██      ██    ██ ███    ███ ███    ██  ██████       ██████ ██    ██ ██████  ███████  ██████  
#██   ██ ██      ██    ██ ████  ████ ████   ██ ██    ██     ██      ██    ██ ██   ██ ██      ██    ██ 
#███████ ██      ██    ██ ██ ████ ██ ██ ██  ██ ██    ██     ██      ██    ██ ██████  ███████ ██    ██ 
#██   ██ ██      ██    ██ ██  ██  ██ ██  ██ ██ ██    ██     ██      ██    ██ ██   ██      ██ ██    ██ 
#██   ██ ███████  ██████  ██      ██ ██   ████  ██████       ██████  ██████  ██   ██ ███████  ██████  

def alumnoCurso():
    #Datos alumno matriculado
    listarMatricula()
    IdMatricula = buscarMatricula()
    #Datos Cursos
    listarCurso()
    IdCurso = buscarCurso()
    IdAlumnoCurso = input("Ingresar id:\n")
    try:
        """consulta = query.InsertAlumnoCurso(IdMatricula, IdCurso)
        resconn = conn.ejecutarBDD(consulta)"""
        nuevoAlumnoCurso = AlumnoCurso.alumnoCurso(IdAlumnoCurso, IdMatricula, IdCurso)
        resconn = conn.insertarRegistro("Asignacion Alumno Curso", nuevoAlumnoCurso.toDic())
        if resconn:
            print("Se agrego correctamente")
        else:
            print("No fue posible asignar al alumno")
        input("Desea continuar")
    except Exception as e:
        print(e)

def listarAlumnoCurso():
    try:
        """consulta = query.ListarAllAlumnoCurso()
        resconn = conn.consultarBDD(consulta)"""
        query = {}
        resconn = conn.leerRegistros("Asignacion Alumno Curso", query)
        for tplAlumCurso in resconn:
            print(tplAlumCurso['IdAlumnoCurso'], tplAlumCurso['Matricula'], tplAlumCurso['Curso'])
        sleep(2)
    except Exception as e:
        print(e)

def buscarAsignarNotas():
    IdCursoMatricula = input("Ingresar id del cual desea asignar la nota:\n")    
    try:
        consulta = query.BuscarAlumnoCursoNota(IdCursoMatricula)
        resconn = conn.consultarBDD(consulta)
        for tplAlumCurso in resconn:
            print(tplAlumCurso[0], tplAlumCurso[1], tplAlumCurso[2], tplAlumCurso[3], tplAlumCurso[4], tplAlumCurso[5], tplAlumCurso[6])
        sleep(2)
        return IdCursoMatricula
    except Exception as e:
        print(e)

def asignarNota(IdNota):    
    Nota = input("Ingrese la Nota:\n")
    try:
        consulta = query.AsignarNota(Nota, IdNota)
        resconn = conn.ejecutarBDD(consulta)
        if resconn:
            print("Se agrego correctamente")
        else:
            print("No fue posible asignar al alumno")
        input("Desea continuar")
    except Exception as e:
        print(e)

def listarNota():
    try:
        query = {}
        resconn = conn.leerRegistros("Listar Notas", query)
        for tplAlumCurso in resconn:
            print(tplAlumCurso['IdAlumnoCurso'], tplAlumCurso['Matricula'], tplAlumCurso['Curso'])
        sleep(2)
    except Exception as e:
        print(e)