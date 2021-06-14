import json
from pathlib import Path
from ClaseProvincia import Provincia
from ManejadorProvincias import ManejadorProvincias
class ObjectEncoder:
    def decodificarDiccionario(self,d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name == 'ManejadorProvincias':
                provincias=d['provincias']
                manejador= class_()
                for i in range(len(provincias)):
                    dProvincia= provincias[i]
                    class_name=dProvincia.pop('__class__')
                    class_=eval(class_name)
                    atributos=dProvincia['__atributos__']
                    unaProvincia= class_(**atributos)
                    manejador.agregarProvincia(unaProvincia)
            return manejador
    def guardarJSONArchivo(self,diccionario,archivo):
        with Path(archivo).open("w",encoding="UTF-8") as destino:
            json.dump(diccionario,destino,indent=4)
            destino.close()
    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario= json.load(fuente)
            fuente.close()
            return diccionario

