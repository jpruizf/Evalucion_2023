class Puntaje:
    __valor1:int
    __valor2:int
    __valor3:int
    __prom:int
    def __init__(self,punt1,punt2,punt3):
        self.__valor1 = punt1
        self.__valor2 = punt2
        self.__valor3 = punt3
        self.__prom = None

    def get_puntos(self):
        return f"Puntaje 1->{self.__valor1}/Puntaje 2->{self.__valor2}/Puntaje 3->{self.__valor3}"
    def calcular_promedio(self):
        self.__prom += int((self.__valor1+self.__valor2+self.__valor3)/3)
        return self.__prom

    def __gt__(self,otro):
        return self.__prom > otro.mostrar_promedio()