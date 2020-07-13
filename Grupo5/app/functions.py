from conn import Conexion
from classes import Periodos
# Funciones mantenimiento Periodos
def crearPeriodos():
    try: 
        periodos = int(insert('Ingrese el numero de periodos que tendra el año escolar: '))
        for i in range(periodos):        
            conn = Conexion('mongodb://localhost:27017','Hackathon7_Team5')
            periodo = Periodos(i+1, f'Periodo {i+1}', '')
            conn.insertar_registro('Periodos', {
                'id': periodo.id,
                'nombre': periodo.nombre,
                'descripcion': periodo.descripcion,
            })
    except:
        print("Error!: Ingrese un número entero positivo")