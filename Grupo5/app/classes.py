import os

class Menu:
    def __init__(self, lstOpciones, strTitulo, strMenuDescr):
        self.lstOpciones = lstOpciones
        self.strTitulo = strTitulo
        self.strMenuDescr = strMenuDescr
        self.OptionSelect = 0
    def show(self):
        os.system("cls")
        print(f"\033[1;32;40m")
        print(20*":" + f"{self.strTitulo:^30}" + 20*":")
        print(20*":" + f"{self.strMenuDescr:^30}" + 20*":")
        for k, v in self.lstOpciones.items():
            print(k, "::", v)
        print("9 :: Salir")
        while True:
            try:
                self.OptionSelect = int(input("Ingrese su opción: "))
                if self.OptionSelect > 0 and self.OptionSelect < len(self.lstOpciones)+1:
                    return self.OptionSelect
                elif self.OptionSelect == 9:
                    break
                else:
                    print("Ingrese alguna de las opciones mostradas")
            except ValueError:
                print("Ingresa un número entero")
                
class Periodos:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

class Salon:
    def __init__(self, cod_salon, desc, cod_grado):
        self.cod_salon = cod_salon
        self.desc = desc
        self.cod_grado = cod_grado

class Periodo:
    def __init__(self, cod_periodo, desc):
        self.cod_periodo = cod_periodo
        self.desc = desc
        
class Grados:
    def __init__(self, cod_grado, desc):
        self.cod_grado = cod_grado
        self.desc = desc

class Cursos:
    def __init__(self, cod_curso, nombre, cod_grado, numero_notas):
        self.cod_curso = cod_curso
        self.nombre = nombre
        self.cod_grado = cod_grado
        self.numero_notas = numero_notas

class Notas:
    def __init__(self, cod_matricula, cod_curso, nota):
        self.cod_matricula = cod_matricula
        self.cod_curso = cod_curso
        self.nota = nota

