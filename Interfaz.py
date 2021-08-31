from tkinter import *
from tkinter import ttk as tk
from Personas import *

class ventana ():
    def __init__(self,title,size,bgColor):
        self.ventana = Tk()
        self.ventana.title(title)
        self.ventana.geometry(size)
        self.ventana.configure(bg = bgColor)

        """ /check box enviado los datos 
        self.generarAuto = BooleanVar()
        self.generarAuto_Entry = Checkbutton(self.ventana,text = 'Si',var = self.generarAuto)
        self.generarAuto_Entry.place(x= 80,y=100)
        """
        #Decalaracion de variables
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.numero = StringVar()
        self.direccion = StringVar()

        #Campos 
        self.etiquetaNom = tk.Label(self.ventana,text="Nombre")
        self.nombre_entry = Entry(self.ventana,textvariable=self.nombre,width=10)
        self.etiquetaNom.place(x=440,y=200)
        self.nombre_entry.place(x=500,y=200)
        

        self.etiquetaApe = tk.Label(self.ventana,text="Apellido")
        self.ape_entry = Entry(self.ventana,textvariable=self.apellido,width=10)
        self.etiquetaApe.place(x=440,y=400)
        self.ape_entry.place(x=500,y=400)


        self.etiquetaNum = tk.Label(self.ventana,text="Numero")
        self.num_entry = Entry(self.ventana,textvariable=self.numero,width=10)
        self.etiquetaNum.place(x=440,y=450)
        self.num_entry.place(x=500,y=450)

        self.etiquetaDirec = tk.Label(self.ventana,text="Direccion")
        self.direc_entry = Entry(self.ventana,textvariable=self.direccion,width=10)
        self.etiquetaDirec.place(x=440,y=500)
        self.direc_entry.place(x=500,y=500)



        self.boton2 = tk.Button(self.ventana,text = 'Aceptar',command=self.send_data)
        self.boton2.place(x=440,y=600)

        self.ventana.mainloop()

    def send_data(self):

        self.nombre_data = self.nombre.get()
        self.apellido_data = self.apellido.get()
        self.numero_data = self.numero.get()
        self.direccion_data = self.direccion.get()

        ##Sentecia de pedido

        pepe = Persona(self.nombre_data,self.apellido_data,self.numero_data,self.direccion_data)
        self.ventana.destroy()

        

        



        


"""
def pruebas():
    generarAuto_data = generarAuto.get()
    if generarAuto_data == True:
        print("Entro")
    else:
        print(False)
    
ventana  = tk.Tk()
ventana.title("Parcial Corte 1 ")
ventana.geometry('980x680')
ventana.configure(background = '#151934')

generarAuto = BooleanVar()


generarAuto_Entry = Checkbutton(ventana,text = 'Si',var = generarAuto)
generarAuto_Entry.place(x= 80,y=100)

boton2 = ttk.Button(ventana,text = 'Aceptar',command=pruebas)
boton2.place(x=80,y=80)
"""






def main():
    mi_app = ventana("Parcial Corte 1 ",'980x680','#151934')
    return 0



main()