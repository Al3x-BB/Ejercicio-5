import re
class claseAlumno:
    __nom = ''  #nombre del alumno
    __ano = ''  #año a la que asiste
    __div = ''  #división a la que asiste
    __ina = 0   #cantidad de inasistencias
    __inaMax = 0    #cantidad de inasistencias máxima que se puede tener
    __clasesT = 0   #cantidad de clases totales
    def __init__(self, nom, ano, div, ina, inaMax, clasesT):
        if(re.match('^[a-z\ ]{3,40}$', nom.lower())):
            if(re.match('^[a-z1-9]{1,40}$', ano.lower())):
                if(re.match('^[a-z]{1,7}$', div.lower())):
                    if(ina >= 0):
                        if(inaMax >= 0):
                            if(clasesT >= 0):
                                self.__nom = nom
                                self.__ano = ano
                                self.__div = div
                                self.__ina = ina
                                self.__inaMax = inaMax
                                self.__clasesT = clasesT
                            else: print('ERROR: cantidad de clases totales inválida')
                        else: print('ERROR: cantidad de inasistencias máximas inválida')
                    else: print('ERROR: cantidad de inasistencias inválida')
                else: print('ERROR: división inválida')
            else: print('ERROR: año inválido')
        else: print('ERROR: nombre inválido')
    def getNom(self):
        return self.__nom
    def getIna(self):
        return self.__ina
    def getAno(self):
        return self.__ano
    def getDiv(self):
        return self.__div
    def getInaMax(self):
        return self.__inaMax
    def modInaMax(self, cant):
        self.__inaMax = cant