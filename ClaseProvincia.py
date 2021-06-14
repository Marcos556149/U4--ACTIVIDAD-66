class Provincia:
    __nombre= ''
    __capital= ''
    __cantHabitantes= 0
    __cantDepPar= 0
    def __init__(self,nom='',cap='',cantH=0,cantD=0):
        self.__nombre= self.requerido(nom,'Nombre es un valor requerido')
        self.__capital= self.requerido(cap,'capital es un valor requerido')
        self.__cantHabitantes= self.ValorCorrecto(cantH,'Cantidad de Habitantes es un valor requerido')
        self.__cantDepPar= cantD= self.ValorCorrecto(cantD, 'Cantidad de Departamentos/Partidos es un valor requerido')
    def getNombre(self):
        return self.__nombre
    def getCapital(self):
        return self.__capital
    def getCantHabitantes(self):
        return self.__cantHabitantes
    def getCantDepPar(self):
        return self.__cantDepPar
    def requerido(self,valor,mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    def ValorCorrecto(self,valor,mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    def toJSON(self):
        d= dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                nom= self.__nombre,
                cap= self.__capital,
                cantH= self.__cantHabitantes,
                cantD= self.__cantDepPar
                     )
            )
        return d

