
import logging

#Create and configure logger
logging.basicConfig(
                    filename="Logging_colegio.log",
                    level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s'
                    )



def validarEntero(mensaje):
    booleanCampo = True
    entrada=0
    while booleanCampo:
        entrada = input(mensaje)
        try:
            entrada = int(entrada)
            booleanCampo=False
        except ValueError:
            print("La entrada es incorrecta: escribe un numero entero")
    return entrada


def validarFloat(mensaje):
    booleanCampo = True
    entrada=0.0
    while booleanCampo:
        entrada = input(mensaje)
        try:
            entrada = float(entrada)
            booleanCampo=False
        except ValueError:
            print("La entrada es incorrecta: escribe un numero entero o con decimal")
    return entrada



def listaSimple(lstObjeto, opcionMenuPrincipal, alertaDetener): 
    strTitulo = "  "
    strTituloGuion = "  "
    intContador = 0
    strTexto = ""
    # Opcion 1 ALUMNO
    if opcionMenuPrincipal=="alumno": 
        for p in lstObjeto:
            intContador+=1
            strTexto += "  "  
            #strTexto += str(p.idAlumno).ljust(10)+"\t\t" 
            strTexto += str(p.dniAlumno).ljust(10)+"\t\t" 
            strTexto += str(p.nombreAlumno).ljust(10)+"\t\t" 
            strTexto += str(p.apellidoAlumno).ljust(10)+"\t\t" 
            strTexto += str(p.direccionAlumno).ljust(10)+"\n" 
        if intContador>0:
            #strTitulo += str("CODIGO").ljust(10)+"\t\t\t\t"
            strTitulo += str("DNI").ljust(10)+"\t\t"
            strTitulo += str("NOMBRE").ljust(10)+"\t\t"
            strTitulo += str("APELLIDO").ljust(10)+"\t\t"
            strTitulo += str("DIRECCION").ljust(10)+"\t\t"
            strTituloGuion += "----------\t\t\t\t----------\t\t----------\t\t----------"
            strTexto += "\n----------------------------------------------------"
        else:
            strTitulo +="Sin datos..."
    # Opcion 2 NOTA
    if opcionMenuPrincipal=="nota": 
        for p in lstObjeto:
            intContador+=1
            strTexto += "  "  
            #strTexto += str(p.idNota).ljust(10)+"\t\t" 
            strTexto += str(p.descripcionNota).ljust(10)+"\t\t" 
            strTexto += str(p.idCurso).ljust(10)+"\t\t"
            strTexto += str(p.idAlumno).ljust(10)+"\n" 
        if intContador>0:
            #strTitulo += str("CODIGO").ljust(10)+"\t\t\t\t"
            strTitulo += str("NOTA").ljust(10)+"\t\t"
            strTitulo += str("CURSO").ljust(10)+"\t\t"
            strTitulo += str("ALUMNO").ljust(10)
            strTituloGuion += "----------\t\t----------\t\t----------"
            strTexto += "\n----------------------------------------------------"
        else:
            strTitulo +="Sin datos..."
    # notaDescriptiva
    if opcionMenuPrincipal=="notaDescriptiva": 
        for p in lstObjeto:
            intContador+=1
            strTexto += str(intContador)+")  "  
            #strTexto += str(p.idNota).ljust(10)+"\t\t" 
            strTexto += str(p.descripcionNota).ljust(10)+"\t\t" 
            strTexto += str(p.idCurso).ljust(10)+"\t\t"
            strTexto += str(p.idAlumno).ljust(10)+"\n" 
        if intContador>0:
            #strTitulo += str("CODIGO").ljust(10)+"\t\t\t\t"
            strTitulo += str("NOTA").ljust(10)+"\t\t"
            strTitulo += str("CURSO").ljust(10)+"\t\t"
            strTitulo += str("ALUMNO").ljust(10)
            strTituloGuion += "----------\t\t----------\t\t----------"
            strTexto += "\n----------------------------------------------------"
        else:
            strTitulo +="Sin datos..."
    # Opcion 3 CURSO
    if opcionMenuPrincipal=="curso": 
        for p in lstObjeto:
            intContador+=1
            strTexto += str(intContador)+")  "  
            #strTexto += str(p.idcurso).ljust(10)+"\t\t"  
            strTexto += str(p.cursoNombre).ljust(10)+"\t\t"  
            strTexto += str(p.anio_academico).ljust(10)+"\n"
        if intContador>0:
            #strTitulo += str("CODIGO").ljust(10)+"\t\t\t\t" 
            strTitulo += str("CURSO").ljust(10)+"\t\t" 
            strTitulo += str("AÑO ESCOLAR").ljust(10)
            strTituloGuion += "----------\t\t\t\t----------"
            strTexto += "\n----------------------------------------------------"
        else:
            strTitulo +="Sin datos..."
    print(strTitulo)
    print(strTituloGuion)
    print(strTexto)
    if alertaDetener ==1:
        input("Enter para continuar...")
    else:
        pass




# Validar que no exista el dni del Alumno en la listaGeneral, mensaje="9999 Cancelar / Dato: "
def validarNoExitaDniAlumnoEnLista(ListaGeneral, mensaje):
    strRetornar = "" 
    boolValor = True
    while boolValor:
        strNombreIngresado=validarEntero(mensaje)
        if(strNombreIngresado==9999):
            boolValor = False
            strRetornar = 9999
            break
        else:
            ValorTemporal = 0
            for p in ListaGeneral:
                if(str(p.dniAlumno)==str(strNombreIngresado)):
                    ValorTemporal+=1
            if(ValorTemporal==0):
                strRetornar=strNombreIngresado
                boolValor=False
            else:                
                print("Valor existente.")
    return strRetornar


# Validar DNI de Alumnos en listaGeneral[], mensaje="9999 Cancelar / Dato: "
def validarDniAlumnoEnLista(ListaGeneral, mensaje):
    strRetornar = "" 
    boolValor = True
    while boolValor:
        strNombreIngresado=validarEntero(mensaje)
        if(strNombreIngresado==9999):
            boolValor = False
            strRetornar = 9999
            break
        else:
            ValorTemporal = 0
            for p in ListaGeneral:
                if(str(p.dniAlumno)==str(strNombreIngresado)):
                    ValorTemporal+=1
            if(ValorTemporal>0):
                strRetornar=strNombreIngresado
                boolValor=False
            else:                
                print("Valor no existente.")
    return strRetornar




