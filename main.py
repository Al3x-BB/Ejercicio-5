from Alumno import claseAlumno
from Manejador import claseManejador
from Menu import claseMenu
import os
def test():
    nom = str(input('Nombre: '))
    ano = str(input('Año: '))
    div = str(input('División: '))
    ina = int(input('Cantidad de inasistencias: '))
    unAlumno = claseAlumno(nom, ano, div, ina, 12, 7)
    print('Alumno: {} - {}'.format(unAlumno.getNom(), unAlumno.getIna()))
if __name__ == '__main__':
    if(str(input('¿Testear? ')).lower() == 'si'):
        test()
    else:
        #variables
        band = False
        manejador = claseManejador()
        menu = claseMenu()
        #inicializar variables
        manejador.crearLista()
        #acciones
        while not band:
            print('----MENU----\n1. Ingresar año y división\n2. Modificar cantidad máxima de faltas\n3. Salir')
            op = int(input('Opción: '))
            os.system('cls')
            menu.menu(op)
            band = op == 3