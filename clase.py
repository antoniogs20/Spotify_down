import os
from tkinter import *
from tkinter import simpledialog
import tkinter.messagebox
import subprocess
#from pygame import mixer
class ventana:
    def __init__(self, master,title='',geometry='500x500',imagen=[],back=[],mensaje=[]):
        self.master = master
        self.back = back
        self.message = mensaje
        self.imagen = imagen
        master.title(title)
        master.geometry(geometry)
        master.configure(bg=self.back)
        if imagen != []:
            master.iconphoto(False,self.imagen)
    def introducir_texto(self):
        e = Entry(self.master, width = '100',textvariable='Introduce')
        e.place(relx=0.5 , rely=0.5 , anchor=CENTER)
        e.focus_set()
        b = Button(self.master,text='okay',command=lambda:get_URL(e));
        b.pack(side='bottom')
    def ventana_boton(self,comando):
        B = Button(self.master, text =self.message, font='3', command = comando,height='2' ,width='20',activebackground='red',activeforeground='blue',bg='green')
        if self.imagen != []:
            self.master.iconphoto(False,self.imagen)
            B.config(image=self.imagen,width="100", height="100")
        else:
            B.config(width="100", height="100")
        B.place(relx=0.5 , rely=0.5 , anchor=CENTER)


prueba = Tk()
prue = ventana(prueba)
prueba.mainloop()