from clase_federado import Federado
from clase_puntaje import Puntaje
import csv

class Gestor_Federado:
    __listado_fede:list

    def __init__(self):
        self.__listado_fede = []

    def agragar_federado(self,Un_federado):
        self.__listado_fede.append(Un_federado)
        
    def agregar_puntaje(self,Un_puntaje):
        self.__listado_fede.append(Un_puntaje)
    def cargar_federado(self):
        bandera = False
        with open('federados.csv') as archivo_fede:
            lector = csv.reader(archivo_fede,delimiter=';')
            for fila in lector:
                if not bandera:
                    bandera = True
                else:
                    ape = fila[0]
                    nom = fila[1]
                    dnxx = fila[2]
                    eda = fila[3]
                    clu = fila[4]
                    fedex = Federado(ape,nom,dnxx,eda,clu)
                    self.agragar_federado(fedex)
        archivo_fede.close()
    def cargar_puntaje(self):
        bandera = False
        with open('evaluacion.csv') as archivo_eva:
            lector = csv.reader(archivo_eva,delimiter=';')
            for fila in lector:
                if not bandera:
                    bandera = True
                else:
                    p1 = fila[2]
                    p2 = fila[3]
                    p3 = fila[4]
                    Pux = Puntaje(p1,p2,p3)
                    self.agregar_puntaje(Pux)
        archivo_eva.close()
    '''inciso a'''
    def mostrar_estilo(self,elemeto):
        for i in range(self.__listado_fede):
            print(f"{self.__listado_fede[i].get_apellido()}/{self.__listado_fede[i].get_nombre()}/{self.__listado_fede[i].get_dni()}")
    '''inciso b'''
    def ordenar_puntaje(self):
        self.__listado_fede.sort()
    
    '''inciso c'''
    def listado_mas_estilos(self,code):
        indice = None
        while indice < len(self.__listado_fede):
            if self.__listado_fede[indice].get_dni() == code:
                print(f"{self.__listado_fede[code].get_apellido()}/{self.__listado_fede[code].get_nombre()}/{self.__listado_fede[indice].get_dni()}/{self.__listado_fede[indice].get_edad()}/{self.__listado_fede[indice].get_club()}")
                indice += 1
            else:
                print("Error :/")
    '''inciso d'''
    def mostrar_puntos(self,elemento):
        for i in range(self.__listado_fede):
            if self.__listado_fede[i].get_dni() == elemento:
                print(self.__listado_fede[i].get_puntos())