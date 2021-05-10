from Manejador import claseManejador
import re
class claseMenu:
    __manejador = None
    def __init__(self, manejador = claseManejador()):
        self.__manejador = manejador
    def menu(self, op):
        if(op == 1):    #Listar por año y división
            print('----OPCIÓN----')
            ano = str(input('Año: '))
            div = str(input('División (Manana o Tarde): '))
            if(re.match('^[a-z1-9]{1,20}$', ano.lower())):
                if(re.match('^[a-z]{1,7}$', div.lower())):
                    self.__manejador.obtAlum(ano, div)
                    self.__manejador.mostrarLista()
                else: print('ERROR: división inválido')
            else: print('ERROR: año inválido')
            input()
            self.__manejador.clear()
        elif(op == 2):  #modificar la cantidad máxima de inasistencias
            max = int(input('Nueva cantidad máxima de faltas: '))
            if(max > 0):
                self.__manejador.mod(max)
            else: print('ERROR: cantidad máxima de inasistencias inválida')
            input()
        elif(op == 3):
            print('DATO: finalizando...')
        else: print('ERROR: opción inválida')