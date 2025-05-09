class Evalucion:
    __aux_dni:int
    __estilo:str

    def __init__(self,aux_d,est):
        self.__aux_dni = aux_d
        self.__estilo = est

    def get_dni(self):
        return self.__aux_dni
    def get_estilo(self):
        return self.__estilo