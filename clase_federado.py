class Federado:
    __apellido:str
    __nombre:str
    __dni:int
    __edad:int
    __club:str

    def __init__(self,ape,nom,dnx,ed,clux):
        self.__apellido = ape
        self.__nombre = nom
        self.__dni = dnx
        self.__edad = ed
        self.__club = clux
    
    def get_apellido(self):
        return self.__apellido
    def get_nombre(self):
        return self.__nombre
    def get_dni(self):
        return self.__dni
    def get_edad(self):
        return self.__edad
    def get_club(self):
        return self.__club