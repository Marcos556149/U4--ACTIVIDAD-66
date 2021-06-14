from ManejadorProvincias import ManejadorProvincias
from ClaseObjectEncoder import ObjectEncoder
from ClaseProvincia import Provincia
class RepositorioProvincias:
    __conn= None
    __manejador= None
    def __init__(self,conn):
        self.__conn= conn
        diccionario= self.__conn.leerJSONArchivo('datos.json')
        self.__manejador=self.__conn.decodificarDiccionario(diccionario)
    def obtenerListaProvincias(self):
        return self.__manejador.getListaProvincias()
    def agregarProvincia(self,provincia):
        self.__manejador.agregarProvincia(provincia)
        return provincia
    def guardarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON(),'datos.json')
