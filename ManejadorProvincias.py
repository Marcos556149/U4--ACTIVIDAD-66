from ClaseProvincia import Provincia
class ManejadorProvincias:
    indice=0
    __listaProvincias= None
    def __init__(self):
        self.__listaProvincias= []
    def agregarProvincia(self,provincia):
        provincia.rowid=ManejadorProvincias.indice
        ManejadorProvincias.indice += 1
        self.__listaProvincias.append(provincia)
    def getListaProvincias(self):
        return self.__listaProvincias
    def getIndiceProvincia(self,provincia):
        bandera= False
        i= 0
        while (bandera == False)and(i< len(self.__listaProvincias)):
            if self.__listaProvincias[i] == provincia.rowid:
                bandera= True
            else:
                i += 1
        return i
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            provincias=[Provincia.toJSON() for Provincia in self.__listaProvincias]
            )
        return d
