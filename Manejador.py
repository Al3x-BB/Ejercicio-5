from Alumno import claseAlumno
import csv
class claseManejador:
    __lista = []
    __lista2 = []
    def __init__(self, lista = []):
        self.__lista = lista
        self.__lista2 = []
    def crearLista(self):   #crea la lista de alumnos a través del archivo csv
        band = False
        reader = csv.reader(open('Lista de ALumnos.csv'), delimiter = ';')
        for fila in reader:
            if(band == False):
                band = True
            else:
                unAlumno = claseAlumno(str(fila[0]), str(fila[1]), str(fila[2]), int(fila[3]), int(fila[4]),
                                       int(fila[5]))
                self.__lista.append(unAlumno)
        if(self.__lista != None):
            print('DATO: se creó la lista correctamente')
        else: print('ERROR: no se creó la lista correctamente')
    def obtAlum(self, ano, div):    #crea una lista con los alumnos que superan la cant de inasistencias máxima
        for i in range(len(self.__lista)):
            if (ano == self.__lista[i].getAno() and div == self.__lista[i].getDiv() and
                    self.__lista[i].getIna() > self.__lista[i].getInaMax()):
                self.__lista2.append(self.__lista[i])
    def mostrarLista(self): #muestra la lista
        cab = """\
        +---------------------------------+
        | Alumno               Porcentaje |
        +---------------------------------+\
        """
        cuerpo = """\
        | {:20}      {:4}% |\
        """
        print(cab)
        for i in range(len(self.__lista2)):
            print(cuerpo.format(self.__lista2[i].getNom(),
                                round((self.__lista2[i].getIna()*100)/self.__lista2[i].getInaMax())))
    def mod(self, max): #modifica la cantidad máxima de inasistencias
        for i in range(len(self.__lista)):
            self.__lista[i].modInaMax(max)
        print('DATO: la cantidad máxima de inasistencias se modificó')
    def clear(self):
        self.__lista2.clear()