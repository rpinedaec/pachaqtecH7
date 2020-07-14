import os
from time import sleep

class Menu:
    
    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones

    def mostrarMenu(self):
        self.limpiarPantalla()
        opSalir = True
        while(opSalir):
            self.limpiarPantalla()
            print("             COLEGIO E-SCHOOL                 ")
            print(" ----------------" +self.nombreMenu + "----------------")
            
            for (key, value) in self.listaOpciones.items():
                print(key, "\t: ", value)
            opcion = 100
            print("\t- Salir \t\t::  9")
            try:
                print("Escoge tu opcion")
                opcion = int(input())
            except ValueError as error:
                print("Opcion invalida deben ser numeros del 0 al 2")
            contOpciones = 0
            for (key, value) in self.listaOpciones.items():
                if(opcion == int(value) or opcion == 9):
                   contOpciones += 1
            if(contOpciones == 0):
                print("Escoge una opcion valida")
                sleep(1)
            else:
                opSalir = False

        return opcion

    def limpiarPantalla(self):
        def clear():
            return os.system('clear')
        clear()
    
