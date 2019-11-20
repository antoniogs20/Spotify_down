import os
from tkinter import *
from tkinter import simpledialog
import tkinter.messagebox
import subprocess
class State:
   def __init__(self):
       self.b = False
 
   def setB(self, setTo):
       self.b = setTo
string= State()
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
        b = Button(self.master,text='okay',command= lambda: (string.setB((e.get())),self.master.destroy()))
        b.pack(side='bottom')
    def ventana_boton(self,comando):
        B = Button(self.master, text =self.message, font='3', command = comando,height='2' ,width='20',activebackground='red',activeforeground='blue',bg='green')
        if self.imagen != []:
            self.master.iconphoto(False,self.imagen)
            B.config(image=self.imagen,width="100", height="100")
        B.place(relx=0.5 , rely=0.5 , anchor=CENTER)
def mag(command):
    #os.system("spotdl --playlist https://open.spotify.com/playlist/0TIQY3zUjsz9qQ4peSsyYl?si=XeklxAOETDSSkQZ_cnO7CQ --write-to /Users/Armayor/lista_nueva.txt")
    subprocess.Popen(['C:\\Users\\anton\\Desktop\\Spoty\\magia.bat'])
    subprocess.Popen(['command'])
    subprocess.Popen('spotdl --overwrite skip --list piso-roma.txt')
    top.destroy()

root = Tk()
p1=PhotoImage(file="logo.png")
texto = ventana(root,geometry='900x80',title='Introduce URL playlist',imagen=p1,back='Red')
texto.introducir_texto()
root.mainloop()
comando = r'spotdl --playlist ' +string.b+  r' --write-to C:\Users\anton\Desktop\Spoty\lista_nueva.txt'

top = Tk()
p1=PhotoImage(file="logo.png")
boton = ventana(top, title='Magia', geometry='500x500',imagen = p1,back = 'black')
boton.ventana_boton(comando= lambda: mag(comando))
top.mainloop()

finish = Tk()
p1=PhotoImage(file="logo.png")
fin = ventana(finish, title='Fin', geometry='300x300',back='black', mensaje= 'Cerrar')
fin.ventana_boton(comando= lambda: finish.destroy())
finish.mainloop()
