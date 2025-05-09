from clase_evalucion import Evalucion
import csv

class Gestor_Evaluacion:
    __listado_evaluacion:list

    def __init__(self):
        self.__listado_evaluacion = []
    
    def agregar_evaluacion(self,Una_evaluacion):
        self.__listado_evaluacion.append(Una_evaluacion)
    
    def cargar_evaluacion(self):
        with open('evaluacion.csv') as archivo_pilo:
            lector = csv.reader(archivo_pilo,delimiter=';')
            for fila in lector:
                aux_dx = fila[0]
                aux_estil = fila[1]
                evax = Evalucion(aux_dx,aux_estil)
                self.agregar_evaluacion(evax)
        archivo_pilo.close()
    '''inciso a'''
    def buscar_estilo(self,elemento):
        bandera = False
        encontrado = None
        indice = None
        while not bandera and indice < len(self.__listado_evaluacion):
            if elemento == self.__listado_evaluacion[indice].get_estilo():
                bandera = True
                encontrado = indice
            else:
                indice += 1
        return encontrado
    
    def buscar_mas_de_un_estilos(self):
        bandera = False
        encontrado = None
        indice = None
        while not bandera and indice < len(self.__listado_evaluacion):
            if self.__listado_evaluacion[indice].get_estilo() == 'L' and self.__listado_evaluacion[indice].get_estilo() == 'E':
                bandera = True
                encontrado = self.__listado_evaluacion[indice].get_dni()
            else:
                indice += 1
        return encontrado