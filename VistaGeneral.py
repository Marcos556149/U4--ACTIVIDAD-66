import json
import requests
from ClaseProvincia import Provincia
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
class Vista(Tk):
    __ventana= None
    def __init__(self):
        super().__init__()
        self.title("Lista de Provincias")
        self.list= ProvinciaLista(self,height=15)
        self.form=UpdateFormularioProvincia(self)
        self.btn_new= tk.Button(self,text="Agregar Provincia")
        self.list.pack(side=tk.LEFT,padx=10,pady=10)
        self.form.pack(padx=10,pady=10)
        self.btn_new.pack(side=tk.BOTTOM,pady=5)
    def setControlador(self,ctrl):
        self.btn_new.config(command=ctrl.crearProvincia)
        self.list.bind_doble_click(ctrl.seleccionarProvincia)
    def agregarProvincia(self,provincia):
        self.list.insertar(provincia)
    def verProvinciaEnForm(self,provincia):
        self.form.mostrarProvinciasEnFormulario(provincia)
class DatosProvincia(tk.LabelFrame):
    fields=("Nombre","Capital","Cantidad de habitantes","Cantidad de departamentos/partidos","Temperatura","Sensacion térmica","Humedad")
    def __init__(self,master,**kwargs):
        if NuevaProvincia.paraNuevaProvincia == 1:
            self.fields=("Nombre","Capital","Cantidad de habitantes","Cantidad de departamentos/partidos")
        super().__init__(master,text="Provincia",padx=10,pady=10,**kwargs)
        self.frame= tk.Frame(self)
        self.entries= list(map(self.crearCampo,enumerate(self.fields)))
        self.frame.pack()
    def crearCampo(self,field):
        position, text=field
        label= tk.Label(self.frame,text=text)
        entry=tk.Entry(self.frame,width=25)
        label.grid(row=position,column=0,pady=5)
        entry.grid(row=position,column=1,pady=5)
        return entry
    def mostrarProvinciasEnFormulario(self,provincia):
        values=(provincia.getNombre(),provincia.getCapital(),provincia.getCantHabitantes(),provincia.getCantDepPar(),temp,sens,hum)
        for entry,value in zip(self.entries,values):
            entry.delete(0,tk.END)
            entry.insert(0,value)
    def crearProvinciaDesdeFormulario(self):
        values= [e.get() for e in self.entries]
        provincia= None
        try:
            provincia= Provincia(values[0],values[1],values[2],values[3])
        except ValueError as e:
            messagebox.showerror("Error de validacion",str(e),parent=self)
        return provincia
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0,tk.END)
class ProvinciaLista(tk.Frame):
    def __init__(self,master,**kwargs):
        super().__init__(master)
        self.lb=tk.Listbox(self,**kwargs)
        scroll= tk.Scrollbar(self,command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT,fill=tk.Y)
        self.lb.pack(side=tk.LEFT,fill=tk.BOTH,expand=1)
    def insertar(self,provincia,index=tk.END):
        text="{}".format(provincia.getNombre())
        self.lb.insert(index,text)
    def bind_doble_click(self,callback):
        handler = lambda _:callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>",handler)
class NuevaProvincia(tk.Toplevel):
    paraNuevaProvincia = 0
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Nueva Provincia")
        self.provincia= None
        NuevaProvincia.paraNuevaProvincia = 1
        self.form=DatosProvincia(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10,pady=10)
        self.btn_add.pack(pady=10)
    def confirmar(self):
        self.provincia= self.form.crearProvinciaDesdeFormulario()
        if self.provincia:
            self.destroy()
    def show(self):
        self.grab_set()
        self.wait_window()
        return self.provincia
class UpdateFormularioProvincia(DatosProvincia):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        opcs= {"ipadx":5,"padx":5,"pady":20}
        style= ttk.Style()
        style.configure("TLabel",**opcs)
        style.configure("TButton",background="#003249",width=35,padding=10)




