import tkinter as tk
from VistaGeneral import Vista,NuevaProvincia
from ManejadorProvincias import ManejadorProvincias
class ControladorProvincias:
    def __init__(self,repo,vista):
        self.repo= repo
        self.vista= vista
        self.seleccion=-1
        self.provincias= list(repo.obtenerListaProvincias())
    def crearProvincia(self):
        nuevaProvincia= NuevaProvincia(self.vista).show()
        if nuevaProvincia:
            provincia= self.repo.agregarProvincia(nuevaProvincia)
            self.provincias.append(provincia)
            self.vista.agregarProvincia(provincia)
    def seleccionarProvincia(self,index):
        self.seleccion= index
        provincia=self.provincias[index]
        self.vista.verProvinciaEnForm(provincia)
    def start(self):
        for c in self.provincias:
            self.vista.agregarProvincia(c)
        self.vista.mainloop()
    def salirGrabarDatos(self):
        self.repo.guardarDatos()

